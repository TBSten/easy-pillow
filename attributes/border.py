
from attributes.combine import CombinedAttribute
from attributes.padding import PaddingAttribute
from core.attributes import Attribute
from core.color import Color
from core.context import DrawContext
from core.layout import Number
from core.node import DrawNode, DrawNodeType, Length, Parent


class RoundAttribute(Attribute):
    def __init__(
        self,
        width: Number,
        color: Color,
    ):
        super().__init__()
        self.width = width
        self.color = color

    def on_layout(self, context: DrawContext, target: DrawNode) -> DrawNode:
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
