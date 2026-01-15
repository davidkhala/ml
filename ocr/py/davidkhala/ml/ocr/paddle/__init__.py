from pathlib import Path

from paddleocr import PaddleOCR


class Client:
    def __init__(self):
        self._ = PaddleOCR(use_doc_unwarping=True)

    def process(self, file: Path) -> list[dict] | dict:
        results = self._.predict(input=str(file))
        for result in results:
            print(result)
