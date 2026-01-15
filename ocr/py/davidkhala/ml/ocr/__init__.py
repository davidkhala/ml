import base64
from abc import ABC, abstractmethod
from pathlib import Path


class Client(ABC):
    @staticmethod
    def _read(file: Path) -> str:
        with open(file, "rb") as f:
            content = base64.b64encode(f.read()).decode('utf-8')
        return content

    @abstractmethod
    def process(self, file: Path, **kwargs) -> list[dict] | dict: ...
