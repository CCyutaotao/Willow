# -*- coding: utf-8 -*-

import os

from flask import Flask, jsonify, make_response, request, abort


from pymongo import MongoClient
from bson import json_util
from bson.objectid import ObjectId

import json
from datetime import datetime

app = Flask(__name__)
app.config['MONGODB_HOST'] = 'localhost'
app.config['MONGODB_PORT'] = 27017
app.config['DB'] = 'willow'

client = MongoClient()
db = client[app.config['DB']]


from elasticsearch import Elasticsearch

app.config['ELASTICSEARCH_URL'] = 'http://127.0.0.1:9200'

es = Elasticsearch(app.config['ELASTICSEARCH_URL'])


es.indics.create(index='title_index', ignore=400)


@app.route('/academy/<string:title_id>/', methods=['GET'])
def get_title(title_id):
    title = db['academy'].find_one(
        {'_id': ObjectId(title_id)}
    )
    return jsonify({'title': json.dumps(title['title'])})


if __name__ == '__main__':
    app.run(debug=True)

