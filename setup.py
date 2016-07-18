# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='py-postie',
    version='0.10',
    py_modules=['py-postie'],
    description='Utility to batch send emails and text messages',
    url='http://github.com/itsnauman/postie',
    author='Nauman Ahmad',
    author_email='nauman-ahmad@outlook.com',
    license='MIT',
    include_package_data=True,
    packages=['postie'],
    install_requires=[
        'mailthon',
        'twilio',
        'jinja2',
    ],
    entry_points='''
        [console_scripts]
        postie=postie.cli:main
    ''',
)
