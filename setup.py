#!/usr/bin/env python

from distutils.core import setup
from urlparse import urljoin
from glob import glob

execfile('info.py')

setup(name='tauperfmon',
      version=__VERSION__,
      author='Noel Dawe',
      author_email='noel.dawe@cern.ch',
      url=__URL__,
      description='ATLAS tau performance monitoring tool',
      long_description=open('README.rst').read(),
      download_url=urljoin(__URL__, "tauperfmon-%s.tar.gz" % __VERSION__),
      license='GPLv3',
      py_modules=['tauperfmon'],
      requires=['yaml'],
      scripts=glob('scripts/*'),
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Utilities",
        "Operating System :: POSIX :: Linux",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License (GPL)"
      ]
    )
