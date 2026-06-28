from os import PathLike

from presidio_image_redactor import ImageRedactorEngine
from PIL import Image

class Client:
    def __init__(self):
        self._ = ImageRedactorEngine()
    def redact(self, path: PathLike):
        return self._.redact(image=Image.open(path))