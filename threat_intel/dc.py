import os
import requests
import configparser
from OSINT.common.web import get_data

config_file = os.path.join(os.path.dirname(__file__), 'threat_intel.conf')
parser = configparser.ConfigParser()
parser.read(config_file)


def intel(val):
    h = {'x-key': parser.read('intelx', 'api_key')}
    p = {
        "term": term,
        "buckets": buckets,
        "lookuplevel": 0,
        "maxresults": maxresults,
        "timeout": timeout,
        "datefrom": datefrom,
        "dateto": dateto,
        "sort": sort,
        "media": media,
        "terminate": terminate
    }
    r = requests.post(self.API_ROOT + '/intelligent/search', headers=h, json=p)


def run(ip):
    for sec in parser.sections():
        resp_type = parser.get(sec, 'type')
        get_data(eval(sec.lower()), resp_type,  ip, '2020-06-19')


if __name__ == '__main__':
    actual_ip = '59.185.252.201'
    # for f in [shodan, censys, binaryedge, onypye]:
    #     get_data(f, actual_ip, '2020-06-17')
