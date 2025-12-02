import unittest

from davidkhala.ml.crawler.changedetection.watch import WatchAPI

api_key = '210c86aa8621847f73cd8aac5f0993a6'
class WatchTestCase(unittest.TestCase):

    watch = WatchAPI(api_key, 'http://localhost:5000')
    def test_list(self):
        print(self.watch.list())
    def test_create(self):
        print(self.watch.create('https://blog.csdn.net/gitblog_00779/article/details/150789129'))
    def test_history(self):
        id = 'b473ed9b-7ce2-41d7-912a-d09a76bfdda8'
        r = self.watch.history(id)
        print(r)
    def test_count(self):
        print(self.watch.count)
    def test_batch(self):
        urls= [
            'https://thei.edu.hk',
            'https://thei.edu.hk/departments/department-of-construction-environment-and-engineering/bachelor-of-engineering-honours-digital-manufacturing/'
        ]
        r = self.watch.create_batch(*urls)
        print(r)

if __name__ == '__main__':
    unittest.main()
