from core.attributes import Attribute
from core.context import DrawContext
from core.layout import LayoutConstraints
from core.node import DrawNode


class CombinedAttribute(Attribute):
    def __init__(self, *attrs: Attribute):
        super().__init__()
        self.attrs = attrs

    def set_constraints(self, context: DrawContext, constraints: LayoutConstraints) -> LayoutConstraints:
        for attr in self.attrs:
            constraints = attr.set_constraints(context, constraints)
        return constraints

    def on_layout(self, context: DrawContext, constraints: LayoutConstraints, target: DrawNode):
        node = target
        for attr in reversed(self.attrs):
            attr.layout(context, constraints, node)

    def on_draw(self, context: DrawContext, target: DrawNode):
        for attr in self.attrs:
            attr.draw(context, target)
