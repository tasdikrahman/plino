# -*- coding: utf-8 -*-
# @Author: Tasdik Rahman
# @Date:   2016-03-30
# @Last Modified by:   Tasdik Rahman
# @Last Modified time: 2016-04-05 16:48:15
# @MIT License
# @http://tasdikrahman.me
# @https://github.com/prodicus

import os
import logging
import sys

from flask import Flask , jsonify, render_template, request
import dill
import bs4


logging.basicConfig(
    filename=os.path.join('logfiles', 'logfile.txt'),
    level=logging.DEBUG,
    filemode='w',
    format='%(asctime)s - %(levelname)s - %(message)s'
)

app = Flask(__name__)

# for debugging purposes
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

classifier_file = open('saved_classifiers/spam_classifier.pickle', 'rb')
classifier_object = dill.load(classifier_file)
classifier_file.close()

trainer_file = open('saved_classifiers/trainer.pickle', 'rb')
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
        return jsonify(response)
    except UnicodeEncodeError:
        hamorspam = 'UnicodeEncodeError'
        response = {'category': hamorspam, 'status': 'error'}
        return jsonify(response)
        
if __name__ == "__main__":
    app.run(debug=True)