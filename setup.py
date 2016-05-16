"""
Flask-CLI
--------------

Support for writing command-line interfaces to web services.

Links
`````

* `documentation <http://flask-script.readthedocs.org>`_


"""
import sys
from setuptools import setup

version='0.2.0'

# Hack to prevent stupid TypeError: 'NoneType' object is not callable error on
# exit of python setup.py test # in multiprocessing/util.py _exit_function when
# running python setup.py test (see
# https://github.com/pypa/virtualenv/pull/259)
try:
    import multiprocessing
except ImportError:
    pass

install_requires = ['Flask',
        'six']

setup(
    name='Flask-CLI',
    version=version,
    url='http://github.com/bunnyblanco/flask-cli',
	download_url = 'https://github.com/bunnyblanco/flask-cli/tarball/v'+version,
    license='BSD',
    author='Bruce C. Paul',
    author_email='bruce.c.paul@gmail.com',
    description='Command-line interface for Flask',
    long_description=__doc__,
    packages=[
        'flask_cli'
    ],
    zip_safe=False,
    install_requires=install_requires,
    tests_require=[
        'pytest',
    ],
    platforms='any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
