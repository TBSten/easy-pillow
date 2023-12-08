from core.attributes import Attribute
from core.color import Color
from core.context import DrawContext
from core.layout import LayoutConstraints
from core.node import DrawNode, DrawNodeType, Length, Parent


class BackgroundAttribute(Attribute):
    def __init__(self, color: Color = Color.TRANSPARENT):
        super().__init__()
        self.color = color

    def on_layout(self, context: DrawContext, constraints: LayoutConstraints, target: DrawNode) -> DrawNode:
        attr_node = BackgroundAttribute.Node(
            label="background-attr-"+str(self.color),
            color=self.color,
            x=target.x,
            y=target.y,
            w=target.w,
            h=target.h,
            children=[target],
        )
        target.parent = attr_node
        target.x = 0
        target.y = 0
        return attr_node

    class Node(DrawNode):
        def __init__(
            self,
            label,
            color: Color,
            parent: Parent = None,
            x: Length = None,
            y: Length = None,
            w: Length = None,
            h: Length = None,
            children: list[DrawNodeType] = [],
        ) -> None:
            super().__init__(label, parent, x, y, w, h, children)
            self.color = color

        def on_draw(self, context: DrawContext):
            rect = self.to_tuple()
            if all([self.w is not None and self.w >= 2, self.h is not None and self.h >= 2]):
                context.img_draw.rectangle(
                    (rect[0], rect[1], rect[2]-1, rect[3]-1), fill=self.color.to_tuple(),
                )
            self.draw_children(context)
