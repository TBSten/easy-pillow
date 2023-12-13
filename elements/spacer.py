from core.attributes import Attrs
from core.context import DrawContext
from core.elements import Element
from core.layout import LayoutConstraints
from core.node import DrawNode, DrawNodeType, Length, Parent


class Spacer(Element):
    def __init__(
        self,
        attrs: Attrs = [],
    ):
        super().__init__(attrs=attrs)

    def layout(self, context: DrawContext, constraints: LayoutConstraints) -> DrawNode:
        node = super().layout(context, constraints)
        return node

    def on_layout(self, context: DrawContext, constraints: LayoutConstraints) -> DrawNode:
        return Spacer.Node(
            w=constraints.get_width_with_constraints(0),
            h=constraints.get_height_with_constraints(0),
        )

    class Node(DrawNode):
        def __init__(
            self,
            parent: Parent = None,
            x: Length = None,
            y: Length = None,
            w: Length = 0,
            h: Length = 0,
            children: list[DrawNodeType] = [],
        ) -> None:
            super().__init__("spacer-element", parent, x, y, w, h, children)

        def on_draw(self, context: DrawContext):
            pass
