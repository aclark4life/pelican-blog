Virtualenv Support Update
=========================

:date: 2014-03-19 17:30
:tags: Django, Plone, Python

.. image:: /images/virtualenv-support-update.jpg
    :alt: alternate text

This is you: I **use virtualenv all the time and I love it!** But I hate having to manually upgrade setuptools within my virtualenvs because the `PyPA has been so prolific with setuptools releases lately <https://pypi.python.org/pypi/setuptools#changes>`_.

Actually this is me, but it may be you too. If this is you, you may be familiar with the following process. If not, you may want to be.

Virtualenv and setuptools
-------------------------

When a virtualenv is created, virtualenv installs setuptools from a local distribution located in ``site-packages/virtualenv_support``. If that setuptools is out of date, so is the setuptools in your new virtualenv. To avoid having to manually upgrade setuptools within newly created virtualenvs, you can do this::

    $ cd /usr/local/lib/python2.7/site-packages/virtualenv_support
    $ curl -O https://pypi.python.org/packages/source/s/setuptools/setuptools-3.3.zip

Et voila!

::

    $ virtualenv .
    New python executable in ./bin/python2.7
    Also creating executable in ./bin/python
    Installing setuptools, pip...done.

::

    $ bin/pip show setuptools
    ---
    Name: setuptools
    Version: 3.3
    Location: /private/var/folders/1k/fmmlqcfn5jsbcqrqsw3q_slm0000gn/T/tmpE4vB1l/lib/python2.7/site-packages
    Requires: 

If you are a Buildout user, this should save you **endless frustration with Buildout attempting to upgrade Setuptools…**

attempting to upgrade Setuptools…

attempting to upgrade Setuptools…

attempting to upgrade Setuptools…
