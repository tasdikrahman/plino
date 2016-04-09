# -*- coding: utf-8 -*-
# @Author: Tasdik Rahman
# @Date:   2016-03-30
# @Last Modified by:   Tasdik Rahman
# @Last Modified time: 2016-04-09 14:47:55
# @MIT License
# @http://tasdikrahman.me
# @https://github.com/prodicus

import logging
import sys

from flask import Flask , jsonify, render_template, request
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

@app.route('/about/')
@app.cache.cached(timeout=300)
def about(name = None):
	return render_template('about.html', title='About')

@app.route('/api/classify',methods=['POST'])
def classify():
    # get the input text email
    email_text = request.form['message']
    return jsonify(ham_or_spam(email_text))

@app.errorhandler(404)
@app.cache.cached(timeout=300)
def page_not_found(error):
    return render_template('404.html', title='Page not found'), 404
        
if __name__ == "__main__":
    app.run()
