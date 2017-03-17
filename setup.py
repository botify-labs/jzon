# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='jzon',
    version='0.4.2',
    py_modules=['jzon'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        jzon=jzon:jzon
    ''',
    author='Yves Bastide',
    author_email='yves@botify.com',
    description='JSON Dumper',
    license='MIT',
    url='https://github.com/botify-labs/jzon',
)
