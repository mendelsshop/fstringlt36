#!/usr/bin/env python3
import setuptools 

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='fstringlt36',
    version='0.0.3',
    description='Python f-strings for before Python3.6',
    license='MIT',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author = 'Mendelsshop',
    author_email = 'mendelsshop@gmail.com',
    url = 'https://github.com/mendelsshop/f-string_lt_36/',
    project_urls = {
        'Bug Tracker': 'https://github.com/mendelsshop/f-string_lt_36/issues'
    },

    install_requires=['fstringlt36'],
    package_dir={'': 'src'},
    packages=['fstringlt36.py'],
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
        ]
    )

