
from abc import ABCMeta, abstractmethod
from typing import TypeAlias

from PIL import Image

from core.context import DrawContext
from core.layout import LayoutConstraints
from core.node import DrawNode


class Attribute(metaclass=ABCMeta):

    def __init__(self):
        self._children = []

    def set_constraints(self, context: DrawContext, constraints: LayoutConstraints) -> LayoutConstraints:
        return constraints.copy()

    def layout(self, context: DrawContext, constraints: LayoutConstraints, target: DrawNode) -> None:
        self.on_layout(context, constraints, target)

    @abstractmethod
    def on_layout(self, context: DrawContext, constraints: LayoutConstraints, target: DrawNode):
        pass

    def draw(self, context: DrawContext, target: DrawNode):
        base_img = context.img
        context.img = Image.new("RGBA", base_img.size)
        self.on_draw(context, target)
        context.img = Image.alpha_composite(base_img, context.img)

    @abstractmethod
    def on_draw(self, context: DrawContext, target: DrawNode):
        pass


Attrs: TypeAlias = "list[Attribute]"
