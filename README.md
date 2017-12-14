# gpiosvr
RESTful interfaces for Raspberry Pi GPIO


# Setup dev environment
```bash
$ python -m venv venv
$ source venv/bin/activate
(venv) $ pip install -r requirements-dev.txt
```

# Run tests with HTML coverage report
```bash
(venv) $ pytest --cov=gpiosvr --cov-report=html
```
