from typing import cast

from core.attributes import Attrs
from core.context import DrawContext
from core.elements import Element
from core.node import DrawNode


class RowElement(Element):
    def __init__(
        self,
        children: list[Element] = [],
        attrs: Attrs = [],
    ):
        super().__init__(attrs)
        self.children = children

    def on_layout(self, context: DrawContext) -> DrawNode:
        row_node = RowElement.Node(label="row-element")
        w = 0
        h = 0
        children: list[DrawNode] = []
        for child in self.children:
            child_node = child.layout(context)
            child_node.parent = row_node
            child_node_h = child_node.h
            child_node.h = child_node_h = cast(
                int,
                child_node_h if child_node_h is not None else -1,
            )
            child_node_w = child_node.w
            if child_node_w is None:
                raise NotImplementedError(
                    f"invalid child_node width {child_node_w}"
                )

            child_node.x = w
            child_node.y = 0
            children.append(child_node)

            if h < child_node_h:
                h = child_node_h
            w += child_node_w

        for child in children:
            if child.w == -1:
                child.w = w
        row_node.w = w
        row_node.h = h
        row_node.children = children
        return row_node

    class Node(DrawNode):
        def on_draw(self, context: DrawContext):
            self.draw_children(context)
            context.img_draw.rectangle(
                self.to_tuple(),
                outline=(255, 0, 0),
                width=1,
            )
