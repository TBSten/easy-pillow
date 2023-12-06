
from abc import ABCMeta, abstractmethod

from core.attributes import Attrs
from core.context import DrawContext
from core.node import DrawNode


class Element(metaclass=ABCMeta):
    def __init__(self, attrs: Attrs = []):
        self.attrs = attrs

    def layout(self, context: DrawContext) -> DrawNode:
        node = self.on_layout(context)
        for attr in reversed(self.attrs):
            node = attr.layout(context, node)
        return node

    @abstractmethod
    def on_layout(self, context: DrawContext) -> DrawNode:
        pass
