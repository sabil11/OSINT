import requests
from urllib import request, parse
import configparser
from OSINT.common.web import get_data

parser = configparser.ConfigParser()
parser.read('blacklist.conf')


def neutrino(ip):
    params = {
        'user-id': parser.get('Neutrino', 'user_id'),
        'api-key': parser.get('Neutrino', 'api_key'),
        'ip': ip
    }
    data = parse.urlencode(params).encode()
    req = request.Request(parser.get('Neutrino', 'url'), data=data)
    response = request.urlopen(req)
    return response


def signals(ip):
    headers = {
        'accept': "application/json",
        'x-auth-token': parser.get('Signals', 'api_key')
    }
    response = requests.get(parser.get('Signals', 'url') + ip, headers=headers)
    return response


def virustotal(ip):
    params = {'apikey': parser.get('VirusTotal', 'apiy_key') + ip, 'ip': ip}
    response = requests.get(parser.get('VirusTotal', 'url') + 'ip-address/report', params=params)
    return response


