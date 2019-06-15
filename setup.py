#!/usr/bin/env python

from setuptools import setup, find_packages


package_name = 'thisamericanlife'
tal_module_ref = __import__(package_name)

setup(
    name=package_name,
    version=tal_module_ref.__version__,
    description='scraper client for the This American Life website',
    author_email=tal_module_ref.__author_email__,
    url='https://github.com/{package_name}',
    packages=find_packages(exclude=['tests'])
)
