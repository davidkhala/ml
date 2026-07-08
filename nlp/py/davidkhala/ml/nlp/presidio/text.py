import json

from presidio_analyzer import AnalyzerEngine, RecognizerResult
from presidio_anonymizer import AnonymizerEngine, EngineResult


class Analyzer:
    def __init__(self):
        self._ = AnalyzerEngine()

    def detect(self, text: str, *, language='en', **kwargs) -> list[RecognizerResult]:
        return self._.analyze(text=text, language=language, **kwargs)


class Anonymizer:
    def __init__(self):
        self._ = AnonymizerEngine()

    def redact(self, text: str, mark: list[RecognizerResult]) -> dict:
        r: EngineResult = self._.anonymize(text=text, analyzer_results=mark)
        return json.loads(r.to_json())
