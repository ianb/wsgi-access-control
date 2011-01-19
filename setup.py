from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='wsgi-access-control',
      version=version,
      description="Add Access-Control-Allow-Origin etc headers to WSGI apps",
      long_description="""\
This provides middleware that adds Access-Control-\\* headers to an
application to allow `cross-origin resource sharing <http://www.w3.org/TR/cors/>`_.
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='wsgi cors xmlhttprequest',
      author='Ian Bicking',
      author_email='ianb@mozilla.com',
      url='http://github.com/ianb/wsgi-access-control',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      zip_safe=False,
      install_requires=[
        ## Nothing so far
      ],
      )
