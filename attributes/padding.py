from core.attributes import Attribute
from core.context import DrawContext
from core.layout import LayoutConstraints
from core.node import DrawNode
from core.unit import Number


class PaddingAttribute(Attribute):
    def __init__(self, left: Number = 0, top: Number = 0, right: Number = 0, bottom: Number = 0):
        super().__init__()
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom

    def set_constraints(self, context: DrawContext, constraints: LayoutConstraints) -> LayoutConstraints:
        con = constraints.copy(
            min_w=constraints.min_w - self.left - self.right if constraints.min_w is not None else None,
            min_h=constraints.min_h - self.top - self.bottom if constraints.min_h is not None else None,            
            max_w=constraints.max_w - self.left - self.right if constraints.max_w is not None else None,
            max_h=constraints.max_h - self.top - self.bottom if constraints.max_h is not None else None,            
        )
        print("    ->", con)
        return con

    def on_layout(self, context: DrawContext, constraints: LayoutConstraints, target: DrawNode) -> DrawNode:
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
            label="padding-attr",
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
