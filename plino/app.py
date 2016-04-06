# -*- coding: utf-8 -*-
# @Author: Tasdik Rahman
# @Date:   2016-03-30
# @Last Modified by:   Tasdik Rahman
# @Last Modified time: 2016-04-06 15:51:37
# @MIT License
# @http://tasdikrahman.me
# @https://github.com/prodicus

import os
import logging
import sys

from flask import Flask , jsonify, render_template, request
import dill
import bs4

app = Flask(__name__)

# for debugging purposes
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

APP = os.path.abspath(__file__)
APP_DIR, APP_NAME = os.path.split(APP)

classifier_file_path = os.path.join(APP_DIR, 'saved_classifiers', 'spam_classifier.pickle')
classifier_file = open(classifier_file_path, 'rb')
classifier_object = dill.load(classifier_file)
classifier_file.close()

trainer_file_path = os.path.join(APP_DIR, 'saved_classifiers', 'trainer.pickle')
trainer_file = open(trainer_file_path, 'rb')
trainer_object = dill.load(trainer_file)
trainer_file.close()

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/api/classify',methods=['POST'])
def classify():
    # get the input text email
    email_text = request.form['message']

    try:
        # === Preprocessing ==== #
        email_text = bs4.UnicodeDammit.detwingle(
            email_text).decode('utf-8')
        email_text = email_text.encode('ascii', 'ignore')
        # ====================== #

        hamorspam = classifier_object.classify(
                        trainer_object.extract_features(email_text)
                    )
        response = {'category': hamorspam, 'status': 'ok'}

        # anything printed to the STDOUT will be stored in heroku's logs
        print "TEXT: '{0}' :: RESPONSE : '{1}'".format(     
                    email_text.replace("\n", " ").replace("\r", " "),     
                    hamorspam
                )

        return jsonify(response)
    except UnicodeEncodeError:
        hamorspam = 'UnicodeEncodeError'
        response = {'category': hamorspam, 'status': 'error'}
        return jsonify(response)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
        
if __name__ == "__main__":
    app.run(debug=True)