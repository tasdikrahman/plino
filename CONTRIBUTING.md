## Contributing

This project is still a work in progress. Feel free to make a PR

- Fork it.

- Clone it

create a [virtualenv](http://pypi.python.org/pypi/virtualenv)

```bash
$ virtualenv venv              # Create virtual environment
$ source venv/bin/activate     # Change default python to virtual one
(venv)$ git clone https://github.com/prodicus/plino.git
(venv)$ cd plino
(venv)$ pip install -r requirements.txt
```

Or, if `virtualenv` is not installed on your system:

```bash
$ wget https://raw.github.com/pypa/virtualenv/master/virtualenv.py
$ python virtualenv.py venv    # Create virtual environment
$ source venv/bin/activate     # Change default python to virtual one
(venv)$ git clone https://github.com/prodicus/plino.git
(venv)$ cd plino
(venv)$ pip install -r requirements.txt
```

-  Create your feature branch

```bash
$ git checkout -b my-new-awesome-feature
```

-  Commit your changes

```bash
$ git commit -am 'Added <xyz> feature'
```

-  Make sure that your code Conforms to [PEP8](https://www.python.org/dev/peps/pep-0008/) and if everything is running fine, integrate your feature

- **Running the tests**

Plino uses `nosetests` to run its test suite. To run them

```bash
$ nosetests # inside the parent directory
```

-  Push to the branch

```bash
$ git push origin my-new-awesome-feature
```

- Create new [Pull Request](https://github.com/prodicus/plino/pull/new/master)

Hack away! :smile: