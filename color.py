from typing import TypeAlias

_RGB: TypeAlias = tuple[int, int, int] | tuple[int, int, int, int]
Color: TypeAlias = str | int | _RGB
