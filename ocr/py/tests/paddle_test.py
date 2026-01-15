import os
import platform
import unittest
from pathlib import Path
from unittest import skipIf

from davidkhala.ml.ocr.paddle import Client


class SDKTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    @skipIf(platform.system() == 'Windows',
            'NotImplementedError: (Unimplemented) ConvertPirAttribute2RuntimeAttribute not support [pir::ArrayAttribute<pir::DoubleAttribute>]  (at ..\paddle\fluid\framework\new_executor\instruction\onednn\onednn_instruction.cc:118')
    def test_predict(self):
        file = Path(__file__).parent / "fixtures" / "transcript.png"
        self.client.process(file)


if __name__ == '__main__':
    unittest.main()
