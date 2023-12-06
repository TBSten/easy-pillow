from enum import Enum


class Align:
    def __init__(self, value: float) -> None:
        self.value = value


class VerticalAlign(Align):
    def __init__(self, value) -> None:
        super().__init__(value)

    @classmethod
    def initialize_constants(cls):
        cls.TOP = cls(0.0)
        cls.CENTER = cls(0.5)
        cls.BOTTOM = cls(1.0)


VerticalAlign.initialize_constants()


class HorizontalAlign(Align):
    def __init__(self, value) -> None:
        super().__init__(value)

    @classmethod
    def initialize_constants(cls):
        cls.LEFT = cls(0.0)
        cls.CENTER = cls(0.5)
        cls.RIGHT = cls(1.0)


HorizontalAlign.initialize_constants()
