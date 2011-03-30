# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

pkg_name = "django_paster"
version = "0.1.0"
setup(
    name = pkg_name,
    # version = __import__(pkg_name).__version__,
    version=version,
    description='Paster templates for Django work',
    long_description=README,
    author='Preston Holmes',
    author_email='preston@ptone.com',
    url='http://www.ptone.com',
    license='BSD',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Paste",
    ],
    # packages=find_packages(),
    packages = find_packages('src'),
    package_dir = {'':'src'},
    include_package_data=True,
    install_requires=[
        "Paste",
        "PasteScript",
    ],
    zip_safe=False,
    entry_points="""
      [paste.paster_create_template]
      app_package = django_paster.pastertemplates:DjangoAppTemplate
      """,
)
