from PIL import Image

from core.attributes import Attribute
from core.context import DrawContext
from core.layout import LayoutConstraints
from core.node import DrawNode, DrawNodeType, Parent
from core.unit import Length


class TranslateAttribute(Attribute):
    def __init__(self, x: Length = 0, y: Length = 0):
        super().__init__()
        self.translate_x = x
        self.translate_y = y

    def on_layout(self, context: DrawContext, constraints: LayoutConstraints, target: DrawNode) -> DrawNode:
        translate_node = TranslateAttribute.Node(
            label="translate-attr",
            x=target.x,
            y=target.x,
            w=target.w,
            h=target.h,
            children=[target],
            translate_x=self.translate_x,
            translate_y=self.translate_y,
        )
        target.parent = translate_node
        target.x = self.translate_x
        target.y = self.translate_y
        return translate_node

    class Node(DrawNode):
        def __init__(
            self,
            label,
            translate_x: Length, translate_y: Length,
            parent: Parent = None,
            x: Length = None, y: Length = None,
            w: Length = None, h: Length = None,
            children: list[DrawNodeType] = [],
        ) -> None:
            super().__init__(label, parent, x, y, w, h, children)
            self.translate_x = translate_x
            self.translate_y = translate_y

        def on_draw(self, context: DrawContext, target: DrawNode):
            base = context.img
            context.img = Image.new("RGBA", context.img.size)
            self.draw_children(context)
            base.alpha_composite(context.img, dest=(
                int(self.translate_x), int(self.translate_y)))
            context.img = base
