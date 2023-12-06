
from abc import ABCMeta, abstractmethod
from typing import TypeAlias

from core.context import DrawContext
from core.layout import Offset
from core.node import DrawNode


class Attribute(metaclass=ABCMeta):
    def __init__(self):
        pass

    def layout(self, context: DrawContext, target: DrawNode) -> DrawNode:
        return self.on_layout(context, target)

    @abstractmethod
    def on_layout(self, context: DrawContext, target: DrawNode) -> DrawNode:
        pass


Attrs: TypeAlias = "list[Attribute]"
