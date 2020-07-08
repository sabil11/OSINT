import requests
from OSINT.config import config
from OSINT.common.web import get_data
import time


class Otx(object):
    # TODO Need to add other sections reputation, geo, malware, url_list, passive_dns
    def __init__(self, ):

        self.baseurl, self.api_key = config.get_n(self.__class__.__name__.upper(), 'url', 'api_key')
        self.headers = {'X-OTX-API-KEY': self.api_key}

    def ip(self, term):
        url = self.baseurl + 'IPv4/%s/%s' %(term, 'general')
        return requests.get(url, headers=self.headers)

    def domain(self, term):
        url = self.baseurl + 'domain/%s/%s' %(term, 'general')
        return requests.get(url, headers=self.headers)

    def hash(self, term):
        url = self.baseurl + 'file/%s/%s' %(term, 'general')
        return requests.get(url, headers=self.headers)

    def search(self, term):
        url = self.baseurl + "search/pulses/"
        params = {"q": term}
        return requests.get(url, params=params, headers=self.headers)

    def run(self, search_type, values, run_date):
        for i in values:
            get_data(eval("self." + search_type), i, run_date)
            time.sleep(2)


