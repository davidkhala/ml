import unittest
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


class CrawlTest(unittest.TestCase):
    def test_thei(self):

        visited = set()

        def crawl(root_url, visited, current_url):
            if current_url in visited or not current_url.startswith(root_url):
                return
            visited.add(current_url)
            try:
                res = requests.get(current_url, timeout=5)
                soup = BeautifulSoup(res.text, "html.parser")
                for a in soup.find_all("a", href=True):
                    next_url = urljoin(current_url, a["href"])
                    crawl(root_url, visited, next_url)
            except:
                pass

            return visited

        crawl("https://thei.edu.hk", visited, "https://thei.edu.hk") # FIXME timeout
        print(f"Total unique URLs: {len(visited)}")


if __name__ == '__main__':
    unittest.main()
