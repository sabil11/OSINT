import requests
from OSINT.config import config


class Onyphe(object):

    def __init__(self, term):
        self.term = term
        self.url, self.api_key = config.get_n(self.__class__.__name__.upper(), 'url', 'api_key')
        self.headers = {
            'Authorization': 'apikey %s' % self.api_key,
            'Content-Type': 'application/json',
        }

    def ip(self):
        url = self.url + 'summary/ip/%s' % self.term
        return requests.get(url, headers=self.headers)

    def domain(self):
        url = self.url + 'summary/domain/%s' % self.term
        return requests.get(url, headers=self.headers)

