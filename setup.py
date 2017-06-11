#!/usr/bin/env python

from distutils.core import setup

from rds import rds

setup(name='RemoteDirectorySync',
      version='0.1',
      description='Remote Directory Synchronization Tool',
      long_description=open('README.md').read(),
      author='Andrew Baumann',
      author_email='andrew.m.baumann@gmail.com',
      url='https://github.com/ambauma/RemoteDirectorySync',
      packages=['rds'],
      license='GPLv3'
      )
