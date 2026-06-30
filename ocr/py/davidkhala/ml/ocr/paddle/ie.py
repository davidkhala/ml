from davidkhala.utils.syntax.path import home_resolve, delete
from paddlenlp import Taskflow
from davidkhala.ml.ocr import Client as BaseClient


class Client(BaseClient):
    def __init__(self):
        self.options = {
            'task': 'information_extraction',
            'batch_size': 1,
            'model': 'paddlenlp/PP-UIE-0.5B',
            'precision': 'float32',
        }

    @staticmethod
    def clean():
        """clean up downloaded models on local disk"""
        delete(home_resolve('.paddlenlp', 'models'))

    def process(self, text: str, **kwargs) -> list[dict]:
        schema: list[str] = kwargs["schema"]
        ie = Taskflow(
            **self.options,
            schema=schema
        )
        results = ie(text)
        assert len(results) == self.options['batch_size']
        return [{k: [_['text'] for _ in v] for k, v in item.items()} for item in results]
