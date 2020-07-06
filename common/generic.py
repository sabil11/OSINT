from OSINT.config import config
import requests


def virustotal(term, var, name):
    url, api_key = config.get_n(name, 'url', 'api_key')
    headers = {'x-apikey': api_key}
    vt_map = {'ip': 'ip_addresses', 'domain': 'domains', 'hash': 'files'}
    if var in vt_map:
        temp_url = url + vt_map[var] + '/' + term
        return requests.get(temp_url, headers=headers)
    else:
        return False


def onyphe(term, var, name):
    url, api_key = config.get_n(name, 'url', 'api_key')
    headers = {
        'Authorization': 'apikey %s' % api_key,
        'Content-Type': 'application/json',
    }
    url = url + 'summary/%s/%s' % (var, term)
    return requests.get(url, headers=headers)


def otx(entity, entity_type, name):
    # Multi section need to be retireved for hash, ip, domain
    url, api_key = config.get_n(name, 'url', 'api_key')
    headers = {"X-OTX-API-KEY": name}
    url = config.get('OTX', 'url')


    # response = requests.get('https://www.virustotal.com/api/v3/files/%7Bid%7D', headers=headers)

