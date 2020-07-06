import requests
from OSINT.config import config


class Censys(object):

    def __init__(self, term):
        self.term = term
        self.url, *self.auth = config.get_n(self.__class__.__name__.upper(), 'url', 'uid', 'secret')

    def ip(self):
        temp_url = self.url + "/view/ipv4/" + self.term
        return requests.get(temp_url, auth=self.auth)

    def domain(self):
        temp_url = self.url + "/view/websites/" + self.term
        return requests.get(temp_url, auth=self.auth)

    def hash(self):
        temp_url = self.url + "/view/certificates/" + self.term
        return requests.get(temp_url, auth=self.auth)
