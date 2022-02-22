#!/usr/bin/env python3
import setuptools 

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='fstringlt36',
    packages=['fstringlt36'],
    version='0.0.3',
    description='Python f-strings for before Python3.6',
    license='MIT',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author = 'Mendelsshop',
    author_email = 'mendelsshop@gmail.com',
    url = 'https://github.com/mendelsshop/fstringlt36/',
    project_urls = {
        'Bug Tracker': 'https://github.com/mendelsshop/fstringlt36/issues'
    },

    install_requires=[''],
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
        ]
    )

