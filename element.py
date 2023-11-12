from typing import TypeAlias, Union
from uuid import uuid4

from attribute import Attribute
from context import RenderContext
from layout import Offset, Size

ElementType:TypeAlias = "Element"

class Element:
    def __init__(self, *nodes: Union[Attribute, ElementType]) -> None:
        self._id = uuid4().hex
        self.parent:ElementType|None = None
        self.name = "Node"
        self._attributes, self._child_elements = split_attribute_elements(*nodes)
    def append_child_element(self, child:ElementType):
        if child.parent is not None:
            raise ValueError("can not append child multi element")
        child.parent = child
        self._child_elements.append(child)
    def append_child_elements(self, *children:ElementType):
        for child in children:
            self.append_child_element(child)
    def __str__(self) -> str:
        s = f"{self.name}"
        if len(self._child_elements):
            s += f"({','.join([str(child) for child in self._child_elements])})"
        return s
    def measure_size(self, context:RenderContext, offset: Offset) -> Size:
        size = self.measure_content_size(context, offset)
        for attr in self._attributes:
            offset, size = attr.measure_size(offset, size)
        return size
    def measure_content_size(self, context:RenderContext, offset: Offset) -> Size:
        raise NotImplementedError("can not measure_size", self.name)
    def draw(self, context:RenderContext, offset: Offset):
        size = self.measure_size(context, offset)
        # self._attributes の適用
        self._draw_chain(0, context, offset, size)
    def on_draw(self, context:RenderContext, offset: Offset, size: Size):
        raise NotImplementedError(f"can not draw {self.name}")
    def _debug_draw(self, context:RenderContext, offset:Offset):
        size = self.measure_size(context, offset)
        debug_color = (255,255,255)
        left = offset[0]
        top = offset[1]
        right =  offset[0] + size[0] -1
        bottom =  offset[1] + size[1] -1
        bound = (
            (min(left, right), min(top, bottom)),
            (max(left, right), max(top, bottom)),
        )
        context.image_draw.rectangle(bound, fill=None, outline=debug_color)
        context.image_draw.text(offset, self.name)
    # 1st attribute, 2st attribute, ..., last attribute, self.on_draw()と描画する。
    def _draw_chain(self, idx: int, context:RenderContext, offset: Offset, size: Size):
        if idx < len(self._attributes):
            self._attributes[idx].draw(
                context, offset, size,
                lambda context, offset, size: self._draw_chain(idx+1, context, offset, size)
            )
        else:
            self.on_draw(context, offset, size)


def split_attribute_elements(*nodes:Union[Element, Attribute]):
    attrs:list[Attribute] = []
    els:list[Element] = []

    for node in nodes:
        if isinstance(node, Element):
            els.append(node)
        elif isinstance(node, Attribute):
            attrs.append(node)
    return attrs, els
