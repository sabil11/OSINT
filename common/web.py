import requests
import traceback
import collections
from OSINT.common.db import MongoDBConnection as mDB
from OSINT.config import config


err_cnt = collections.defaultdict(int)
SKIP_RESPONSE_CODES = [404]


def get_data(func, term, run_date, force=False, retry=0):
    source = func.__name__
    print(term, source)
    with mDB() as mdb:
        res = mdb.collection.find_one({'input': term, 'run_date': run_date, 'source': source})
        if (err_cnt[source] < 3) and (force or not res):
            try:
                resp = func(term)
                resp_type = config.get(source, 'type')
            except requests.Timeout as e:
                print(traceback.format_exc())
                err_cnt[source] += 1
            if resp.status_code == 200:
                if resp_type == 'json':
                    data = resp.json()
                else:
                    data = resp.content
                mdb.append(source, term, run_date, data)
                return True
            elif resp.status_code in SKIP_RESPONSE_CODES:
                print("Probably no data", resp.status_code)
            else:
                err_cnt[source] += 1
                print("Response status code: %s" % resp.status_code)
    return False
