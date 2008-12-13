from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='mr.monkey',
      version=version,
      description="Provides tools for guerilla (monkey)-patching.",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Utilities",
        ],
      keywords='',
      author='Florian Schulze',
      author_email='florian.schulze@gmx.net',
      url='',
      license='BSD',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['mr'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
        # -*- Extra requirements: -*-
      ],
      test_suite='nose.collector',
      tests_require=[
        'nose',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
