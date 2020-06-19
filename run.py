from OSINT.common.input import read_input_csv
import OSINT.ip_search_engine.dc as ip_search_engine_dc
import OSINT.blacklist.dc as blacklist_dc


def main(ip_list, run='both'):
    if run == 'dc':
        for ip in ip_list:
            ip_search_engine_dc.run(ip)
            blacklist_dc.run(ip)



if __name__ == '__main__':
    iplist, domain_list = read_input_csv('input.csv')
    print(iplist, domain_list)
    main(iplist, 'dc')
