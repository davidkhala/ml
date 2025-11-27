import os
import unittest

from davidkhala.ml.crawler.firecrawl import Client


@unittest.skipIf(os.getenv('CI'), "open source deployment only")
class LocalTest(unittest.TestCase):
    firecrawl_i = Client('my-local-key', 'http://localhost:3002')

    def test_thei(self):
        r = self.firecrawl_i.scrape("https://thei.edu.hk")
        print(r)


if __name__ == '__main__':
    unittest.main()
