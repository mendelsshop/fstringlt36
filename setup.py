from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='f-string_lt_37',
    version='0.0.1',
    description='Python f-strings for before Python3.7',
    license='MIT',
    long_description=long_description,
    author = 'Mendelsshop',
    author_email = 'mendelsshop@gmail.com',
    url = 'https://github.com/mendelsshop/f-string_lt_37/tree/regex',
    packages=['f-string_lt_37'],
    install_requires=[]
)

