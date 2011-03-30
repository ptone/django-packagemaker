Django Packagemaker
===================

django-packagemaker is aimed at making it much easier to quickly scaffold
a python package for a django reusable app. It tries to find a balance between
respecting individual choices and being opinionated enough to be useful.

To this end it is more than just a paster template of Django's startapp output.
It creates things like an admin.py file, docs with sphinx-quickstart pre-run
etc.

Getting started
---------------

Install django-packagemaker with pip::

    $ pip install git+git://github.com/ptone/django-packagemaker.git#egg=django_paster

[NOTE: For now, this project itself is not yet on PyPi until more stable]

This will also install the dependencies for using the paster command

Note if you are using virtualenv (and you should be) that due to some
limitation of paste script, the paster packages must be installed in the same
virtualenv as django-packagemaker. If you are using pip's cache (and you should
be) this isn't too bad a speed hit on your virtualenv buildout.

That means if you have paste script already installed in your system
site-packages, you are likely to run into some troubles.

After installation, you can run::

    $ paster create -t app_package coolapp

This will prompt you for several pieces of information about your package, hit
return to accept the defaults. If you have git configured, it will attempt to
read your git config for your name and email. The result will be a directory
with this layout::

    coolapp
    coolapp/coolapp
    coolapp/coolapp/__init__.py
    coolapp/coolapp/admin.py
    coolapp/coolapp/forms.py
    coolapp/coolapp/models.py
    coolapp/coolapp/templates
    coolapp/coolapp/templates/coolapp
    coolapp/coolapp/tests.py
    coolapp/coolapp/urls.py
    coolapp/coolapp/views.py
    coolapp/docs
    coolapp/docs/_build
    coolapp/docs/_static
    coolapp/docs/_templates
    coolapp/docs/conf.py
    coolapp/docs/index.rst
    coolapp/docs/make.bat
    coolapp/docs/Makefile
    coolapp/LICENSE.txt
    coolapp/MANIFEST.in
    coolapp/README.rst
    coolapp/setup.py

If you just want to then include this in your local development virtualenv, you
need only::

    $ pip install -e /path/to/coolapp

This will install the app, but allows you to continue to make changes to it in
its own src location.

If you install the excellent `hub <https://github.com/defunkt/hub>`_ git
extension, you can then easily ``git create`` from inside your app, and you now
have a github repo for your project.
