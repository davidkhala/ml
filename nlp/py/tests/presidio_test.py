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
        print(marker.redact(self.text, analyzer.detect(self.text)))


from davidkhala.ml.nlp.presidio.image import Client

_in = Path(__file__).parent / 'fixtures' / 'transfer.jpeg'
_out = Path(__file__).parent / 'artifacts' / 'transfer-redacted.jpeg'


class ImageTest(unittest.TestCase):
    def test_mask(self):
        client = Client()
        client.redact(_in, _out)


from davidkhala.ml.nlp.presidio.testcontainers import Image as ImageContainer, Analyzer as AnalyzerContainer, \
    Anonymizer as AnonymizerContainer, BaseContainer
from davidkhala.ml.nlp.presidio.request import Request


class ContainerTest(unittest.TestCase):
    container: BaseContainer

    def setUp(self):
        self.container.start()
        base_url = f"http://localhost:{self.container.exposed_port}"
        self.request = Request(base_url)

    def tearDown(self):
        self.container.stop()


class ImageContainerTest(ContainerTest):
    def setUp(self):
        self.container = ImageContainer()
        super().setUp()

    def test_transfer(self):
        self.request.image_redact(source=_in, target=_out)


class AnalyzerContainerTest(ContainerTest):
    def setUp(self):
        self.container = AnalyzerContainer()
        super().setUp()

    def test_sample(self):
        text = "My phone number is 555-123-4567."
        r = self.request.analyze(text)
        print(r)
        self.assertEqual(1, len(r))
        r0 = r[0]
        self.assertDictEqual(
            {'analysis_explanation': None, 'end': 31, 'entity_type': 'PHONE_NUMBER', 'score': 0.75, 'start': 19},
            r0)


class AnonymizerContainerTest(AnalyzerContainerTest):
    def setUp(self):
        super().setUp()
        self.anonymizerC = AnonymizerContainer()
        self.anonymizerC.start()
        self.request2 = Request(f"http://localhost:{self.anonymizerC.exposed_port}")

    def tearDown(self):
        self.anonymizerC.stop()

    def test_sample(self):
        text = "My phone number is 555-123-4567."
        r = self.request2.anonymize(text,
                                    analyzer_results=self.request.analyze(text),
                                    anonymizers={
                                       "PHONE_NUMBER": {"type": "replace", "new_value": "--Redacted phone number--"}
                                   })
        print(r)
