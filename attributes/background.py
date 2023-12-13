from core.attributes import Attribute
from core.color import Color
from core.context import DrawContext
from core.layout import LayoutConstraints
from core.node import DrawNode, DrawNodeType, Length, Parent


class BackgroundAttribute(Attribute):
    def __init__(self, color: Color = Color.TRANSPARENT):
        super().__init__()
        self.color = color

    def on_layout(self, context: DrawContext, constraints: LayoutConstraints, target: DrawNode):
        pass

    def on_draw(self, context: DrawContext, target: DrawNode):
        rect = target.to_tuple()
        print("draw bg", rect)
        if all([
            target.w is not None and target.w >= 2,
            target.h is not None and target.h >= 2,
        ]):
            context.img_draw.rectangle(
                (rect[0], rect[1], rect[2]-1, rect[3]-1), fill=self.color.to_tuple(),
            )
