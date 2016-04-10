<center><img src="https://raw.githubusercontent.com/prodicus/plino/gh-pages/images/logo_2.png?token=AEdMBkvEtWYtyO50OjnlksEt5Qpslm4Yks5XEPPKwA%3D%3D"></center>

> An intelligent spam filtering system built using a **custom Naive Bayes classifier**

**:arrow_forward: You can try it out here at [https://plino.heroku.com/](https://plino.heroku.com/)**

>This app is based directly on the work I did on [https://github.com/prodicus/spamfilter](https://github.com/prodicus/spamfilter)

***

## Table of contents

- [Demo](#demo)
- [REST API usage](#rest-api-usage)
    - [using `curl`](#using-curl)
    - [using `requests` (python)](#using-requests)
    - [using standard python 3 library](#using-standard-python-3-library)
- [Technologies used](#technologies-used)
    - [Backend](#backend)
    - [Front end](#front-end)
- [Contributing](#contributing)
    - [Installing it locally](#installing-it-locally)
    - [Running it](#running-it)
    - [Contributers](#contributers)
- [FAQ](#faq)
    - [What is the classifier based on](#what-is-the-classifier-based-on)
    - [What did you train the classifier on](#what-did-you-train-the-classifier-on)
    - [How accurate is it](#how-accurate-is-it)
- [Roadmap](#roadmap)
- [Legal stuff](#legal-stuff)

***

## Demo
[:arrow_up: Back to top](#table-of-contents)


<center><img src="http://i.imgur.com/Z7Xvc4H.jpg"></center>

<center><img src="http://i.imgur.com/WXUc9ug.jpg"></center>

<center><img src="http://i.imgur.com/Zj96Iul.jpg"></center>

<center><img src="http://i.imgur.com/D0kb3JF.jpg"></center>

<center><img src="http://i.imgur.com/B0obsB5.jpg"></center>

***

For more screenshots

| Desktop view | Mobile View |
|:--:|:--:|
|[desktop demo screens](http://imgur.com/a/w6gbj) | [mobile demo screens](http://imgur.com/a/eI5sp) |

***

## REST API usage
[:arrow_up: Back to top](#table-of-contents)

Yes, we do provide an **API** for our service!

#### using `curl`


```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"email_text":"<YOUR EMAIL TEXT>"}' http://plino.heroku.com/api/v1/classify/
```

**Show me an example**

You thought I was lying!

```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"email_text":"Dear Tasdik, I would like to immediately transfer 10000 thousand dollars to your account as my beloved husband has expired and I have nobody to ask for to transfer the money to your account. I come from the family of the royal prince of burkino fasa and I would be more than obliged to take your help on this matter. Would you care to share your bank account details with me in the next email conversation that we have? -regards -Liah herman"}' http://plino.heroku.com/api/v1/classify/
HTTP/1.1 200 OK
Server: gunicorn/19.4.5
Date: Sat, 09 Apr 2016 14:15:49 GMT
Connection: close
Content-Type: application/json
Content-Length: 507

{
  "email_class": "spam", 
  "email_text": "Dear Tasdik, I would like to immediately transfer 10000 thousand dollars to your account as my beloved husband has expired and I have nobody to ask for to transfer the money to your account. I come from the family of the royal prince of burkino fasa and I would be more than obliged to take your help on this matter. Would you care to share your bank account details with me in the next email conversation that we have? -regards -Liah herman", 
  "status": 200
}
```

#### using `requests`
[:arrow_up: Back to top](#table-of-contents)

How can we forget our beloved [`requests`](https://github.com/kennethreitz/requests) module!

```python
>>> import requests
>>> import json
>>> api_url = "http://plino.heroku.com/api/v1/classify/"
>>> payload = {'email_text': 'Dear Tasdik, I would like to immediately transfer 10000 thousand dollars to your account as my beloved husband has expired and I have nobody to ask for to transfer the money to your account. I come from the family of the royal prince of burkino fasa and I would be more than obliged to take your help on this matter. Would you care to share your bank account details with me in the next email conversation that we have? -regards -Liah herman'}
>>> headers = {'content-type': 'application/json'}
>>> response = requests.post(api_url, data=json.dumps(payload), headers=headers)
>>> response.status_code
200
>>> json_data = response.json()
>>> json_data['email_text']
u'Dear Tasdik, I would like to immediately transfer 10000 thousand dollars to your account as my beloved husband has expired and I have nobody to ask for to transfer the money to your account. I come from the family of the royal prince of burkino fasa and I would be more than obliged to take your help on this matter. Would you care to share your bank account details with me in the next email conversation that we have? -regards -Liah herman'
>>> json_data['email_class']
u'spam'
>>>
```

#### Using standard python 3 library
[:arrow_up: Back to top](#table-of-contents)

[requests module](https://github.com/kennethreitz/requests) really makes our life easy and I use it all the time. But **sigh**, there should be an example using the standard library so here it is

```python
>>> import urllib.request
>>> import json
>>>
>>> url = "http://plino.heroku.com/api/v1/classify/"
>>> req = urllib.request.Request(url)
>>> req.add_header('Content-Type', 'application/json; charset=utf-8')
>>>
>>> body = {'email_text': 'Dear Tasdik, I would like to immediately transfer 10000 thousand dollars to your account as my beloved husband has expired and I have nobody to ask for to transfer the money to your account. I come from the family of the royal prince of burkino fasa and I would be more than obliged to take your help on this matter. Would you care to share your bank account details with me in the next email conversation that we have? -regards -Liah herman'}
>>> jsondata = json.dumps(body)
>>>
>>> jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
>>> req.add_header('Content-Length', len(jsondataasbytes))
>>>
>>> print (jsondataasbytes)
b'{"email_text": "Dear Tasdik, I would like to immediately transfer 10000 thousand dollars to your account as my beloved husband has expired and I have nobody to ask for to transfer the money to your account. I come from the family of the royal prince of burkino fasa and I would be more than obliged to take your help on this matter. Would you care to share your bank account details with me in the next email conversation that we have? -regards -Liah herman"}'
>>>
>>> with urllib.request.urlopen(req, jsondataasbytes) as f:
...   print(f.read().decode('utf-8'))
...
{
  "email_class": "spam",
  "email_text": "Dear Tasdik, I would like to immediately transfer 10000 thousand dollars to your account as my beloved husband has expired and I have nobody to ask for to transfer the money to your account. I come from the family of the royal prince of burkino fasa and I would be more than obliged to take your help on this matter. Would you care to share your bank account details with me in the next email conversation that we have? -regards -Liah herman",
  "status": 200
}
>>>
```

***

## Technologies used
[:arrow_up: Back to top](#table-of-contents)

Built upon the giant shoulders of (__in no particular order__)

#### Backend

- [Flask](http://flask.pocoo.org/) because __I ♥ `Flask` more than [`Django`](https://www.djangoproject.com/)__
- [Flask-Cache](https://pythonhosted.org/Flask-Cache/) for **caching**
- [nltk](http://nltk.org) for text pre-processing
- [gunicorn](http://gunicorn.org/) as the production server
- [Jinja2](http://jinja.pocoo.org/) as the templating engine
- [dill](https://pypi.python.org/pypi/dill) for de-serializing complex python objects

[and some more](https://github.com/prodicus/plino/blob/master/requirements.txt)

#### Front end

- [MaterializeCSS](http://materializecss.com/)
- [Jquery](https://jquery.com/)
- [WowJS](https://github.com/matthieua/WOW)

***

## Contributing
[:arrow_up: Back to top](#table-of-contents)

#### Installing it locally

```bash
$ virtualenv venv              # Create virtual environment
$ source venv/bin/activate     # Change default python to virtual one
(venv)$ git clone https://github.com/prodicus/plino.git
(venv)$ cd plino 
(venv)$ pip install -r requirements.txt
```

#### Running it

```sh
$ make run
```

**Refer [CONTRIBUTING.md](https://github.com/prodicus/plino/blob/master/CONTRIBUTING.md) for detailed reference**

#### Contributers

- [Nitesh Sharma (sinscary)](https://github.com/sinscary) : **UI dev**

***

## FAQ
[:arrow_up: Back to top](#table-of-contents)

#### What is the classifier based on 

This repo is build directly on the work I did on [prodicus/spamfilter](https://github.com/prodicus/spamfilter)

#### What did you train the classifier on

The pickled classifier was trained against a total of close to **33,000** emails picked from publicly available [enron dataset](https://www.cs.cmu.edu/~./enron/). You can find the `full_corpus` directory, which holds the training emails [here](https://github.com/prodicus/spamfilter/tree/master/data)

#### How accurate is it

I will leave that to you to decide upon. But for the questions sake, decent enough! :smile:

***

## Roadmap
[:arrow_up: Back to top](#table-of-contents)

- [x] Deploying to heroku
- [x] Creating a REST API
- [x] Improving the UI
- [ ] Simple API authentication
- [ ] Writing tests

***

## Legal Stuff
[:arrow_up: Back to top](#table-of-contents)

Licensed under [GNU GPLv3](https://github.com/prodicus/alice/tree/master/LICENSE)

    plino: A spam filtering system
    Copyright (C) 2016  Tasdik Rahman

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

You can find the full copy of the `LICENSE` [here](https://github.com/prodicus/alice/tree/master/LICENSE)