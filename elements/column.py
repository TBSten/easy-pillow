from typing import cast

from core.attributes import Attrs
from core.context import DrawContext
from core.elements import Element
from core.node import DrawNode


class ColumnElement(Element):
    def __init__(
        self,
        children: list[Element] = [],
        attrs: Attrs = [],
    ):
        super().__init__(attrs)
        self.children = children

    def on_layout(self, context: DrawContext) -> DrawNode:
        column_node = ColumnElement.Node(label="column_node")
        w = 0
        h = 0
        children: list[DrawNode] = []
        for child in self.children:
            child_node = child.layout(context)
            child_node.parent = column_node
            child_node_w = child_node.w
            child_node.w = child_node_w = cast(
                int,
                child_node_w if child_node_w is not None else -1,
            )
            child_node_h = child_node.h
            if child_node_h is None:
                raise NotImplementedError(
                    f"invalid child_node height {child_node_h}"
                )

            child_node.x = 0
            child_node.y = h
            child_node.parent = column_node
            children.append(child_node)

            if w < child_node_w:
                w = child_node_w
            h += child_node_h

        print("column children", w, h)
        for child in children:
            if child.w == -1:
                child.w = w
            print("column child", child)
        column_node.w = w
        column_node.h = h
        column_node.children = children
        return column_node

    class Node(DrawNode):
        def on_draw(self, context: DrawContext):
            self.draw_children(context)
            context.img_draw.rectangle(
                self.to_tuple(),
                outline=(255, 0, 0),
                width=1,
            )
