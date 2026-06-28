from os import PathLike

from presidio_image_redactor import ImageRedactorEngine
from PIL import Image


class Client:
    def __init__(self):
        self._ = ImageRedactorEngine()

    def redact(self, _in: PathLike, _out: PathLike):
        with Image.open(_in) as image:
            redacted = self._.redact(image)

        redacted.save(_out)
        redacted.close()
