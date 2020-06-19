import os
import requests
import configparser
from OSINT.common.web import get_data

config_file = os.path.join(os.path.dirname(__file__), 'ip_search_engine.conf')
parser = configparser.ConfigParser()
parser.read(config_file)


def shodan(ip):
    url = parser.get('Shodan', 'url')
    api_key = parser.get('Shodan', 'API_KEY')
    url = url + '%s?key=%s&minify=True' % (ip, api_key)
    return requests.get(url)


def censys(ip):
    url = parser.get('Censys', 'url')
    uid = parser.get('Censys', 'uid')
    secret = parser.get('Censys', 'secret')
    return requests.get(url + "/view/ipv4/" + ip, auth=(uid, secret))


def binaryedge(ip):
    headers = {'X-Key': parser.get('BinaryEdge', 'API_KEY')}
    return requests.get(parser.get('BinaryEdge', 'URL') + ip, headers=headers)


def onypye(ip):
    headers = {
        'Authorization': 'apikey %s' % parser.get('Onypye', 'API_KEY'),
        'Content-Type': 'application/json',
    }
    response = requests.get(parser.get('Onypye', 'url') + 'summary/ip/%s' % ip, headers=headers)
    return response


def run(ip):
    for sec in parser.sections():
        resp_type = parser.get(sec, 'type')
        get_data(eval(sec.lower()), resp_type,  ip, '2020-06-19')


if __name__ == '__main__':
    actual_ip = '59.185.252.201'
    for f in [shodan, censys, binaryedge, onyphe]:
        get_data(f, actual_ip, '2020-06-17')

