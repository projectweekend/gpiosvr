from setuptools import setup


setup(
    name='gpiosvr',
    version='0.0.1',
    license='MIT',
    author='Brian Hines',
    author_email='brian@projectweekend.net',
    description='RESTful interfaces for Raspberry Pi GPIO',
    url='https://github.com/projectweekend/gpiosvr',
    packages=['gpiosvr'],
    py_modules=['gpiosvr'],
    python_requires='>=3',
    install_requires=[
        'falcon',
        'gpiozero',
        'gunicorn',
        'python-mimeparse',
        'six',
    ],
)
