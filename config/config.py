import os
import configparser

parser = configparser.ConfigParser()


def read():
    config_file = os.path.join(os.path.dirname(__file__), 'source.conf')
    parser.read(config_file)

read()
def get(section, var):
    return parser.get(section.upper(), var)


def get_n(section, *args):
    return [parser.get(section.upper(), i) for i in args]




