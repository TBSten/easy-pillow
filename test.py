from basic.attribute import a
from basic.element import p
from element import Element
from image import to_image


def section(elements:list[Element]):
    return p.column(
        attrs=[
            a.padding.horizontal(100),
            a.bgColor((255, 255, 255, 255), radius=20),
            a.padding.all(20),
        ],
        elements=elements,
    )

text_section = section(
    elements=[
        p.text("テキスト", (0,0,0,100)),
        p.text("easy pillow"),
        p.text("日本語もいける"),
        p.text("絵文字は未対応...😭"),
    ],
)

image_section = section(
    elements=[
        p.text("画像", (0,0,0,100)),
        p.img("./test.png"),
    ],
)

blur_section = section(
    elements=[
        p.text("ぼかし", (0,0,0,100)),
        p.img("./test.png", attrs=[a.blur(3)]),
    ],
)

background_section = section(
    elements=[
        p.text("背景色", (0,0,0,100)),
        p.text(
            text="margin and padding", 
            attrs=[
                a.padding.all(20), # margin
                a.bgColor((255, 0, 0)),
                a.padding.all(10), # padding
            ],
        ),
        p.text(
            text="rounded", 
            attrs=[
                a.bgColor((255, 0, 0), 10),
                a.padding.vertical(5),
                a.padding.horizontal(20),
            ],
        ),
    ],
)

image = to_image(
    p.column(
        attrs=[
            a.bgColor((200, 255, 200)),
            a.padding.all(50),
        ],
        elements=[
            text_section,
            p.spacer(10),
            image_section,
            p.spacer(10),
            blur_section,
            p.spacer(10),
            background_section,
        ],
    )
)

image.save("output.png", save_all=True)
