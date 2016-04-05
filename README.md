## plino
    
An intelligent spam filtering system built using a `custom Naive Bayes classifier`

**:arrow_forward: You can try it out here at [https://plino.heroku.com/](https://plino.heroku.com/)**

>This app is based directly on the work I did on [https://github.com/prodicus/spamfilter](https://github.com/prodicus/spamfilter)


***

## Table of contents

- [Demo](#demo)
- [Technologies used](#technologies-used)
    - [Backend](#backend)
    - [Front end](#front-end)
- [Contributing](#contributing)
    - [Installing it locally](#installing-it-locally)
    - [Running it](#running-it)
- [FAQ](#faq)
    - [What is the classifier based on](#what-is-the-classifier-based-on)
    - [What did you train the classifier on](#what-did-you-train-the-classifier-on)
    - [How accurate is it](#how-accurate-is-it)
- [Roadmap](#roadmap)
- [Legal stuff](#legal-stuff)

***

## Demo
[:arrow_up: Back to top](https://github.com/prodicus/plino#plino)

### For Ham Mail

<center><img src="http://i.imgur.com/5dUkBDp.jpg"></center>


***

### For Spam Mail

<center><img src="http://i.imgur.com/v0dEJZj.jpg"></center>

***

## Technologies used
[:arrow_up: Back to top](https://github.com/prodicus/plino#plino)

Built upon the giant shoulders of (__in no particular order__)

#### Backend

- [Flask](http://flask.pocoo.org/) as `Django` would have been an overkill for this!
- [nltk](http://nltk.org) for text pre-processing
- [gunicorn](http://gunicorn.org/) as the production server
- [beautifulsoup4](http://www.crummy.com/software/BeautifulSoup/) for handling unicode issues
- [Jinja2](jinja.pocoo.org/) as the templating engine
- [dill](https://pypi.python.org/pypi/dill) for de-serializing complex python objects

[and some more](https://github.com/prodicus/plino/blob/master/requirements.txt)

#### Front end

- [Bootstrap](http://getbootstrap.com)
- [Jquery](https://jquery.com/)

***

## Contributing
[:arrow_up: Back to top](https://github.com/prodicus/plino#plino)

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

***

## FAQ
[:arrow_up: Back to top](https://github.com/prodicus/plino#plino)

#### What is the classifier based on 

This repo is build directly on the work I did on [prodicus/spamfilter](https://github.com/prodicus/spamfilter)

#### What did you train the classifier on

The pickled classifier was trained against a total of close to **33,000** emails picked from publicly available [enron dataset](https://www.cs.cmu.edu/~./enron/). You can find the `full_corpus` directory, which holds the training emails [here](https://github.com/prodicus/spamfilter/tree/master/data)

#### How accurate is it

I will leave that to you to decide upon. But for the questions sake, decent enough! :smile:

***

## Roadmap
[:arrow_up: Back to top](https://github.com/prodicus/plino#plino)

- [x] Deploying to heroku
- [ ] Improving the UI
- [ ] Writing tests
- [ ] :soon: Creating an REST API

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

