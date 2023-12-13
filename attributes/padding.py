from PIL import Image

from core.attributes import Attribute
from core.context import DrawContext
from core.layout import LayoutConstraints
from core.node import DrawNode
from core.unit import Number


class PaddingAttribute(Attribute):
    def __init__(self, left: Number = 0, top: Number = 0, right: Number = 0, bottom: Number = 0):
        super().__init__()
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom

    def set_constraints(self, context: DrawContext, constraints: LayoutConstraints) -> LayoutConstraints:
        con = constraints.copy(
            min_w=constraints.min_w - self.left -
            self.right if constraints.min_w is not None else None,
            min_h=constraints.min_h - self.top -
            self.bottom if constraints.min_h is not None else None,
            max_w=constraints.max_w - self.left -
            self.right if constraints.max_w is not None else None,
            max_h=constraints.max_h - self.top -
            self.bottom if constraints.max_h is not None else None,
        )
        return con

    def on_layout(self, context: DrawContext, constraints: LayoutConstraints, target: DrawNode):
        left = self.left
        top = self.top
        right = self.right
        bottom = self.bottom

        target_w = target.w
        if target_w is not None:
            target.w = target_w + (left + right)

        target_h = target.h
        if target_h is not None:
            target.h = target_h + (top + bottom)

    def on_draw(self, context: DrawContext, target: DrawNode):
        print("padding", self.left, self.top, self.right, self.bottom)
        base = context.img
        target_w = target.w
        target_h = target.h
        if target_w is None:
            raise NotImplementedError(f"invalid w {target_w}")
        if target_h is None:
            raise NotImplementedError(f"invalid h {target_h}")

        # context.img = Image.new("RGBA", context.img.size)
        # target.w = target_w - self.left - self.right
        # target.h = target_h - self.top - self.bottom

        # # 元に戻す
        # base.alpha_composite(context.img, dest=(int(self.left), int(self.top)))
        # context.img = base
        # target.w = target_w
        # target.h = target_h
