from core.attributes import Attrs
from core.context import DrawContext
from core.elements import Element
from core.node import DrawNode, DrawNodeType, Length, Parent


class Spacer(Element):
    def __init__(
        self,
        width=None,
        height=None,
        color=(255, 0, 0),
        attrs: Attrs = [],
    ):
        super().__init__(attrs=attrs)
        self.width = width
        self.height = height
        self.color = color

    def on_layout(self, context: DrawContext) -> DrawNode:
        return Spacer.Node(color=self.color, w=self.width, h=self.height)

    class Node(DrawNode):
        def __init__(
            self,
            color,
            parent: Parent = None,
            x: Length = None,
            y: Length = None,
            w: Length = None,
            h: Length = None,
            children: list[DrawNodeType] = [],
        ) -> None:
            super().__init__("spacer-element", parent, x, y, w, h, children)
            self.color = color

        def on_draw(self, context: DrawContext):
            context.img_draw.rectangle(self.to_tuple(), fill=self.color)
