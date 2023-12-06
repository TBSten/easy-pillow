from core.attributes import Attribute
from core.context import DrawContext
from core.node import DrawNode


class CombinedAttribute(Attribute):
    def __init__(self, *attrs: Attribute):
        super().__init__()
        self.attrs = attrs

    def on_layout(self, context: DrawContext, target: DrawNode) -> DrawNode:
        node = target
        for attr in reversed(self.attrs):
            node = attr.layout(context, node)
        return node
