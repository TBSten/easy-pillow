
from attributes.background import BackgroundAttribute
from attributes.border import BorderAttribute
from attributes.size import HeightAttribute, WidthAttribute, size
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
    row_sample = RowElement(
        horizontal_gap=10,
        horizontal_align=HorizontalAlign.CENTER,
        attrs=[
            BackgroundAttribute(Color.BLUE.copy(a=16)),
            BorderAttribute(2, WHITE),
            WidthAttribute(200),
            HeightAttribute(100),
        ],
        children=[
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
        ],
    )
    col_sample = ColumnElement(
        vertical_gap=10,
        attrs=[BorderAttribute(1, WHITE)],
        children=[
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
        ],
    )
    img = ColumnElement(children=[
        RowElement(children=[
            row_sample, col_sample,
        ]),
        RowElement(children=[
            col_sample, row_sample, 
        ]),
    ])

    # red = Spacer([
    #     BorderAttribute(1, WHITE),
    #     BackgroundAttribute(Color.RED.copy(a=128)),
    #     # WidthAttribute(200),
    #     # HeightAttribute(100),
    #     size(200,100),
    # ])
    # img = ColumnElement(children=[
    #     RowElement(children=[
    #         ColumnElement(children=[red]),
    #         RowElement(children=[red,red]),
    #         ColumnElement(children=[red]),
    #         RowElement(children=[red]),
    #         ColumnElement(children=[red,red]),
    #     ]),
    #     RowElement(children=[
    #         RowElement(children=[red]),
    #         ColumnElement(children=[red]),
    #         RowElement(children=[red]),
    #         ColumnElement(children=[red]),
    #     ]),
    # ])

    to_image(img,debug=True).save("./output/test1.png")


test1()
