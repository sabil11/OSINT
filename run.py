from OSINT.common.input import read_input_csv
import OSINT.search_engine.ip as ip_search_engine_dc
import OSINT.blacklist.ip as blacklist_dc
from OSINT.data_source import virustotal, shodan, otx


def ip_search(ip_list, run='both'):
    if run == 'dc':
        vt = virustotal.Virustotal()
        vt.run("ip", ip_list, "2020-07-06")


if __name__ == '__main__':
    iplist, domain_list = read_input_csv('input.csv')
    print(iplist, domain_list)
    ip_search(iplist, 'dc')
