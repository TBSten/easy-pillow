from typing import Any

from PIL import Image, ImageDraw


class RenderLayer:
    def __init__(self, image: Image.Image) -> None:
        self._image = image


class RenderContext:
    def __init__(self, image:Image.Image) -> None:
        self.image:Image.Image = image
    @property
    def image_draw(self):
        return ImageDraw.Draw(self.image)
    def create_layer(self):
        base_image = self.image
        layer =  RenderLayer(base_image)
        self.image = Image.new("RGBA", base_image.size)
        return layer
    def alpha_composite_layer(self, layer:RenderLayer):
        self.image = Image.alpha_composite(layer._image, self.image)

