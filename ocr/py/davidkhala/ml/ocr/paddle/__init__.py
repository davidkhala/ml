from pathlib import Path
from typing import Literal

from davidkhala.utils.syntax.path import home_resolve, delete


class Client:

    def init(self, type: Literal['all', 'focus']):

        from paddleocr import PaddleOCR
        self.all = PaddleOCR(use_doc_unwarping=True)

    @staticmethod
    def clean():
        """clean up downloaded models on local disk"""
        delete(home_resolve('.paddlex', 'official_models'))

    def process(self, file: Path) -> list[dict] | dict:
        results = self.all.predict(str(file))
        assert len(results) == 1
        return results[0]['rec_texts']
