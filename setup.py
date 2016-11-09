from setuptools import setup, find_packages
import sys

version = '1.0.0'

requires = ['six']
if sys.version_info[0] == 2:
    if sys.version_info[1] in (4, 5):
        requires.append('simplejson < 2.0.10')

setup(name='randomclone',
      version=version,
      install_requires=requires,
      packages=find_packages(exclude=['ez_setup']),
      include_package_data=True,
      zip_safe=True,
      entry_points="""
        [console_scripts]
        randomc = randomclone.cli:main
      """,
      )
