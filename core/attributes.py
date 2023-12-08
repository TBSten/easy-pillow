
from abc import ABCMeta, abstractmethod
from typing import TypeAlias

from core.context import DrawContext
from core.layout import LayoutConstraints
from core.node import DrawNode


class Attribute(metaclass=ABCMeta):
    def __init__(self):
        pass

    def set_constraints(self, context: DrawContext, constraints: LayoutConstraints) -> LayoutConstraints:
        return constraints.copy()

    def layout(self, context: DrawContext, constraints: LayoutConstraints, target: DrawNode) -> DrawNode:
        node = self.on_layout(context, constraints, target)
        node.w = constraints.get_width_with_constraints(node.w)
        node.h = constraints.get_height_with_constraints(node.h)
        return node

    @abstractmethod
    def on_layout(self, context: DrawContext, constraints: LayoutConstraints, target: DrawNode) -> DrawNode:
        pass


Attrs: TypeAlias = "list[Attribute]"
