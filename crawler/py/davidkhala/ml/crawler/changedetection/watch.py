from datetime import datetime

from davidkhala.ml.crawler.changedetection.api import API


class WatchAPI(API):
    def __init__(self, api_key, base_url):
        super().__init__(api_key, base_url)
        self.root_url = self.base_url
        self.base_url = f"{self.base_url}/watch"

    def list(self, recheck_all: bool = False, tag: str | None = None):
        return self.request(self.base_url, 'GET', params={
            'recheck_all': "1" if recheck_all else None,
            'tag': tag
        })

    def create(self, url, **kwargs):
        r = self.request(self.base_url, 'POST', json={
            'url': url,
            **kwargs
        })
        return r['uuid']
    def create_batch(self):
        r = self.request(self.base_url, 'POST', json={})
        # TODO
    def history(self, id:str)->dict[datetime, str]:
        r = self.request(f"{self.base_url}/{id}/history", 'GET')
        r_t = {}
        for timestamp, value in r.items():
            key = datetime.fromtimestamp(int(timestamp))
            r_t[key] = value
        return r_t

    @property
    def count(self):
        r = self.request(f"{self.root_url}/systeminfo", "GET")
        return r['watch_count']