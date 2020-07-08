import requests
from OSINT.config import config
from OSINT.common.web import  get_data
import time
import base64


class Virustotal(object):

    def __init__(self, ):
        self.classname = self.__class__.__name__.upper()
        self.baseurl, self.api_key, self.source_type = config.get_n(self.classname, 'url', 'api_key', 'type')
        self.headers = {'x-apikey': self.api_key, 'User-Agent': "curl/7.68.0"}

    def ip(self, ip):
        url = self.baseurl + 'ip_addresses/' + ip
        return requests.get(url, headers=self.headers)

    def domain(self, domain):
        url = self.baseurl + 'domains/' + domain
        return requests.get(url, headers=self.headers)

    def hash(self, hsh):
        url = self.baseurl + 'files/' + hsh
        return requests.get(url, headers=self.headers)

    def url(self, _url):

        encoded_url = base64.b64encode(_url.encode('ascii')).decode()
        url = self.baseurl + 'urls/' + encoded_url
        print(url, _url)
        return requests.get(url, headers=self.headers)

    def run(self, search_type, values, run_date):
        total = len(values)
        for c, i in enumerate(values, 1):
            resp = get_data(eval("self." + search_type), i, self.source_type, self.classname, run_date)
            if resp or c < total:
                # to skip last sleep
                time.sleep(15)


if __name__ == '__main__':
    vt = Virustotal()