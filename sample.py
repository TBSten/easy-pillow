from PIL import Image

from attributes.background import BackgroundAttribute
from attributes.border import BorderAttribute
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
        BorderAttribute(1, WHITE),
        BackgroundAttribute(Color.RED.copy(a=128)),
        size(100,100),
    ])
    img = BoxElement(
        horizontal_align=HorizontalAlign.CENTER,
        vertical_align=VerticalAlign.CENTER,
        attrs=[HeightAttribute(300), BackgroundAttribute(Color.WHITE)],
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

    to_image(img,debug=True).save("./output/test1.png")


test1()
