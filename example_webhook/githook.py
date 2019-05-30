#!/usr/bin/env python3
from flask import Flask, request, jsonify
from pprint import pprint

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    github_info = request.get_json()
    print('-' * 10 + ' Headers ' + '-' * 10)
    pprint(request.headers, indent=4)
    print('-' * 10 + ' Payload ' + '-' * 10)
    pprint(github_info, indent=4)
    return jsonify(True)
