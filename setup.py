# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in msmr/__init__.py
from msmr import __version__ as version

setup(
	name='msmr',
	version=version,
	description='all about msmr.ch',
	author='Joel Mesmer',
	author_email='joel@msmr.ch',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
