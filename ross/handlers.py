import requests as req

class RossInterface:
    html = None
    request_result = None
    url = None
    proxies = None

    def make_request(self):
        raise NotImplemented

    def get_response(self):
        raise NotImplemented


class Ross(RossInterface):
    def __init__(self, url):
        self.url = url
        self.PROXIES = {
            'http':'127.0.0.1:8118',
            'https':'127.0.0.1:8118'
        }
    
    def make_request(self, url=None, proxies=None):
        if url is None:
            url = self.url
        if proxies is None:
            proxies = self.PROXIES
        try:
            self.request_result = req.get(url, proxies=proxies)
            return self.request_result
        except Exception as e:
            print(e)
            return False
    
    def get_response(self, format=None):
        if format == 'json':
            try:
                return self.request_result.json()
            except:
                pass
        return self.request_result.text
