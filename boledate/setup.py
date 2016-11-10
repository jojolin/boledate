# Automatically created by: scrapyd-deploy

from setuptools import setup, find_packages

setup(
    name         = 'boledate',
    version      = '1.0',
    packages     = find_packages(),
    package_data = {
        '': ['*.txt'],
    },
    entry_points = {'scrapy': ['settings = boledate.setting']},
)
