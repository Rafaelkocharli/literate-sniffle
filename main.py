from flask import Flask, request
import json

from helper import getEntityByField, handleParams

app = Flask(__name__)


@app.route('/сommunities/')
def community():
    [field, value] = handleParams(request.values)
    with open('db/communities.json') as f:
        table = json.load(f)
        if field:
            data = getEntityByField(table, field, value) or {}
        else:
            data = table
        return data

@app.route('/posts/')
def post():
    [field, value] = handleParams(request.values)
    with open('db/posts.json') as f:
        table = json.load(f)
        if field:
            data = getEntityByField(table, field, value) or {}
        else:
            data = table
        return {**data}
