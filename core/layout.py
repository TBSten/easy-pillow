
from core.unit import Length, Number


def number_to_int(num: Number):
    return int(num)


class Offset:
    def __init__(self, x: Number, y: Number) -> None:
        self._x = x
        self._y = y

    @property
    def x(self):
        return number_to_int(self._x)

    @x.setter
    def x(self, value: Number):
        self._x = value

    @property
    def y(self):
        return number_to_int(self._y)

    @y.setter
    def y(self, value: Number):
        self._y = value


class Size:
    def __init__(self, w: Number, h: Number) -> None:
        self._w = w
        self._h = h

    @property
    def w(self):
        return number_to_int(self._w)

    @w.setter
    def w(self, value: Number):
        self._w = value

    @property
    def h(self):
        return number_to_int(self._h)

    @h.setter
    def h(self, value: Number):
        self._h = value


class Rect:
    def __init__(self, offset: Offset, size: Size) -> None:
        self._offset = offset
        self._size = size

    @property
    def x(self):
        return number_to_int(self._offset.x)

    @x.setter
    def x(self, value: Number):
        self._offset.x = value

    @property
    def y(self):
        return number_to_int(self._offset.y)

    @y.setter
    def y(self, value: Number):
        self._offset.y = value

    @property
    def w(self):
        return number_to_int(self._size.w)

    @w.setter
    def w(self, value: Number):
        self._size.w = value

    @property
    def h(self):
        return number_to_int(self._size.h)

    @h.setter
    def h(self, value: Number):
        self._size.h = value

    def to_tuple(self):
        return (self.x, self.y, self.x+self.w, self.y+self.h)

    def __str__(self) -> str:
        return f"Rect({self.x},{self.y},{self.w},{self.h})"


class LayoutConstraints:
    def __init__(
        self,
        min_w: Length = None,
        max_w: Length = None,
        min_h: Length = None,
        max_h: Length = None,
    ) -> None:
        self.max_w = max_w
        self.min_w = min_w
        self.max_h = max_h
        self.min_h = min_h

    def get_width_with_constraints(self, width: Length):
        if width is None:
            if self.max_w == self.min_w:
                return self.max_w
            else:
                return None
        # min_w以下だったらmin_wを返す
        if self.min_w is not None and width < self.min_w:
            return self.min_w
        # max_w以上だったらmax_wを返す
        if self.max_w is not None and self.max_w < width:
            return self.max_w
        return width

    def get_height_with_constraints(self, height: Length):
        if height is None:
            if self.max_h == self.min_h:
                return self.max_h
            else:
                return None
        # min_h以下だったらmin_hを返す
        if self.min_h is not None and height < self.min_h:
            return self.min_h
        # max_h以上だったらmax_hを返す
        if self.max_h is not None and self.max_h < height:
            return self.max_h
        return height

    def get_size_with_constraints(self, width: Length, height: Length):
        return (self.get_width_with_constraints(width), self.get_height_with_constraints(height))

    def __str__(self) -> str:
        return f"LayoutConstraints(min_w={self.min_w},max_w={self.max_w},min_h={self.min_h},max_h={self.max_h})"

    def copy(
        self,
        min_w: Length = None,
        max_w: Length = None,
        min_h: Length = None,
        max_h: Length = None,
    ):
        con = LayoutConstraints(
            min_w=min_w if min_w is not None else self.min_w,
            max_w=max_w if max_w is not None else self.max_w,
            min_h=min_h if min_h is not None else self.min_h,
            max_h=max_h if max_h is not None else self.max_h,
        )
        return con

    @classmethod
    def init_constants(cls):
        cls.NONE = LayoutConstraints(
            min_w=None, max_w=None,
            min_h=None, max_h=None,
        )


LayoutConstraints.init_constants()
