import requests
from OSINT.config import config
from OSINT.common.web import  get_data
import time


class Virustotal(object):

    def __init__(self, ):
        classname = self.__class__.__name__.upper()
        self.url, self.api_key, self.source_type = config.get_n(classname, 'url', 'api_key', 'type')
        self.headers = {'x-apikey': self.api_key, 'User-Agent': "curl/7.68.0"}

    def ip(self, ip):
        url = self.url + 'ip_addresses/' + ip
        return requests.get(url, headers=self.headers)

    def domain(self, domain):
        url = self.url + 'domains/' + domain
        return requests.get(url, headers=self.headers)

    def hash(self, hsh):
        url = self.url + 'files/' + hsh
        return requests.get(url, headers=self.headers)

    def run(self, search_type, values, run_date):
        for i in values:
            get_data(eval("self." + search_type), i, run_date)
            time.sleep(15)


