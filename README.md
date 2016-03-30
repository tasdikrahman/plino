## Alice
    
An intelligent spam filtering system built using a custom Naive Bayes classifier

<!-- <p align="center">
    <img width="320" src="http://i.imgur.com/TPXlkCH.jpg">
</p>
 -->

***

### Installing

```sh
$ git clone https://github.com/prodicus/alice && cd alice
$ pip install -r requirements.txt
$ make run
```

Opens the app on [http://localhost:8000](http://localhost:8000)

**Watch and lay back!**

## Screenshots

<center><p><strong>Ham Mail</strong></p></center>

<center><img src="http://i.imgur.com/5dUkBDp.jpg"></center>


***

<center><p><strong>Spam Mail</strong></p></center>

<center><img src="http://i.imgur.com/v0dEJZj.jpg"></center>

## Technologies used

Built upon the giant shoulders of (__in no particular order__)

#### Backend

- [Flask](http://flask.pocoo.org/)
- [beautifulsoup4](http://www.crummy.com/software/BeautifulSoup/)
- [dill](https://pypi.python.org/pypi/dill)
- [itsdangerous](https://pypi.python.org/pypi/itsdangerous)
- [Jinja2](jinja.pocoo.org/)
- [MarkupSafe](www.pocoo.org/projects/markupsafe/)
- [nltk](http://nltk.org)
- [tabulate](https://bitbucket.org/astanin/python-tabulate)
- [Werkzeug](werkzeug.pocoo.org/)

#### Front end

- [Bootstrap](http://getbootstrap.com)
- [Jquery](https://jquery.com/)

## Development

- __This repo only holds the flask app for the [prodicus/spamfilter](https://github.com/prodicus/spamfilter)__
- The pickled classifier was trained against a total of close to **33,000** emails.

## Legal Stuff

Licensed under [GNU GPLv3](https://github.com/prodicus/alice/tree/master/LICENSE)
