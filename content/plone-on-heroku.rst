Plone on Heroku
===============

:date: Sat Jun 27 19:09:24 EDT 2015
:tags: Plone, Python

*Dear Plone, welcome to 2015*

Picture it. The year 2014. I was incredibly moved and inspired by this blog entry: 

- http://www.niteoweb.com/blog/dear-plone-welcome-to-2014

Someone had finally done it. (`zupo <https://github.com/zupo>`_ in this case, kudos!) Someone had finally beat me to implementing the dream of ``git push heroku plone``. And I could not have been happier.

But something nagging would not let go: I still **didn't fully understand how the buildpack worked**. Today I'm happy to say: that nag is gone and I now fully understand how Heroku buildpacks work… thanks to… wait for it… a `buildpack for Plock <https://github.com/plock/buildpack>`_.

Plock Buildpack
---------------

There's a lot of the same things going on in both the `Plone Buildpack <https://github.com/plone/heroku-buildpack-plone>`_ and the `Plock Buildpack <https://github.com/plock/buildpack/blob/master/bin/compile>`_, with some exceptions.

Experimental
~~~~~~~~~~~~

The **Plock buildpack is highly experimental, still in development and possibly innovative**. Here's what it currently does:

- Configures Python user site directory in Heroku cache
- Installs setuptools in user site
- Installs pip in user site
- Installs Buildout in user site
- Installs Plone in user site
- Copies cache to build directory
- Installs a portion of "user Plone" (the Heroku app's buildout.cfg) in the build directory (not the cache)
- Relies on the app itself to install the remainder (the Heroku app's heroku.cfg). **Most importantly, the app runs Buildout which finishes quickly thanks to the cache & configures the port which is only available to the app (not the buildpack.)**

Here's `an example <https://github.com/ACLARKNET/plone-demo>`_:

::

    # buildout.cfg
    [buildout]
    extends = https://raw.github.com/plock/pins/master/plone-4-3

    [user]
    packages = collective.loremipsum

::

    # heroku.cfg
    [buildout]
    extends = buildout.cfg

    [plone]
    http-address = ${env:PORT}

::

    # Procfile
    web: buildout -c heroku.cfg; plone console

Opinionated
-----------

The Plock Buildpack is built on Plock, an "opinionated" installer for Plone. It may eventually use `Plock <https://pypi.python.org/pypi/plock/0.4.0>`_ itself, but currently only uses `Plock Pins <https://github.com/plock/pins>`_.
