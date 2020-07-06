import requests
from OSINT.config import config


class Binaryedge(object):
    # TODO Need to add other sections reputation, geo, malware, url_list, passive_dns
    def __init__(self, term):
        self.term = term
        self.url, self.api_key = config.get_n(self.__class__.__name__.upper(), 'url', 'api_key')
        self.headers = {'X-Key': self.api_key}

    def ip(self):
        url = self.url + 'query/ip/%s' % self.term
        return requests.get(url, headers=self.headers)

    # def domain(self):
    #     url = self.url + 'domain/%s/%s' %(self.term, 'general')
    #     return requests.get(url, headers=self.headers)
    #
    # def hash(self):
    #     url = self.url + 'file/%s/%s' %(self.term, 'general')
    #     return requests.get(url, headers=self.headers)

