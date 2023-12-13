
from attributes.combine import CombinedAttribute
from attributes.padding import PaddingAttribute
from core.attributes import Attribute
from core.color import Color
from core.context import DrawContext
from core.layout import LayoutConstraints
from core.node import DrawNode, DrawNodeType, Length, Parent
from core.unit import Number


class BorderAttribute(PaddingAttribute):
    def __init__(
        self,
        width: Number,
        color: Color,
    ):
        super().__init__(
            left=width,
            top=width,
            right=width,
            bottom=width,
        )
        self.width = width
        self.color = color

    def set_constraints(self, context: DrawContext, constraints: LayoutConstraints) -> LayoutConstraints:
        return constraints.copy(
            max_w=constraints.max_w if constraints.max_w is not None else None,
            max_h=constraints.max_h if constraints.max_h is not None else None,
        )

    def on_layout(self, context: DrawContext, constraints: LayoutConstraints, target: DrawNode):
        pass

    def on_draw(self, context: DrawContext, target: DrawNode):
        print("round attr draw")
        super().on_draw(context, target)
        rect = target.to_tuple()
        context.img_draw.rectangle(
            xy=(
                rect[0], rect[1],
                rect[2]-1, rect[3]-1,
            ),
            outline=self.color.to_tuple(),
            width=self.width,
        )


# def BorderAttribute(
#     width: Number,
#     color: Color,
# ):
#     # TODO
#     return CombinedAttribute(
#         RoundAttribute(
#             width=width,
#             color=color,
#         ),
#         PaddingAttribute(width, width, width, width),
#     )

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
