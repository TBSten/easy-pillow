
from PIL import Image

from core.attributes import Attrs
from core.context import DrawContext
from core.elements import Element
from core.layout import LayoutConstraints
from core.node import DrawNode, DrawNodeType, Parent
from core.unit import Length


class PillowImageElement(Element):
    def __init__(
        self,
        img: Image.Image,
        attrs: Attrs = [],
    ):
        super().__init__(attrs)
        self.img = img

    def on_layout(self, context: DrawContext, constraints: LayoutConstraints) -> DrawNode:
        print(self.img.height, constraints)
        return PillowImageElement.Node(
            img=self.img,
            label="pillow-image-element",
            w=constraints.get_width_with_constraints(self.img.width),
            h=constraints.get_height_with_constraints(self.img.height),
        )

    class Node(DrawNode):
        def __init__(self, label, img: Image.Image, parent: Parent = None, x: Length = None, y: Length = None, w: Length = None, h: Length = None) -> None:
            super().__init__(
                label,
                parent,
                x, y,
                w, h,
                children=[],
            )
            self.img = img

        def on_draw(self, context: DrawContext):
            context.img.alpha_composite(
                self.img,
                dest=(int(self.absolute_x), int(self.absolute_y)),
            )
            self.draw_children(context)
