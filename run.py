from OSINT.common.input import read_input_csv
from OSINT.data_source import virustotal
from OSINT.data_source import shodan


def ip_search(source_list, ip_list, run_date, run='both'):
    if run == 'dc':
        for source in source_list:
            obj = eval("%s.%s()" % (source, source.capitalize()))
            obj.run("ip", ip_list, run_date)

    #     vt = virustotal.Virustotal()
    #     vt.run("ip", ip_list, "2020-07-06")
    #



if __name__ == '__main__':
    iplist, domain_list = read_input_csv('docs/input.csv')
    print(iplist, domain_list)
    ip_search(['virustotal'], iplist, run_date= "2020-07-07", run='dc')
