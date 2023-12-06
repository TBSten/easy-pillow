from typing import TypeAlias

_RGB: TypeAlias = tuple[int, int, int] | tuple[int, int, int, int]


class Color:
    def __init__(
        self,
        r: float | int,
        g: float | int,
        b: float | int,
        a: float | int = 255,
    ) -> None:
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def copy(
        self,
        r: float | int | None = None,
        g: float | int | None = None,
        b: float | int | None = None,
        a: float | int | None = None,
    ):
        return Color(
            r=r if r is not None else self.r,
            g=g if g is not None else self.g,
            b=b if b is not None else self.b,
            a=a if a is not None else self.a,
        )

    def to_tuple(self):
        return (int(self.r), int(self.g), int(self.b), int(self.a))

    def __str__(self) -> str:
        return f"Color({self.r},{self.g},{self.b},{self.a})"

    @classmethod
    def initialize_constants(cls):
        cls.TRANSPARENT = Color(0, 0, 0, 0)
        cls.BLACK = Color(0, 0, 0)
        cls.WHITE = Color(255, 255, 255)
        cls.RED = Color(255, 0, 0)
        cls.GREEN = Color(0, 255, 0)
        cls.BLUE = Color(0, 0, 255)


Color.initialize_constants()
