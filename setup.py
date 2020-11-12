import os

import setuptools

module_path = os.path.join(os.path.dirname(__file__), 'flask_restx_patched/__init__.py')
version_line = [line for line in open(module_path)
                if line.startswith('__version__')][0]

__version__ = version_line.split('__version__ = ')[-1][1:][:-2]

setuptools.setup(
    name="flask-restx-patched",
    version=__version__,
    url="https://github.com/justinrubek/flask-restx-patched",

    author="Justin Rubek",
    author_email="justin@levitytech.net",

    description="Forked from flask-restplus-patched. Extends flask-restx so it can handle Marshmallow schemas and Webargs arguments.",
    long_description=open('README.md').read(),

    packages=['flask_restx_patched'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',

    install_requires=[
        'Flask', 'flask-restx', 'marshmallow', 'flask-marshmallow',
        'webargs', 'apispec'],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
    ],
)
