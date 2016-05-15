# -*- coding: utf-8 -*-
# @Author: Tasdik Rahman
# @Date:   2016-03-30
# @Last Modified by:   Sahil Dua
# @Last Modified time: 2016-05-15 06:20:03
# @MIT License
# @http://tasdikrahman.me
# @https://github.com/prodicus

import logging
import sys

from flask import Flask, jsonify, render_template, request, abort
from flask.ext.cache import Cache

from utils import ham_or_spam

app = Flask(__name__)

# defining the app settings for caching
# TODO: use 'memcache' or 'redis' later than using the browser inmemory
app.config['CACHE_TYPE'] = 'simple'
app.cache = Cache(app)

# for debugging purposes
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)


@app.route('/')
@app.route('/index')
@app.cache.cached(timeout=300)
def index():
    return render_template('index.html', title='Home')


@app.route('/api/classify', methods=['POST'])
def classify():
    # get the input text email
    email_text = request.form['message']
    return jsonify(ham_or_spam(email_text))


@app.errorhandler(404)
@app.cache.cached(timeout=300)
def page_not_found(error):
    return render_template('404.html', title='Page not found'), 404


# REST API v1
@app.route('/api/v1/classify', methods=['POST'])
@app.route('/api/v1/classify/', methods=['POST'])
def api_v1():
    if not request.json or not 'email_text' in request.json:
        abort(400)

    email_class = ham_or_spam(request.json['email_text'])["category"]
    json_data = {
        'status': 200,
        'email_text': request.json['email_text'],
        'email_class': email_class
    }

    return jsonify(json_data), 200


if __name__ == "__main__":
    app.run()
