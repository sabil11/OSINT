from bottle import Bottle, request, response
from bottle import run
from bottle.ext.mongo import MongoPlugin
import datetime
from bson import ObjectId

app = Bottle()
plugin = MongoPlugin(uri="mongodb://127.0.0.1", db="app", json_mongo=True)
app.install(plugin)


@app.get('/')
def hello():
    return 'Hello, World!'


def save_and_trigger(data, mongodb):

    result = mongodb.requests.find_one(data, {'status': 1, "id": 1})
    print(result)
    if not result:
        data['status'] = 'queued'
        data['request_time'] = str(datetime.datetime.now())
        resp = mongodb.requests.insert_one(data)
        result = mongodb.requests.find_one({"_id": resp.inserted_id })
    return result


@app.post('/collect')
def collect(mongodb):
    print("here")
    data = request.json
    response.headers['Content-Type'] = 'application/json'
    resp = save_and_trigger(data, mongodb)
    return resp


@app.get('/collect')
def get_data(mongodb):
    data = request.json
    response.headers['Content-Type'] = 'application/json'
    result = mongodb.requests.find_one({"_id": ObjectId(data['id'])})
    if not result:
        result = dict(data)
        result['status'] = "id doesn't exist"
    return result


if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True, reloader=True)

     # app.run()
    # # save_and_trigger({'type': 'ip', 'source': ['virustotal', 'shodan'], 'run_date': '2020-07-09'})
