## plino
    
An intelligent spam filtering system built using a `custom Naive Bayes classifier`

**:arrow_forward: You can try it out here at [https://plino.heroku.com/](https://plino.heroku.com/)**

>This app is based on the work I did on [https://github.com/prodicus/spamfilter]


***

## Table of contents

- [Screenshots](#screenshots)
- [Technologies used](#technologies-used)
    - [Backend](#backend)
    - [Front end](#front-end)
- [Development](#development)
    - [Installing it locally](#installing-it-locally)
    - [Running it](#running-it)
    - [How accurate is it](#how-accurate-is-it)
- [FAQ](#faq)
    - [What is the classifier based on](#what-is-the-classifier-based-on)
    - [What did you train the classifier on](#what-did-you-train-the-classifier-on)
- [Roadmap](#roadmap)
- [Legal stuff](#legal-stuff)

***

## Screenshots
[:arrow_up: Back to top](https://github.com/prodicus/plino#plino)

### For Ham Mail

<center><img src="http://i.imgur.com/5dUkBDp.jpg"></center>


***

### For Spam Mail

<center><img src="http://i.imgur.com/v0dEJZj.jpg"></center>

***

## Technologies used
[:arrow_up: Back to top](https://github.com/prodicus/plino#plino)

Built upon the giant shoulders of the following awesome (__in no particular order__)

#### Backend

- [Flask](http://flask.pocoo.org/)
- [nltk](http://nltk.org)
- [gunicorn](http://gunicorn.org/) as the production server
- [beautifulsoup4](http://www.crummy.com/software/BeautifulSoup/)
- [dill](https://pypi.python.org/pypi/dill)
- [itsdangerous](https://pypi.python.org/pypi/itsdangerous)
- [Jinja2](jinja.pocoo.org/)
- [MarkupSafe](www.pocoo.org/projects/markupsafe/)
- [tabulate](https://bitbucket.org/astanin/python-tabulate)
- [Werkzeug](werkzeug.pocoo.org/)

#### Front end

- [Bootstrap](http://getbootstrap.com)
- [Jquery](https://jquery.com/)

***

## Development
[:arrow_up: Back to top](https://github.com/prodicus/plino#plino)

#### Installing it locally

```sh
$ git clone https://github.com/prodicus/plino && cd plino
$ pip install -r requirements.txt
```

#### Running it

```sh
$ make run
```

***

## FAQ
[:arrow_up: Back to top](https://github.com/prodicus/plino#plino)

#### What is the classifier based on 

This repo is build directly on the work I did on [prodicus/spamfilter](https://github.com/prodicus/spamfilter)

#### What did you train the classifier on

The pickled classifier was trained against a total of close to **33,000** emails picked from publicly available [enron dataset](https://www.cs.cmu.edu/~./enron/)

#### How accurate is it

I will leave that to you to decide upon. But for the questions sake, decent enough! :smile:

***

## Roadmap
[:arrow_up: Back to top](https://github.com/prodicus/plino#plino)

- [x] Deploying to heroku
- [ ] Improving the UI
- [ ] Writing tests
- [ ] Creating an REST API

***

## Legal Stuff
[:arrow_up: Back to top](https://github.com/prodicus/plino#plino)

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

