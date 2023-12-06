
from abc import ABCMeta, abstractmethod
from typing import cast

from PIL import Image

from attributes import Attrs, PaddingAttribute
from context import DrawContext
from node import DrawNode, DrawNodeType, Length, Parent, RootDrawNode


class Element(metaclass=ABCMeta):
    def __init__(self, attrs: Attrs = []):
        self.attrs = attrs

    def layout(self, context: DrawContext) -> DrawNode:
        node = self.on_layout(context)
        for attr in self.attrs:
            node = attr.layout(context, node)
        return node

    @abstractmethod
    def on_layout(self, context: DrawContext) -> DrawNode:
        pass


class Spacer(Element):
    def __init__(
        self,
        width=None,
        height=None,
        color=(255, 0, 0),
        attrs: Attrs = [],
    ):
        super().__init__(attrs=attrs)
        self.width = width
        self.height = height
        self.color = color

    def on_layout(self, context: DrawContext) -> DrawNode:
        return Spacer.Node(color=self.color, w=self.width, h=self.height)

    class Node(DrawNode):
        def __init__(
            self,
            color,
            parent: Parent = None,
            x: Length = None,
            y: Length = None,
            w: Length = None,
            h: Length = None,
            children: list[DrawNodeType] = [],
        ) -> None:
            super().__init__("spacer-element", parent, x, y, w, h, children)
            self.color = color

        def on_draw(self, context: DrawContext):
            context.img_draw.rectangle(self.to_tuple(), fill=self.color)


class ColumnElement(Element):
    def __init__(
        self,
        children: list[Element] = [],
        attrs: Attrs = [],
    ):
        super().__init__(attrs)
        self.children = children

    def on_layout(self, context: DrawContext) -> DrawNode:
        column_node = ColumnElement.Node(node_id="column_node")
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


class RowElement(Element):
    def __init__(
        self,
        children: list[Element] = [],
        attrs: Attrs = [],
    ):
        super().__init__(attrs)
        self.children = children

    def on_layout(self, context: DrawContext) -> DrawNode:
        row_node = RowElement.Node(node_id="row-element")
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
        print("row draw node", row_node)
        return row_node

    class Node(DrawNode):
        def on_draw(self, context: DrawContext):
            self.draw_children(context)
            context.img_draw.rectangle(
                self.to_tuple(),
                outline=(255, 0, 0),
                width=1,
            )


el = ColumnElement(
    children=[
        ColumnElement(
            children=[
                Spacer(width=100, height=100, color=(255, 0, 0, 128)),
            ],
        ),
        ColumnElement(
            children=[
                Spacer(width=200, height=200, color=(0, 255, 0, 128)),
                Spacer(width=200, height=200, color=(0, 255, 0, 128+64)),
                Spacer(width=200, height=200, color=(0, 255, 0, 255)),
            ],
        ),
        Spacer(width=300, height=300, color=(0, 0, 255, 128)),
        RowElement(
            attrs=[PaddingAttribute(top=100, bottom=100)],
            children=[
                Spacer(width=100, height=100, color=(0, 0, 0)),
                Spacer(width=100, height=200, color=(0, 0, 0, 128)),
                Spacer(width=100, height=100, color=(0, 0, 0)),
                Spacer(width=100, height=200, color=(0, 0, 0, 128)),
                Spacer(width=100, height=100, color=(0, 0, 0)),
                Spacer(width=100, height=200, color=(0, 0, 0, 128)),
                Spacer(width=100, height=100, color=(0, 0, 0)),
            ],
        ),
    ],
)

# layout
context = DrawContext(Image.new("RGBA", (0, 0)))
el_draw_node = RootDrawNode(node_id="root-node",root_node=el.layout(context))
el_draw_node.x = 0
el_draw_node.y = 0

w = el_draw_node.w
h = el_draw_node.h

if w is None or h is None:
    raise NotImplementedError(f"invalid root element size {w}*{h}")

# render
context = DrawContext(Image.new("RGBA", (int(w), int(h))))
context.img.alpha_composite(Image.open("./test.png").resize((int(w), int(h))))
el_draw_node.draw(context)
image = context.img

image.save("output.png")
