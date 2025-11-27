from firecrawl import Firecrawl


class Client:
    def __init__(self, api_key: str, api_url: str | None=None):
        self._ = Firecrawl(api_key, api_url)

    def scrape(self, url):
        return self._.scrape(
            url,
            formats=['markdown', 'change_tracking']
        )
