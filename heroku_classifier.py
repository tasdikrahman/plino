# -*- coding: utf-8 -*-
# @Author: Tasdik Rahman
# @Date:   2016-03-30
# @Last Modified by:   Tasdik Rahman
# @Last Modified time: 2016-03-30 22:12:37
# @MIT License
# @http://tasdikrahman.me
# @https://github.com/prodicus

from flask import Flask , jsonify, render_template, request
import dill
import bs4

app = Flask(__name__)

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
    email_text = request.form['message']

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

if __name__ == "__main__":
    app.run(debug=True, port=8000)