import requests
import traceback
import collections
from OSINT.common.db import MongoDBConnection as MDB

err_cnt = collections.defaultdict(int)
SKIP_RESPONSE_CODES = [404]


def get_data(func, ip, run_date, force=False):
    source = func.__name__
    print(ip, source)
    with MDB() as mdb:
        res = mdb.collection.find_one({'input_ip': ip, 'run_date': run_date, 'source': source})
        if (err_cnt[source] < 3) and (force or not res):
            try:
                resp = func(ip)
            except requests.Timeout as e:
                print(traceback.format_exc())
                err_cnt[source] += 1
            if resp.status_code == 200:
                data = resp.json()
                print(data)
                mdb.append(source, ip, run_date, data)
                return True
            elif resp.status_code in SKIP_RESPONSE_CODES:
                print("Probably no data", resp.status_code)
            else:
                err_cnt[source] += 1
                print("Response status code: %s" % resp.status_code)
    return False
