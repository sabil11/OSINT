import requests
from OSINT.common.web import get_data
from OSINT.config import config
from OSINT.common import generic


def shodan(ip, name):
    url, api_key = config.get_n(name, 'url', 'api_key')
    url = url + '%s?key=%s' % (ip, api_key)
    return requests.get(url)


def censys(ip, name):
    url, uid, secret = config.get_n(name, 'url', 'uid', 'secret')
    return requests.get(url + "/view/ipv4/" + ip, auth=(uid, secret))


def binaryedge(ip, name):
    url, api_key = config.get_n(name, 'url', 'api_key')
    headers = {'X-Key': api_key}
    return requests.get(url + ip, headers=headers)


def onyphe(term, name):
    return generic.onyphe(term, 'ip', name)


def virustotal(ip, name):
    return generic.virustotal(ip, 'ip', name)


def run(ip):

    for sec in ['SHODAN', 'VIRUSTOTAL', 'onyphe']:
    # for sec in config.sections():
        get_data(eval(sec.lower()),  ip, '2020-06-20',)



if __name__ == '__main__':
    actual_ip = '59.185.252.201'
    # for f in [shodan, censys, binaryedge, onyphe, virustotal]:
    #     get_data(f, actual_ip, '2020-06-17')
    run(actual_ip)

