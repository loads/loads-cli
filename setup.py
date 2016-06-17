import io
import os
import sys

from loads import __version__
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with io.open(os.path.join(here, 'README.md'), encoding='utf8') as f:
    README = f.read()
with io.open(os.path.join(here, 'CHANGELOG.md'), encoding='utf8') as f:
    CHANGES = f.read()

extra_options = {
    'packages': find_packages(),
}


setup(name='loads',
      version=__version__,
      description='Interactive tool for running loads-broker loadtests',
      long_description=README + '\n\n' + CHANGES,
      classifiers=['Topic :: Software Development :: Quality Assurance',
                   'Topic :: Software Development :: Testing',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.4'
                   ],
      keywords='[testing, load-testing, loadtest]',
      author='Mozilla Cloud Services',
      author_email='cloud-services-qa@mozilla.org',
      license='MPL2',
      include_package_data=True,
      zip_safe=False,
      entry_points='''
      [console_scripts]
      loads-cli = loads.main:main
      ''',
      **extra_options
      )
