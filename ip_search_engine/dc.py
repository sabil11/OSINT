import requests
import configparser
from OSINT.common.generic import get_data


parser = configparser.ConfigParser()
parser.read('../conf')


def shodan(ip):
    url = parser.get('SHODAN', 'url')
    api_key = parser.get('SHODAN', 'API_KEY')
    url = url + '%s?key=%s&minify=True' % (ip, api_key)
    return requests.get(url)


def censys(ip):
    url = parser.get('CENSYS', 'url')
    uid = parser.get('CENSYS', 'uid')
    secret = parser.get('CENSYS', 'secret')
    return requests.get(url + "/view/ipv4/" + ip, auth=(uid, secret))


def binaryedge(ip):
    headers = {'X-Key': parser.get('BinaryEdge', 'API_KEY')}
    return requests.get(parser.get('BinaryEdge', 'URL') + ip, headers=headers)


def onyphe(ip):
    headers = {
        'Authorization': 'apikey %s' % parser.get('ONYPYE', 'API_KEY'),
        'Content-Type': 'application/json',
    }
    response = requests.get(parser.get('ONYPYE', 'url') + 'summary/ip/%s' % ip, headers=headers)
    return response


if __name__ == '__main__':
    actual_ip = ''
    for f in [shodan, censys, binaryedge, onyphe]:
        get_data(f, actual_ip, '2020-06-17')

