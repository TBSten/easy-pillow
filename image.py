
from PIL import Image

from basic.element import p
from context import RenderContext
from element import Element


def to_image(top: Element):
    root = p.root(top)

    image = Image.new("RGBA", (0,0))
    context = RenderContext(image)

    # measure root size
    root_size = root.measure_size(context, offset=(0,0))
    print("root size", root_size)

    # draw root
    output_image = Image.new("RGBA", root_size)
    context = RenderContext(output_image)
    root.draw_root(context)

    return context.image
