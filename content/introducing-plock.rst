Introducing Plock
=================

:date: 2013-07-19
:tags: Plone, Python

*Plock is a Plone Installer for the Pip-Loving Crowd. Plone is a Python-based CMS.*

Installing Plone with `Plock <https://github.com/aclark4life/plock>`_ looks like this::

    $ pip install plock
    $ bin/install-plone
    $ bin/plone fg

Configuration
-------------

Plone uses `Buildout <https://pypi.python.org/pypi/zc.buildout>`_ to manage its installation and configuration. Plock creates a ``buildout.cfg`` file for you that looks like this::

    [buildout]
    extends = https://raw.github.com/pythonpackages/buildout-plone/master/latest

    [plone]
    eggs +=
    # Add-ons go here e.g.:
    #    Products.PloneFormGen

Add-ons 
~~~~~~~

See https://pypi.python.org/pypi?:action=browse&show=all&c=563 for a complete list of add-ons compatible with Plone 4.3.

To install add-ons, add the desired Python package name(s) to the ``eggs +=`` parameter e.g.::

    [buildout]
    extends = https://raw.github.com/pythonpackages/buildout-plone/master/latest

    [plone]
    eggs +=
        Products.PloneFormGen

Stop Plone and run Buildout::

    $ bin/buildout

Start Plone::

    $ bin/plone fg

Install the add-on(s) in Plone via Site Setup -> Add-ons.
