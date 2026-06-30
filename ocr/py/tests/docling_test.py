import unittest
from pathlib import Path
from unittest import skipIf

from davidkhala.ml.ocr.docling import Converter, Extractor

transcript = Path(__file__).parent / "fixtures" / "transcript.png"
class ConverterTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Converter()

    def test_sample(self):
        """https://github.com/docling-project/docling#3-python-usage-recommended"""
        source = "https://arxiv.org/pdf/2408.09869"  # a document via a local path or URL
        result = self.client.process(source)
        self.assertIn('## Docling Technical Report', result.document.export_to_markdown())
    def test_transcript(self):
        result = self.client.process(transcript)
        print(result.document.export_to_markdown())
class ExtractTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Extractor()
    @skipIf(True, "known issue")
    def test_transcript(self):
        # FIXME E           TypeError: Qwen2VLForConditionalGeneration.__init__() got an unexpected keyword argument 'dtype'
        #   known issue: https://github.com/docling-project/docling/issues/2544
        r = self.client.process(transcript, schema={
            'Student': 'string',
        })