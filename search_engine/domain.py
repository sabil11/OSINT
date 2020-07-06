import requests
from OSINT.common.web import get_data
from OSINT.config import config
from OSINT.common import generic


def shodan(term, name):
    url, api_key = config.get_n(name, 'url', 'api_key')
    url = url + '/search?key=%s&query=%s' % (api_key, term)
    return requests.get(url)


def censys(term, name):
    url, uid, secret = config.get_n(name, 'url', 'uid', 'secret')
    return requests.get(url + "/view/websites/" + term, auth=(uid, secret))


def binaryedge(term, name):
    url, api_key = config.get_n(name, 'url', 'api_key')
    headers = {'X-Key': api_key}
    return requests.get(url + term, headers=headers)


def onyphe(term, name):
    return generic.onyphe(term, 'domain', name)


def virustotal(term, name):
    return generic.virustotal(term, 'domain', name)


def run(ip):

    for sec in ['SHODAN', 'VIRUSTOTAL', 'ONYPHE', 'CENSYS']:
    # for sec in config.sections():
        get_data(eval(sec.lower()),  ip, '2020-06-20')


if __name__ == '__main__':
    var = 'lntecc.com'
    # for f in [shodan, censys, binaryedge, onyphe, virustotal]:
    #     get_data(f, actual_ip, '2020-06-17')
    run(var)

