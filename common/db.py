from pymongo import MongoClient
import datetime
from pymongo import InsertOne, DeleteMany, ReplaceOne, UpdateOne
import atexit


class MongoDBConnection(object):
    bulk_op = []

    def __init__(self, db_name='osint', host='localhost', port=27017):
        self.host = host
        self.port = port
        self.client = None
        self.db_name = db_name

    def __enter__(self):
        self.client = MongoClient(self.host, self.port)
        self.db = self.client[self.db_name]
        self.collection = self.db['raw']
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()

    def append(self, source, ip, run_date, data):
        resp = {
            "source": source,
            "resp": data,
            "last_modified": datetime.datetime.now()
        }
        find = {'input_ip': ip, 'run_date': run_date, 'source': source}
        MongoDBConnection.bulk_op.append(UpdateOne(find, {'$set': resp}, upsert=True))
        if len(self.bulk_op) >= 50:
            self.flush()

    def flush(self):
        temp = MongoDBConnection.bulk_op
        total = len(temp)
        if temp:
            self.collection.bulk_write(temp)
            temp.clear()
        print("Data has been flushed in mongo",  total)


@atexit.register
def exit_handler():
    with MongoDBConnection() as mdb:
        mdb.flush()


