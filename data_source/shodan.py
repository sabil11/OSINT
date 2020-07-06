import requests
from OSINT.config import config
from OSINT.common.web import  get_data
import time



class Shodan(object):
    def __init__(self):
        self.__class__.__name__
        url, api_key = config.get_n(self.__class__.__name__.upper(), 'url', 'api_key')

    def ip(self, term):
        url = self.url + '%s?key=%s' % (term, self.api_key)
        return requests.get(url)

    def domain(self, term):
        url = self.url + '/search?key=%s&query=%s' % (self.api_key, term)
        return requests.get(url)

    def run(self, search_type, values, run_date):
        for i in values:
            get_data(eval("self." + search_type), i, run_date)
            time.sleep(2)




