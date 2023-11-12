from typing import Union

from PIL import Image, ImageFont

from attribute import Attribute, AttributeLike, to_attributes
from basic.attribute import a
from color import Color
from context import RenderContext
from element import Element, ElementType
from layout import Offset, Size


class RootElement(Element):
    def __init__(self, top:Element) -> None:
        super().__init__()
        self.name = "Root"
        self.append_child_element(top)
    def measure_content_size(self, context:RenderContext, offset:Offset) -> Size:
        return self._top.measure_size(context, offset)
    def on_draw(self, context:RenderContext, offset: Offset, size: Size):
        self._top.draw(context, offset)
    def draw_root(self, context:RenderContext):
        self.draw(context, (0, 0))
    @property
    def _top(self):
        return self._child_elements[0]

class ColumnElement(Element):
    def __init__(self, attrs: AttributeLike=[], elements: list[Element]=[]) -> None:
        super().__init__(*to_attributes(attrs), *elements)
        self.name = "Column"
    def measure_content_size(self, context:RenderContext, offset: Offset) -> Size:
        w = 0
        h = 0
        for child in self._child_elements:
            child_x = offset[0]
            child_y = offset[1] + h
            child_w, child_h = child.measure_size(context, (child_x,child_y))
            w = child_w if w <= child_w else w
            h += child_h
        return (w, h)
    def on_draw(self, context: RenderContext, offset: Offset, size: Size):
        y = 0
        for child in self._child_elements:
            child_x = offset[0]
            child_y = offset[1] + y
            child_w, child_h = child.measure_size(context, (child_x, child_y))
            child.draw(context, (child_x, child_y))
            y += child_h

class RowElement(Element):
    def __init__(self, attrs: AttributeLike=[], elements: list[Element]=[]) -> None:
        super().__init__(*to_attributes(attrs), *elements)
        self.name = "Row"
    def measure_content_size(self, context:RenderContext, offset: Offset) -> Size:
        w = 0
        h = 0
        for child in self._child_elements:
            child_x = offset[0] + w
            child_y = offset[1]
            child_w, child_h = child.measure_size(context, (child_x,child_y))
            w += child_w
            h = child_h if h <= child_h else h
        return (w, h)
    def on_draw(self, context: RenderContext, offset: Offset, size: Size):
        x = 0
        for child in self._child_elements:
            child_x = offset[0] + x
            child_y = offset[1]
            child_w, child_h = child.measure_size(context, (child_x, child_y))
            child.draw(context, (child_x, child_y))
            x += child_w

class TextElement(Element):
    def __init__(self, text:str, color: Color=(0,0,0), attrs: AttributeLike = []) -> None:
        super().__init__(*to_attributes(attrs))
        self.name = "Text"
        self._text = text
        self._font = ImageFont.truetype("./fonts/MPLUS1p-Regular.ttf", size=24)
        self._color = color
    def __str__(self) -> str:
        return f"Text('{self._text}')"
    def measure_content_size(self, context:RenderContext, offset: Offset) -> Size:
        left, top, right, bottom = context.image_draw.textbbox(
            offset, 
            self._text, 
            font=self._font,
        )
        return right-offset[0], bottom-offset[1]
    def on_draw(self, context: RenderContext, offset: Offset, size: Size):
        context.image_draw.text(
            offset, 
            self._text, 
            font=self._font,
            fill=self._color,
        )

class ImageElement(Element):
    def __init__(self, src:str, attrs: AttributeLike=[]) -> None:
        super().__init__(*to_attributes(attrs))
        self.name = "Image"
        self._src = src
    def __str__(self) -> str:
        return f"Image('{self._src}')"
    def measure_content_size(self, context: RenderContext, offset:Offset) -> Size:
        img = self._image # todo cache
        return (img.width,img.height)
    def on_draw(self, context: RenderContext, offset: Offset, size: Size):
        layer = context.create_layer()
        context.image.paste(self._image, offset)
        context.alpha_composite_layer(layer)
    @property
    def _image(self)->Image.Image:
        return Image.open(self._src).convert("RGBA")

def spacer(size: int, attr: AttributeLike=[]):
    return ColumnElement(
        attrs=[
            a.padding(size, 0, 0, 0),
            *to_attributes(attr),
        ],
    )

class _EasyPillowElements:
    def __init__(self) -> None:
        self.img = ImageElement
        self.image = ImageElement
        self.text = TextElement
        self.root = RootElement
        self.column = ColumnElement
        self.spacer = spacer
        self.row = RowElement


p = _EasyPillowElements()
