import unittest
from pathlib import Path

from davidkhala.ml.ocr.paddle import Client


class SDKTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Client()


    def test_clean(self):
        self.client.clean()

    def test_schema(self):
        file = Path(__file__).parent / "fixtures" / "transcript.png"
        self.client.init('focus')
        self.client.process(file)


if __name__ == '__main__':
    unittest.main()
