import requests
from urllib import request, parse
import configparser
from OSINT.common.web import get_data

parser = configparser.ConfigParser()
parser.read('blacklist.conf')

HEADERS = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'
}


def neutrino(ip):
    params = {
        'user-id': parser.get('Neutrino', 'user_id'),
        'api-key': parser.get('Neutrino', 'api_key'),
        'ip': ip
    }
    response = requests.post(parser.get('Neutrino', 'url'), data=params)
    return response


def signals(ip):
    headers = {
        'accept': "application/json",
        'x-auth-token': parser.get('Signals', 'api_key')
    }
    response = requests.get(parser.get('Signals', 'url') + ip, headers=headers)
    return response


# def virustotal(ip):
#     params = {'apikey': parser.get('VirusTotal', 'api_key'), 'ip': ip}
#     # response = requests.get(parser.get('VirusTotal', 'url') + 'ip-address/report', params=params)
#     response = requests.get(parser.get('VirusTotal', 'url') + 'ip-address/detection', params=params)
#     return response


def virustotal(ip):
    headers = dict(HEADERS)
    headers.update({'referer': 'https://www.virustotal.com/', 'authority': 'www.virustotal.com',
                   'accept': 'application/json', 'x-app-hostname': 'https://www.virustotal.com/gui/',
                   'x-app-version': '20200618t103427'})
    params = {'relationships[comment]': 'author,item',
              'relationships[url]': 'network_location,last_serving_ip_address',
              'limit': '20', 'query': ip}

    # 'cookie': '_ga=GA1.2.1945727751.1591424955; _gid=GA1.2.1730215913.1592410665;
    # __utma=194538546.1945727751.1591424955.1592477820.1592477820.1; __utmc=194538546;
    # __utmz=194538546.1592477820.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _gat=1',
    return requests.get('https://www.virustotal.com/ui/search', headers=headers, params=params)


if __name__ == '__main__':
    actual_ip = ''
    # for i in parser.sections():
    #     resp_type = parser.get(i, 'type')
    #     get_data(eval(i.lower()), resp_type,  actual_ip, '2020-06-17')
    i = 'virustotal'
    resp_type = 'html'
    get_data(eval(i.lower()), resp_type, actual_ip, '2020-06-16')
