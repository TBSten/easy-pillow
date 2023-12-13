
from abc import ABCMeta, abstractmethod

from core.attributes import Attrs
from core.context import DrawContext
from core.layout import LayoutConstraints
from core.node import DrawNode, DrawNodeType, Parent
from core.unit import Length


class Element(metaclass=ABCMeta):
    def __init__(self, attrs: Attrs = []):
        self.attrs = attrs

    def layout(self, context: DrawContext, constraints: LayoutConstraints) -> DrawNode:
        parent_constraints = constraints
        for attr in self.attrs:
            constraints = attr.set_constraints(context, constraints)
        node = self.on_layout(context, constraints.copy())
        for attr in reversed(self.attrs):
            attr.layout(context, constraints, node)
        # あってるか不安
        node.w = parent_constraints.get_width_with_constraints(node.w)
        node.h = parent_constraints.get_height_with_constraints(node.h)
        node.add_attrs(self.attrs)
        return node

    @abstractmethod
    def on_layout(self, context: DrawContext, constraints: LayoutConstraints) -> DrawNode:
        pass
