from pathlib import Path
from typing import Literal

from davidkhala.utils.syntax.path import home_resolve, delete


class Client:

    def init(self, type: Literal['all', 'focus']):
        match type:
            case 'all':
                from paddleocr import PaddleOCR
                self.all = PaddleOCR(use_doc_unwarping=True)
            case 'focus':
                from paddleocr import PPStructureV3
                self.focus = PPStructureV3(use_doc_unwarping=True)

    @staticmethod
    def clean():
        """clean up downloaded models on local disk"""
        delete(home_resolve('.paddlex', 'official_models'))

    def process(self, file: Path, schema) -> list[dict] | dict:
        _input = str(file)
        if schema:
            results = self.focus.predict(_input)
        else:
            results = self.all.predict(_input)
        assert len(results) == 1
        result = results[0]
        if schema:
            print(result.keys())
            print(result)
            ...
        else:
            return result['rec_texts']
