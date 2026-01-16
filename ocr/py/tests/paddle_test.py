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
        from pprint import pprint
        from paddlenlp import Taskflow

        schema = ['时间', '选手', '赛事名称']  # Define the schema for entity extraction
        ie = Taskflow('information_extraction',
                      schema=schema,
                      schema_lang="zh",
                      batch_size=1,
                      model='paddlenlp/PP-UIE-0.5B',
                      precision='float16')
        pprint(
            ie("2月8日上午北京冬奥会自由式滑雪女子大跳台决赛中中国选手谷爱凌以188.25分获得金牌！"))  # Better print results using pprint
        # 输出
        # [{'时间': [{'text': '2月8日上午'}],
        #   '赛事名称': [{'text': '北京冬奥会自由式滑雪女子大跳台决赛'}],
        #   '选手': [{'text': '谷爱凌'}]}]


if __name__ == '__main__':
    unittest.main()
