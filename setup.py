from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='f-string_lt_36',
    version='0.0.3',
    description='Python f-strings for before Python3.7',
    license='MIT',
    long_description=long_description,
    author = 'Mendelsshop',
    author_email = 'mendelsshop@gmail.com',
    url = 'https://github.com/mendelsshop/f-string_lt_36',
    packages=['f-string_lt_36'],
    install_requires=['logging' ,'os', 'sys'],
    packages=find_packages(where='src'),
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
        ]
)

