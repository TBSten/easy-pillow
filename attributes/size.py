from attributes.combine import CombinedAttribute
from core.attributes import Attribute, Attrs
from core.context import DrawContext
from core.layout import LayoutConstraints
from core.node import DrawNode, DrawNodeType, Length, Parent
from core.unit import Number


class WidthAttribute(Attribute):
    def __init__(self, width: Length):
        super().__init__()
        self.width = width

    def set_constraints(self, context: DrawContext, constraints: LayoutConstraints) -> LayoutConstraints:
        return constraints.copy(
            min_w=self.width,
            max_w=self.width,
        )

    def on_layout(self, context: DrawContext, constraints: LayoutConstraints, target: DrawNode) -> DrawNode:
        return target

    class Node(DrawNode):
        def __init__(
            self,
            label,
            parent: Parent = None,
            x: Length = None,
            y: Length = None,
            w: Length = None,
            h: Length = None,
            children: list[DrawNodeType] = [],
        ) -> None:
            super().__init__(label, parent, x, y, w, h, children)

        def on_draw(self, context: DrawContext):
            self.draw_children(context)


class HeightAttribute(Attribute):
    def __init__(self, height: Length):
        super().__init__()
        self.height = height

    def set_constraints(self, context: DrawContext, constraints: LayoutConstraints) -> LayoutConstraints:
        return constraints.copy(
            min_h=self.height,
            max_h=self.height,
        )

    def on_layout(self, context: DrawContext, constraints: LayoutConstraints, target: DrawNode) -> DrawNode:
        return target

    class Node(DrawNode):
        def __init__(
            self,
            label,
            parent: Parent = None,
            x: Length = None,
            y: Length = None,
            w: Length = None,
            h: Length = None,
            children: list[DrawNodeType] = [],
        ) -> None:
            super().__init__(label, parent, x, y, w, h, children)

        def on_draw(self, context: DrawContext):
            self.draw_children(context)


def size(width: Number, height: Number):
    return CombinedAttribute(
        WidthAttribute(width),
        HeightAttribute(height),
    )
