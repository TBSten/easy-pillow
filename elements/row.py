from typing import cast

from core.align import HorizontalAlign, VerticalAlign
from core.attributes import Attrs
from core.context import DrawContext
from core.elements import Element
from core.layout import LayoutConstraints
from core.node import DrawNode
from core.unit import Number


class RowElement(Element):
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

    def on_layout(self, context: DrawContext, constraints: LayoutConstraints) -> DrawNode:
        row_node = RowElement.Node(label="row-element")
        w = 0
        h = 0
        children: list[DrawNode] = []
        for child in self.children:
            child_node = child.layout(context, constraints)
            child_node.parent = row_node
            child_node.h = child_node_h = cast(
                int,
                child_node.h if child_node.h is not None else -1,
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
            w += self.horizontal_gap
        w -= self.horizontal_gap

        for child in children:
            if child.w == -1:
                child.w = w
            child_h = child.h
            if child_h is None:
                raise NotImplementedError(
                    f"invalid column child height {child_h}"
                )
            child.y = (h-child_h)*self.vertical_align.value
        row_node.w = w
        row_node.h = h
        row_node.children = children
        return row_node

    class Node(DrawNode):
        def on_draw(self, context: DrawContext):
            self.draw_children(context)
