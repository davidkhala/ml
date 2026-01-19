from davidkhala.utils.syntax.path import home_resolve, delete
from paddlenlp import Taskflow


class Client:
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

    def process(self, text: str, _schema: list[str]) -> list[dict]:
        ie = Taskflow(
            **self.options,
            schema=_schema
        )
        results = ie(text)
        assert len(results) == self.options['batch_size']
        return [{ k: [_['text'] for _ in v] for k, v in item.items()} for item in results ]


