from core.attributes import Attribute
from core.context import DrawContext
from core.node import DrawNode


class PaddingAttribute(Attribute):
    def __init__(self, left=0, top=0, right=0, bottom=0):
        super().__init__()
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom

    def on_layout(self, context: DrawContext, target: DrawNode) -> DrawNode:
        left = self.left
        top = self.top
        right = self.right
        bottom = self.bottom
        target_w = target.w
        if target_w is None:
            raise NotImplementedError(
                f"invalid target.w:{target_w} for padding attr"
            )
        target_h = target.h
        if target_h is None:
            raise NotImplementedError(
                f"invalid target.h:{target_h} for padding attr"
            )

        attr_node = PaddingAttribute.Node(
            label="test-attr",
            x=target.x, y=target.y,
            w=left+target_w+right, h=top+target_h+bottom,
            children=[target],
        )
        target.x = left
        target.y = top
        target.parent = attr_node
        return attr_node

    class Node(DrawNode):
        def on_draw(self, context: DrawContext):
            self.draw_children(context)
