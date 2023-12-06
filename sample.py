
import sys

from attributes.background import BackgroundAttribute
from attributes.border import BorderAttribute
from attributes.size import WidthAttribute, size
from core.align import HorizontalAlign
from core.color import Color
from core.elements import Element
from core.image import to_image
from elements.column import ColumnElement
from elements.row import RowElement
from elements.spacer import Spacer

GREEN = Color(0, 255, 0)
RED = Color(255, 0, 0, 128)
BLUE = Color(0, 0, 255)
BLACK = Color.BLACK
WHITE = Color.WHITE


def test1():
    spacers: list[Element] = [
        Spacer(attrs=[
            BackgroundAttribute(RED.copy(a=255*0.5)),
            size(30, 30),
        ]),
        Spacer(attrs=[
            BackgroundAttribute(RED.copy(a=255*0.25)),
            size(30, 30),
        ]),
        Spacer(attrs=[
            BackgroundAttribute(RED.copy(a=255*0.125)),
            size(30, 30),
        ]),
    ]
    row_sample = RowElement(
        horizontal_gap=10,
        horizontal_align=HorizontalAlign.CENTER,
        attrs=[BorderAttribute(45, WHITE), WidthAttribute(50)],
        children=spacers,
    )
    col_sample = ColumnElement(
        vertical_gap=10,
        attrs=[BorderAttribute(1, WHITE)],
        children=spacers,
    )
    img = to_image(
        ColumnElement(
            vertical_gap=10,
            children=[
                RowElement(
                    children=[row_sample, col_sample],
                    horizontal_gap=10,
                ),
                RowElement(
                    children=[col_sample, row_sample],
                    horizontal_gap=10,
                ),
            ],
        )
    )
    img.save("./output/test1.png")


test1()
