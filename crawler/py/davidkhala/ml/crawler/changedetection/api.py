from davidkhala.utils.http_request import Request


class API(Request):
    def __init__(self, api_key, base_url='https://app.changedetection.io'):
        super().__init__()
        self.options['headers']['x-api-key'] = api_key
        self.base_url = f"{base_url}/api/v1"
