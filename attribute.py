from typing import Callable, TypeAlias

from context import RenderContext
from layout import Offset, Size

AttributeLike :TypeAlias = "Attribute | list[Attribute]"

class Attribute:
    def measure_size(self, offset: Offset, size: Size) -> tuple[Offset, Size]:
        return (offset, size)
    def draw(
            self, 
            context: RenderContext, 
            offset: Offset, 
            size: Size, 
            draw_content: Callable[[RenderContext, Offset, Size], None],
        ):
        draw_content(context, offset, size)

def to_attributes(attr_likes: AttributeLike) -> list[Attribute]:
    if isinstance(attr_likes, Attribute):
        return [attr_likes]
    return attr_likes
