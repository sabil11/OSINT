from flask import Flask, request, Response
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/app"
mongo = PyMongo(app)


@app.route('/')
def hello():
    return 'Hello, World!'


def save_and_trigger(data):

    result = mongo.db.requests.find_one(data, {'status': 1, "_id": 1})
    print(result)
    if not result:
        data['status'] = 'queued'
        resp = mongo.db.requests.insert_one(data)
        result = mongo.db.requests.find_one({"_id": resp.inserted_id })
    result['_id'] = str(result["_id"])
    return result


@app.route('/collect',  methods=['POST', 'GET'])
def collect():
    print("here")
    data = request.json
    if request.method == "POST":
        print(data)
        save_and_trigger(data)
        Response.headers['Content-Type'] = 'application/json'
    else:
        print(data)
    return "Good!!"


if __name__ == '__main__':
    app.run()
    # save_and_trigger({'type': 'ip', 'source': ['virustotal', 'shodan'], 'run_date': '2020-07-09'})
