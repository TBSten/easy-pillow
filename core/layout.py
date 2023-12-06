
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
