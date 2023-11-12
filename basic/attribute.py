from typing import Callable

from PIL import Image, ImageColor, ImageFilter

from attribute import Attribute
from color import Color
from context import RenderContext
from layout import Offset, Size


class PaddingAttribute(Attribute):
    def __init__(
            self,
            top: int,
            left: int,
            right: int,
            bottom: int,
    ) -> None:
        super().__init__()
        self._top = top
        self._left = left
        self._right = right
        self._bottom = bottom

    def measure_size(self, offset: Offset, size: Size) -> tuple[Offset, Size]:
        offset = (self._left + offset[0], self._right + offset[1])
        size = (self._left + size[0] + self._right, self._top + size[1] + self._bottom)
        return (offset, size)

    def draw(
            self, 
            context: RenderContext, 
            offset: Offset, 
            size: Size, 
            draw_content: Callable[[RenderContext, Offset, Size], None],
        ) -> None:
        draw_content(
            context,
            (self._left + offset[0], self._top + offset[1]),
            (size[0]-self._left-self._right, size[1]-self._top-self._bottom),
        )

    @staticmethod
    def all(value: int):
        return PaddingAttribute(
            top=value,
            left=value,
            right=value,
            bottom=value,
        )
    @staticmethod
    def vertical(value: int):
        return PaddingAttribute(
            top=value,
            bottom=value,
            left=0,
            right=0,
        )
    @staticmethod
    def horizontal(value: int):
        return PaddingAttribute(
            top=0,
            bottom=0,
            left=value,
            right=value,
        )


class BackgroundColorAttribute(Attribute):
    def __init__(self, color: Color, radius: int=0) -> None:
        super().__init__()
        self._color = color
        self._radius = radius
    def draw(
            self, 
            context: RenderContext, 
            offset: Offset, 
            size: Size, 
            draw_content: Callable[[RenderContext, Offset, Size], None],
        ) -> None:
        rect = (offset[0],offset[1],offset[0]+size[0],offset[1]+size[1])
        context.image_draw.rounded_rectangle(
            rect, 
            radius=self._radius,
            fill=self._color,
        )
        layer = context.create_layer()
        draw_content(context, offset, size)
        context.alpha_composite_layer(layer)


class BlurAttribute(Attribute):
    def __init__(self, radius: float) -> None:
        super().__init__()
        self._radius = radius
    def draw(self, context: RenderContext, offset: Offset, size: Size, draw_content: Callable[[RenderContext, Offset, Size], None]):
        layer = context.create_layer()
        draw_content(context, offset, size)
        context.image = context.image.filter(ImageFilter.BoxBlur(self._radius))
        context.alpha_composite_layer(layer)

class _EasyPillowAttribute:
    padding = PaddingAttribute
    backgroundColor = BackgroundColorAttribute
    bgColor = BackgroundColorAttribute
    blur = BlurAttribute


a = _EasyPillowAttribute
