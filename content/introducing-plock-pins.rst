Introducing Plock Pins
======================

:date: 2014-03-20 21:15
:tags: Plone, Python

.. image:: /images/buildout-all-the-plones.jpg
    :alt: alternate text

::

    "Plock Pins are the greatest thing to happen to Plone since Buildout"

                                                            — Alex Clark

Plock Pins are the final incarnation of a collection of Plone Buildouts I've been developing since 2010. They attempt to make it easy to install Plone with only Python installed [1]_. Installing Plone with Plock Pins looks like this::

    $ virtualenv-2.7 .
    $ bin/pip install zc.buildout
    $ bin/buildout init

Now edit your ``buildout.cfg`` to include a link to the Plock Pins::

    [buildout]
    extends = https://raw.github.com/plock/pins/master/plone-4-3

Then run Buildout::

    $ bin/buildout

Followed by the following command to start Plone::

    $ bin/plone fg

That's it! This technique should work for all versions of Plone all the way back to Plone 1.1. If it doesn't, please let me know here:

- https://github.com/plock/pins/issues

Finally, here is a list of all available Plock Pins you can extend [2]_:

- https://raw.github.com/plock/pins/master/plone-4-3
- https://raw.github.com/plock/pins/master/plone-4-2
- https://raw.github.com/plock/pins/master/plone-4-1
- https://raw.github.com/plock/pins/master/plone-4-0
- https://raw.github.com/plock/pins/master/plone-3-3
- https://raw.github.com/plock/pins/master/plone-3-2
- https://raw.github.com/plock/pins/master/plone-3-1
- https://raw.github.com/plock/pins/master/plone-3-0
- https://raw.github.com/plock/pins/master/plone-2-5
- https://raw.github.com/plock/pins/master/plone-2-1
- https://raw.github.com/plock/pins/master/plone-1-1

.. [1] In future versions of Python 3.x, the Pip installer will be included as part of the core software. This will lessen the burden for users attempting to install packages from PyPI. In 2.x, one must install Setuptools and/or Pip before attempting to do so.

.. [2] Remember to use Python 2.4 for < Plone 4
