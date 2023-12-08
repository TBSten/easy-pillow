
from attributes.combine import CombinedAttribute
from attributes.padding import PaddingAttribute
from core.attributes import Attribute
from core.color import Color
from core.context import DrawContext
from core.layout import LayoutConstraints
from core.node import DrawNode, DrawNodeType, Length, Parent
from core.unit import Number


class RoundAttribute(Attribute):
    def __init__(
        self,
        width: Number,
        color: Color,
    ):
        super().__init__()
        self.width = width
        self.color = color

    def on_layout(self, context: DrawContext, constraints: LayoutConstraints, target: DrawNode) -> DrawNode:
        attr_node = RoundAttribute.Node(
            width=self.width,
            color=self.color,
            label="round-attr",
            parent=target.parent,
            w=target.w, h=target.h,
            children=[target],
        )
        target.x = 0
        target.y = 0
        target.parent = attr_node
        return attr_node

    class Node(DrawNode):
        def __init__(
            self,
            label,
            width: Number,
            color: Color,
            parent: Parent = None,
            x: Length = None,
            y: Length = None,
            w: Length = None,
            h: Length = None,
            children: list[DrawNodeType] = [],
        ) -> None:
            super().__init__(label, parent, x, y, w, h, children)
            self.width = width
            self.color = color

        def on_draw(self, context: DrawContext):
            rect = self.to_tuple()
            context.img_draw.rectangle(
                xy=(rect[0], rect[1], rect[2]-1, rect[3]-1),
                outline=self.color.to_tuple(),
                width=self.width,
            )
            self.draw_children(context)


def BorderAttribute(
    width: Number,
    color: Color,
):
    # TODO
    return CombinedAttribute(
        RoundAttribute(
            width=width,
            color=color,
        ),
        PaddingAttribute(width, width, width, width),
    )

# class BorderAttribute(PaddingAttribute):
#     def __init__(
#         self,
#         width: Number,
#         color: Color,
#     ):
#         super().__init__(width,width,width,width)
#         self.color = color

#     def on_layout(self, context: DrawContext, constraints: LayoutConstraints, target: DrawNode) -> DrawNode:
#         return super().on_layout(context, constraints, target)

#     class Node(PaddingAttribute.Node):
#         def __init__(
#             self,
#             padding_node :PaddingAttribute.Node,
#             width: Number,
#             color: Color,
#         ) -> None:
            
#             super().__init__(
#                 padding_node.label, 
#                 padding_node.parent, 
#                 padding_node.x, 
#                 padding_node.y, 
#                 padding_node.w, 
#                 padding_node.h, 
#                 padding_node.children,
#             )
#             self.width = width
#             self.color = color

#         def on_draw(self, context: DrawContext):
#             rect = self.to_tuple()
#             context.img_draw.rectangle(
#                 xy=(rect[0], rect[1], rect[2]-1, rect[3]-1),
#                 outline=self.color.to_tuple(),
#                 width=self.width,
#             )
#             self.draw_children(context)
