

from PIL import Image

from core.context import DrawContext
from core.debug import print_node_tree
from core.elements import Element
from core.layout import LayoutConstraints
from core.node import RootDrawNode


def to_image(root_element: Element, debug:bool=False):
    # layout
    context = DrawContext(Image.new("RGBA", (0, 0)))
    el_draw_node = RootDrawNode(
        label="root-node",
        root_node=root_element.layout(context, LayoutConstraints.NONE),
    )
    el_draw_node.x = 0
    el_draw_node.y = 0

    w = el_draw_node.w
    h = el_draw_node.h

    if debug:
        print_node_tree(el_draw_node)

    if w is None or h is None:
        raise NotImplementedError(f"invalid root element size {w}*{h}")

    # render
    context = DrawContext(Image.new("RGBA", (int(w), int(h))))
    el_draw_node.draw(context)
    image = context.img

    return image
