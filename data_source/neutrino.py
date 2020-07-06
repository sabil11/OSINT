import requests
from OSINT.config import config


class Neutrino(object):

    def __init__(self, term):
        self.url, user_id, api_key = config.get_n(self.__class__.__name__.upper(), 'url', 'user_id', 'api_key')

        self.params = {
            'user-id': user_id,
            'api-key': api_key,
            'ip': term
        }

    def ip(self):
        return requests.get(url, headers=self.headers)

    def domain(self):
        url = self.url + 'domains/' + self.term
        return requests.get(url, headers=self.headers)

    def hash(self):
        url = self.url + 'files/' + self.term
        return requests.get(url, headers=self.headers)

