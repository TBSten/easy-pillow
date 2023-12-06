from abc import ABCMeta, abstractmethod
from typing import TypeAlias

from PIL import Image

from core.context import DrawContext
from core.layout import Number

Length: TypeAlias = "Number|None"

DrawNodeType: TypeAlias = "DrawNode"
Parent: TypeAlias = "DrawNode|None"


class DrawNode(metaclass=ABCMeta):
    def __init__(
        self,
        label,
        parent: Parent = None,
        x: Length = None, y: Length = None,
        w: Length = None, h: Length = None,
        children: list[DrawNodeType] = [],
    ) -> None:
        self.parent = parent
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.children = children
        self.label = label

    @property
    def absolute_x(self):
        if self.parent is None:
            print("❌ invaild parent")
            print(self.label, self.parent)
            raise NotImplementedError("❌ invalid parent")
        elif self.parent.absolute_x is None:
            print("❌ invaild parent absolute_x")
            print(self.label, self.parent, self.parent.absolute_x)
            raise NotImplementedError("❌ invalid parent")
        return self.parent.absolute_x + self.x

    @property
    def absolute_y(self):
        if self.parent is None:
            print("❌ invaild parent")
            print(self.label, self.parent)
            raise NotImplementedError("❌ invalid parent")
        elif self.parent.absolute_y is None:
            print("❌ invaild parent absolute_y")
            print(self.label, self.parent, self.parent.absolute_y)
            raise NotImplementedError("❌ invalid parent absolute_y")
        return self.parent.absolute_y + self.y

    def __str__(self) -> str:
        children_str = f",children=[{','.join([str(child) for child in self.children])}]" if \
            len(self.children) >= 1 \
            else ""
        return f"DrawNode(label={self.label},x={self.x},y={self.y},w={self.w},h={self.h}{children_str},parent_id={self.parent.label if self.parent is not None else 'None'})"

    def draw(self, context: DrawContext):
        base_img = context.img
        context.img = Image.new("RGBA", base_img.size)
        self.on_draw(context)
        context.img = Image.alpha_composite(base_img, context.img)

    def draw_children(self, context: DrawContext):
        for child in self.children:
            child.draw(context)

    @abstractmethod
    def on_draw(self, context: DrawContext):
        pass

    def to_tuple(self):
        x = self.absolute_x
        if x is None:
            raise NotImplementedError(f"invalid x {x}")
        y = self.absolute_y
        if y is None:
            raise NotImplementedError(f"invalid y {y}")
        w = self.w
        if w is None:
            raise NotImplementedError(f"invalid w {w}")
        h = self.h
        if h is None:
            raise NotImplementedError(f"invalid h {h}")
        return (x, y, x+w, y+h)


class RootDrawNode(DrawNode):
    def __init__(
        self,
        label,
        root_node: DrawNodeType,
    ) -> None:
        super().__init__(
            label=label,
            parent=None,
            x=0,
            y=0,
            w=root_node.w, h=root_node.h,
            children=[root_node],
        )
        root_node.x = 0
        root_node.y = 0
        root_node.parent = self

    @property
    def absolute_x(self):
        return 0

    @property
    def absolute_y(self):
        return 0

    def on_draw(self, context: DrawContext):
        self.draw_children(context)
