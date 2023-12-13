from typing import cast

from core.align import HorizontalAlign, VerticalAlign
from core.attributes import Attrs
from core.context import DrawContext
from core.elements import Element
from core.layout import LayoutConstraints
from core.node import DrawNode
from core.unit import Number


class BoxElement(Element):
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
        box_node = BoxElement.Node(label="box_node")

        content_w = 0
        content_h = 0
        children: list[DrawNode] = []
        for child in self.children:
            child_node = child.layout(context, LayoutConstraints.NONE)
            child_node.parent = box_node

            children.append(child_node)

            # contents size の更新
            child_node_w = child_node.w
            content_w = child_node.w if child_node_w is not None and content_w < child_node_w else content_w
            child_node_h = child_node.h
            content_h = child_node.h if child_node_h is not None and content_h < child_node_h else content_h

        box_node.w = constraints.get_width_with_constraints(content_w)
        box_node.h = constraints.get_height_with_constraints(content_h)

        for child_node in children:
            # 大きさがNoneの場合 幅いっぱいに伸ばす
            if child_node.w is None:
                child_node.w = box_node.w
            if child_node.h is None:
                child_node.h = box_node.h
            # self.horizontal_align, self.vertical_align を適用
            child_node.x = (box_node.w - child_node.w) * \
                self.horizontal_align.value
            child_node.y = (box_node.h - child_node.h) * \
                self.vertical_align.value

        box_node.children = children
        return box_node

    class Node(DrawNode):
        def on_draw(self, context: DrawContext):
            self.draw_children(context)
