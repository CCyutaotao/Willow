# -*- coding: utf-8 -*-

import os

from flask import Flask, jsonify, make_response, request, abort


from pymongo import MongoClient
from bson import json_util
from bson.objectid import ObjectId

import json
from datetime import datetime

app = Flask(__name__)
app.config['DB'] = 'willow'

client = MongoClient('mongodb://localhost:27017/?ssl=true')

db = client[app.config['DB']]


from elasticsearch import Elasticsearch

app.config['ELASTICSEARCH_URL'] = 'http://127.0.0.1:9200'


es = Elasticsearch(app.config['ELASTICSEARCH_URL'])


es.indices.create(index='title_index', ignore=400)

@app.route('/academy/<string:title_id>/', methods=['GET'])
def get_title(title_id):
    es.indices.create(index='my-index', ignore=400)
    es.index(index="my-index", doc_type="test-type", id=42, body={"any": "data", "timestamp": datetime.now()})
    title = db['academy'].find_one(
        {'_id': ObjectId(title_id)}
    )
    return jsonify({'title': json.dumps(title['title'])})


if __name__ == '__main__':
    app.run(debug=True)

