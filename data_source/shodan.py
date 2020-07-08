import requests
from OSINT.config import config
from OSINT.common.web import  get_data
import time



class Shodan(object):
    def __init__(self):
        self.__class__.__name__
        self.baseurl, self.api_key = config.get_n(self.__class__.__name__.upper(), 'url', 'api_key')

    def ip(self, term):
        url = self.baseurl + '%s?key=%s' % (term, self.api_key)
        return requests.get(url)

    def domain(self, term):
        url = self.baseurl + '/search?key=%s&query=%s' % (self.api_key, term)
        return requests.get(url)

    def run(self, search_type, values, run_date):
        total = len(values)
        for c, i in enumerate(values, 1):
            resp = get_data(eval("self." + search_type), i, self.source_type, self.classname, run_date)
            if resp or c < total:
                # to skip last sleep
                time.sleep(2)





