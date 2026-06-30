import os
import unittest
from pathlib import Path
from unittest import skipIf


class PaddleOCRTestCase(unittest.TestCase):
    def setUp(self):
        from davidkhala.ml.ocr.paddle import Client
        self.client = Client()

    def test_all_text(self):
        file = Path(__file__).parent / "fixtures" / "transcript.png"
        self.client.init()
        tokens = self.client.process(file)
        self.assertIn('High School Transcript', tokens)

    @skipIf(os.environ.get("CI") is not None, "used for cleanup local only")
    def test_clean(self):
        self.client.clean()


class PaddleNLPTestCase(unittest.TestCase):
    def test_raw_sample(self):
        from paddlenlp import Taskflow

        schema = ['时间', '选手', '赛事名称']  # Define the schema for entity extraction
        ie = Taskflow('information_extraction',
                      schema=schema,
                      schema_lang="zh",
                      batch_size=1,
                      model='paddlenlp/PP-UIE-0.5B',
                      precision='float32')
        print(ie("2月8日上午北京冬奥会自由式滑雪女子大跳台决赛中中国选手谷爱凌以188.25分获得金牌！"))
        # [{'时间': [{'text': '2月8日上午'}],
        #   '赛事名称': [{'text': '北京冬奥会自由式滑雪女子大跳台决赛'}],
        #   '选手': [{'text': '谷爱凌'}]}]
    def test_client(self):
        from davidkhala.ml.ocr.paddle.ie import Client
        schema = ['时间', '选手', '赛事名称']  # Define the schema for entity extraction
        c = Client()
        text = "2月8日上午北京冬奥会自由式滑雪女子大跳台决赛中中国选手谷爱凌以188.25分获得金牌！"
        r = c.process(text, schema=schema)
        print(r)

if __name__ == '__main__':
    unittest.main()
