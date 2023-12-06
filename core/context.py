from PIL import Image, ImageDraw


class DrawContext:
    def __init__(self, img: Image.Image) -> None:
        self.img = img

    @property
    def img_draw(self) -> ImageDraw.ImageDraw:
        return ImageDraw.Draw(self.img)
