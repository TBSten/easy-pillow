from PIL import Image

from attributes.background import BackgroundAttribute
from attributes.border import BorderAttribute
from attributes.padding import PaddingAttribute
from attributes.size import HeightAttribute, WidthAttribute, size
from core.align import HorizontalAlign, VerticalAlign
from core.color import Color
from core.elements import Element
from core.image import to_image
from elements.box import BoxElement
from elements.column import ColumnElement
from elements.pillow import PillowImageElement
from elements.row import RowElement
from elements.spacer import Spacer

GREEN = Color(0, 255, 0)
RED = Color(255, 0, 0, 128)
BLUE = Color(0, 0, 255)
BLACK = Color.BLACK
WHITE = Color.WHITE


def test1():
    red = Spacer([
        size(100, 100),
        BorderAttribute(10, BLUE),
        BackgroundAttribute(Color.RED.copy(a=128)),
        # BackgroundAttribute(Color.RED.copy(a=128)),
    ])
    img = ColumnElement(
        horizontal_align=HorizontalAlign.CENTER,
        vertical_align=VerticalAlign.CENTER,
        attrs=[
            # HeightAttribute(300),
            BackgroundAttribute(Color.WHITE),
        ],
        children=[
            PillowImageElement(
                Image.open("./input/placeholder.png")
                .resize((int(300/2), int(200/2)))
            ),
            red,
            red,
            red,
        ],
    )

    # img = BoxElement(
    #     attrs=[
    #         BorderAttribute(100, BLUE),
    #         PaddingAttribute(10, 10, 10, 10),
    #         BackgroundAttribute(RED),
    #         size(50,50),
    #     ],
    #     children=[
    #     ],
    # )

    # img = RowElement(
    #     attrs=[
    #         BackgroundAttribute(WHITE),
    #         PaddingAttribute(100,100,100,100),
    #         BorderAttribute(3, WHITE),
    #         BackgroundAttribute(RED),
    #         PaddingAttribute(10,10,10,10),
    #         size(200,100),
    #     ],
    #     children=[
    #         Spacer(attrs=[
    #             BackgroundAttribute(Color(128,255,128)),
    #             size(100,100),
    #         ])
    #     ],
    # )

    to_image(img, debug=True).save("./output/test1.png")


test1()
