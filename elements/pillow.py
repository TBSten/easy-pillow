
from core.attributes import Attrs
from core.context import DrawContext
from core.elements import Element
from PIL import Image

from core.layout import LayoutConstraints
from core.node import DrawNode, DrawNodeType, Parent
from core.unit import Length

class PillowImageElement(Element):
  def __init__(
      self, 
      img: Image.Image,
      attrs: Attrs = [],
  ):
    super().__init__(attrs)
    self.img = img

  def on_layout(self, context: DrawContext, constraints: LayoutConstraints) -> DrawNode:
    return PillowImageElement.Node(
      img = self.img,
      label="",
    )
  
  class Node(DrawNode):
    def __init__(self, label,img: Image.Image, parent: Parent = None, x: Length = None, y: Length = None) -> None:
      super().__init__(
        label, 
        parent, 
        x, y, 
        w=img.width, h=img.height, 
        children=[],
      )
      self.img = img
    def on_draw(self, context: DrawContext):
      context.img.alpha_composite(
        self.img, 
        dest=(int(self.absolute_x), int(self.absolute_y)),
      )
