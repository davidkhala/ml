import unittest
from pathlib import Path

from davidkhala.ml.nlp.presidio.text import Analyzer, Anonymizer


class TextTest(unittest.TestCase):
    text = "My phone number is 212-555-5555"

    def test_analyze(self):
        analyzer = Analyzer()
        print(analyzer.detect(self.text))

    def test_mask(self):
        analyzer = Analyzer()
        marker = Anonymizer()
        print(marker.redact(self.text, analyzer.detect(self.text)).to_json())


from davidkhala.ml.nlp.presidio.image import Client

_in = Path(__file__).parent / 'fixtures' / 'transfer.jpeg'
_out = Path(__file__).parent / 'artifacts' / 'transfer-redacted.jpeg'


class ImageTest(unittest.TestCase):
    def test_mask(self):
        client = Client()
        client.redact(_in, _out)


from davidkhala.ml.nlp.presidio.testcontainers import Image, Request


class TestcontainersTest(unittest.TestCase):
    def setUp(self):
        self.container = Image()
        self.container.start()
        base_url = f"http://localhost:{self.container.exposed_port}"
        self.request = Request(base_url)

    def tearDown(self):
        self.container.stop()

    def test_image(self):
        self.request.image_redact(source=_in, target=_out)
