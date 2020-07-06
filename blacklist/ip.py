import requests
from OSINT.common.web import get_data
from OSINT.config import config


def neutrino(ip):
    url, api_key = config.get_n(name, 'url', 'user-id', 'api_key')

    params = {
        'user-id': config.get('Neutrino', 'user_id'),
        'api-key': config.get('Neutrino', 'api_key'),
        'ip': ip
    }
    response = requests.post(config.get('Neutrino', 'url'), data=params)
    return response


def signals(ip):
    headers = {
        'accept': "application/json",
        'x-auth-token': config.get('Signals', 'api_key')
    }
    response = requests.get(config.get('Signals', 'url') + ip, headers=headers)
    return response



# def virustotal(ip):
#     params = {'apikey': config.get('VirusTotal', 'api_key'), 'ip': ip}
#     # response = requests.get(config.get('VirusTotal', 'url') + 'ip-address/report', params=params)
#     response = requests.get(config.get('VirusTotal', 'url') + 'ip-address/detection', params=params)
#     return response





def run(ip):
    for sec in config.sections():
        resp_type = config.get(sec, 'type')
        get_data(eval(sec.lower()), resp_type, ip, '2020-06-19')


if __name__ == '__main__':
    actual_ip = ''
    # for i in config.sections():
    #     resp_type = config.get(i, 'type')
    #     get_data(eval(i.lower()), resp_type,  actual_ip, '2020-06-17')
    i = 'virustotal'
    resp_type = 'html'
    get_data(eval(i.lower()), resp_type, actual_ip, '2020-06-16')
