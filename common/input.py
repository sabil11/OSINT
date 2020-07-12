import csv
import os
import ipaddress
import validators
import re


def get_port_inp(port_str):

    def port_pattern(p_str):
        p_str = p_str.strip()
        if p_str[1].lower() == 't':
            tcp_port.extend(p_str[2:].split('/'))
        elif p_str[1].lower() == 'u':
            udp_port.extend(p_str[2:].split('/'))
        else:
            raise Exception("Incorrect protocol use either (T/U)")

    udp_port = []
    tcp_port = []
    temp = port_str.split(',')
    if len(temp) > 2:
        raise Exception("Improper port")
    elif len(temp) == 1:
        port_pattern(temp[0])
    elif len(temp) == 2:
        port_pattern(temp[0])
        port_pattern(temp[1])
    return tcp_port, udp_port


def read_input_csv(inputfile):
    ip_list = []
    domain_list = []
    with open(inputfile) as inf:
        reader = csv.reader(inf)
        reader.__next__()  # skip header
        for i in reader:
            if '-' in i[0]:
                nt, start, end = re.findall('(\d+\.\d+\.\d+\.)(\d+)\-(\d+)', i[0])[0]
                for oct in range(int(start), int(end) + 1):
                    ip_list.append(str(ipaddress.ip_address(nt + str(oct))))
            elif validators.ipv4_cidr(i[0]):
                ip_list.extend([str(ip) for ip in ipaddress.ip_network(i[0])])
            elif validators.ipv4(i[0]):
                ip_list.append(str(ipaddress.ip_address(i[0])))
            elif validators.domain(i):
                domain_list.append(i[0])
    return list(set(ip_list)), list(set(domain_list))


def parse_db_list(s_type, inp_list):
    temp = []

    for i in inp_list:
        if s_type == 'ip':
            if '-' in i:
                nt, start, end = re.findall(r"(\d+\.\d+\.\d+\.)(\d+)\-(\d+)", i)[0]
                for oct in range(int(start), int(end) + 1):
                    temp.append(str(ipaddress.ip_address(nt + str(oct))))
            elif validators.ipv4_cidr(i):
                temp.extend([str(ip) for ip in ipaddress.ip_network(i)])
            elif validators.ipv4(i):
                temp.append(str(ipaddress.ip_address(i)))
        elif validators.domain(i):
            temp.append(i)
    return temp
