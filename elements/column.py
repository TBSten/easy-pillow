from typing import cast

from core.align import HorizontalAlign, VerticalAlign
from core.attributes import Attrs
from core.context import DrawContext
from core.elements import Element
from core.layout import Number
from core.node import DrawNode


class ColumnElement(Element):
    def __init__(
        self,
        vertical_align: VerticalAlign = VerticalAlign.TOP,
        horizontal_align: HorizontalAlign = HorizontalAlign.LEFT,
        vertical_gap: Number = 0,
        horizontal_gap: Number = 0,
        children: list[Element] = [],
        attrs: Attrs = [],
    ):
        super().__init__(attrs)
        self.children = children
        self.vertical_align = vertical_align
        self.horizontal_align = horizontal_align
        self.vertical_gap = vertical_gap
        self.horizontal_gap = horizontal_gap

    def on_layout(self, context: DrawContext) -> DrawNode:
        column_node = ColumnElement.Node(label="column_node")
        w = 0
        h = 0
        children: list[DrawNode] = []
        for child in self.children:
            child_node = child.layout(context)
            child_node.parent = column_node
            child_node_w = child_node.w = cast(
                int,
                child_node.w if child_node.w is not None else -1,
            )
            child_node_h = child_node.h
            if child_node_h is None:
                raise NotImplementedError(
                    f"invalid child_node height {child_node_h}"
                )

            child_node.y = h
            child_node.parent = column_node
            children.append(child_node)

            if w < child_node_w:
                w = child_node_w
            h += child_node_h
            h += self.vertical_gap
        h -= self.vertical_gap

        for child in children:
            if child.w == -1:
                child.w = w
            child_w = child.w
            if child_w is None:
                raise NotImplementedError(
                    f"invalid column child width {child_w}"
                )
            child.x = (w-child_w)*self.horizontal_align.value
        column_node.w = w
        column_node.h = h
        column_node.children = children
        return column_node

    class Node(DrawNode):
        def on_draw(self, context: DrawContext):
            self.draw_children(context)
