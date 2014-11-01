Plone 5 Alpha 2 is here!
========================

:date: 2014-06-18 08:00
:tags: Plone, Python

*This post is long overdue since Plone 5 alpha 2 was released on 2014-04-20! It is also too short. I may do a followup blog entry to review more features, depending on how well this one is received. I also want to talk more about Plock.*

When Plone 4 alpha 1 was released, I was so excited I immediately `ran it in production <http://blog.aclark.net/2012/10/03/plone-4-3-alpha-1-in-production/>`_. Now-a-days I use `Pyramid for aclark.net <http://blog.aclark.net/2013/04/22/new-pyramid-site/>`_ but I still get excited about new Plone releases.

As such, I finally got around to testing the latest Plone 5 alpha with `my deployment stack <http://blog.aclark.net/2014/03/20/introducing-plock-pins/>`_ and the results were very impressive, so I thought I'd share.

Hosted configuration
--------------------

Because of the "muscle memory" I've built up over the years doing this, I always install Plone in development and production via my `hosted configuration files <https://github.com/plock/pins>`_. If you are not a developer you may instead prefer the `Unified Installer, VirtualBox/Vagrant installer or OS X Lion/Mountain Lion/Mavericks Binary Installer <http://plone.org/products/plone/releases/5.0>`_ otherwise follow along [1]_:

::

    $ pip install tmp virtualenv
    $ cd `tmp`
    $ virtualenv .
    $ bin/pip install zc.buildout
    $ bin/buildout init

Edit ``buildout.cfg`` to contain::

    [buildout]
    extends = https://raw.github.com/plock/pins/master/plone-5-0

Run Buildout and start Plone::

    $ bin/buildout
    $ bin/plone fg

Create Plone Site
-----------------

The first thing you will notice is the improved "Create a Plone Site" page which now includes a timezone configuration option:

.. image:: /images/plone-5-screen-0.png
    :alt: Plone 5

Barceloneta Theme
-----------------

I selected the ``US/Eastern`` timezone and clicked ``Create Plone Site``, shortly after which I was greeted with a beautiful new Plone 5 site in all its open source glory. Immediately you will notice a new theme and toolbar:

.. image:: /images/plone-5-screen-1.png
    :alt: Plone 5

Plone Toolbar
-------------

Here is a quick tour of the new toolbar.

.. image:: /images/plone-5-screen-1.png
    :alt: Plone 5

Folder contents
~~~~~~~~~~~~~~~
.. image:: /images/plone-5-screen-2.png
    :alt: Plone 5

Edit button
~~~~~~~~~~~
.. image:: /images/plone-5-screen-3.png
    :alt: Plone 5

Sharing settings
~~~~~~~~~~~~~~~~
.. image:: /images/plone-5-screen-4.png
    :alt: Plone 5

Workflow settings
~~~~~~~~~~~~~~~~~
.. image:: /images/plone-5-screen-5.png
    :alt: Plone 5

Add content
~~~~~~~~~~~
.. image:: /images/plone-5-screen-6.png
    :alt: Plone 5

Layout settings
~~~~~~~~~~~~~~~
.. image:: /images/plone-5-screen-7.png
    :alt: Plone 5

User menu
~~~~~~~~~
.. image:: /images/plone-5-screen-8.png
    :alt: Plone 5

Love it! Of all these, only the eye icon didn't function as expected. Not sure what it's supposed to do but I assume it's not done yet. Additionally, I wish the small Plone logo in the toolbar navigated "home" like the portal logo. Or maybe it will close the toolbar? Oh, the possibilities!

Thanks
------

Many thanks to everyone who has worked hard to make Plone 5 a reality.

*You should probably* `hire me <http://aclark.net>`_ *or* `follow me on Twitter <http://twitter.com/aclark4life>`_ *or both*.

.. [1] And please try `Plock <http://plock.github.io>`_ which automates all of these steps e.g. ``pip install plock; plock .;bin/plone fg`` Once Plone (4) is installed, update the extends parameter in ``buildout.cfg`` to ``https://raw.github.com/plock/pins/master/plone-5-0`` and rerun Buildout.
