

from context import DrawContext
from elements import Element
from node import RootDrawNode
from PIL import Image

def to_image(root_element: Element):
    # layout
    context = DrawContext(Image.new("RGBA", (0, 0)))
    el_draw_node = RootDrawNode(label="root-node", root_node=root_element.layout(context))
    el_draw_node.x = 0
    el_draw_node.y = 0

    w = el_draw_node.w
    h = el_draw_node.h

    if w is None or h is None:
        raise NotImplementedError(f"invalid root element size {w}*{h}")

    # render
    context = DrawContext(Image.new("RGBA", (int(w), int(h))))
    el_draw_node.draw(context)
    image = context.img

    return image

