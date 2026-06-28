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

class ImageTest(unittest.TestCase):
    def test_mask(self):
        path = Path(__file__).parent / 'transfer.jpeg'
        from davidkhala.ml.nlp.presidio.image import Client
        client = Client()
        print(client.redact(path))