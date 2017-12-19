# gpiosvr
RESTful interfaces for Raspberry Pi GPIO


# Run an LED server
Create a module for Gunicorn.

**Example: `led_server.py`**

```python
from gpiosvr import led
from gpiozero import LED


pin_config = (('red', 5), ('yellow', 6), ('green', 13), )

application = led.create_server(pin_config=pin_config, led_factory=LED)  
```

Start the server with Gunicorn, using your desired options.

```bash
$ gunicorn -b 127.0.0.1:8000 led_server
```


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
