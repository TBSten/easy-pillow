
from attributes.padding import PaddingAttribute
from core.image import to_image
from elements.column import ColumnElement
from elements.row import RowElement
from elements.spacer import Spacer

image = to_image(
    ColumnElement(
        children=[
            ColumnElement(
                children=[
                    Spacer(width=100, height=100, color=(255, 0, 0, 128)),
                ],
            ),
            ColumnElement(
                children=[
                    Spacer(width=200, height=200, color=(0, 255, 0, 128)),
                    Spacer(width=200, height=200, color=(0, 255, 0, 128+64)),
                    Spacer(width=200, height=200, color=(0, 255, 0, 255)),
                ],
            ),
            Spacer(width=300, height=300, color=(0, 0, 255, 128)),
            RowElement(
                attrs=[PaddingAttribute(top=100, bottom=100)],
                children=[
                    Spacer(width=100, height=100, color=(0, 0, 0)),
                    Spacer(width=100, height=200, color=(0, 0, 0, 128)),
                    Spacer(width=100, height=100, color=(0, 0, 0)),
                    Spacer(width=100, height=200, color=(0, 0, 0, 128)),
                    Spacer(width=100, height=100, color=(0, 0, 0)),
                    Spacer(width=100, height=200, color=(0, 0, 0, 128)),
                    Spacer(width=100, height=100, color=(0, 0, 0)),
                ],
            ),
        ],
    ),
)
image.save("./output.png")
