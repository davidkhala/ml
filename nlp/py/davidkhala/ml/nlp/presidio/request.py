from os import PathLike
from typing import TypedDict, Any

from davidkhala.utils.http_request import Request as RawRequest, default_on_response
from davidkhala.utils.http_request.on_response import file


class RecognizerResult(TypedDict):
    start: int
    end: int
    score: float
    entity_type: str
    analysis_explanation: Any


class OperatorConfig(TypedDict):
    type: str
    ...


class Request(RawRequest):
    def __init__(self, base_url):
        super().__init__()
        self.base_url = base_url

    def image_redact(self, *, source: PathLike, data: dict | None = None, target: PathLike):
        # curl -XPOST "http://localhost:3000/redact" -H "content-type: multipart/form-data" -F "image=@ocr_test.png" -F "data=\"{'color_fill':'255'}\""
        url = f"{self.base_url}/redact"

        self.on_response = file
        if not data:
            data = {}
        with open(source, "rb") as f:
            resp: bytes = self.request(url, method="POST", files={"image": f}, data={"data": str(data)})

        with open(target, "wb") as out:
            out.write(resp)
        self.on_response = default_on_response

    def analyze(self, text: str, *, language="en") -> list[RecognizerResult]:
        # curl -X POST http://localhost:5002/analyze -H "Content-Type: application/json" -d '{"text": "My phone number is 555-123-4567.",   "language": "en" }'
        return self.request(f"{self.base_url}/analyze", method="POST", json={'text': text, 'language': language})

    def anonymize(self, text: str,
                  *,
                  anonymizers: dict[str, OperatorConfig], analyzer_results: list[RecognizerResult]
                  ) -> str:
        r = self.request(f"{self.base_url}/anonymize", method="POST", json={
            'text': text, 'anonymizers': anonymizers, 'analyzer_results': analyzer_results
        })
        return r['text']
