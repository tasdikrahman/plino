# -*- coding: utf-8 -*-
# @Author: Tasdik Rahman
# @Date:   2016-03-30
# @Last Modified by:   Tasdik Rahman
# @Last Modified time: 2016-04-06 18:17:36
# @MIT License
# @http://tasdikrahman.me
# @https://github.com/prodicus

import logging
import sys

from flask import Flask , jsonify, render_template, request

from plino.utils import ham_or_spam

app = Flask(__name__)

# for debugging purposes
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/api/classify',methods=['POST'])
def classify():
    # get the input text email
    email_text = request.form['message']
    return jsonify(ham_or_spam(email_text))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
        
if __name__ == "__main__":
    app.run(debug=True)