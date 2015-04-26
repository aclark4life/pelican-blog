Plock Rocks
===========

:date: Sun Apr 26 11:37:21 EDT 2015
:tags: Plone, Python

.. image:: /images/plock-meme.png
    :alt: Plock Meme
    :align: center

*Plock is a Plone installer for the pip-loving crowd. Plone is the ultimate open source enterprise CMS.*

Understanding Plock
-------------------

To understand Plock you must understand a few things:

- The complexity of the Plone stack [1]_.
- My desire to simplify, clarify and reduce-to-bare-elements everything I touch.
- My willingness to mask complexity when eliminating it is not possible, despite the risk of contributing to it.

Pyramid author Chris McDonough [2]_ once made a comment a long time ago to the effect: "Let's stop piling more crap on top of Plone" and that sentiment still resonates today. That's why even though I love small and useful tools like Plock, it pains me to know what Plock is doing "under the hood" [7]_. Nevertheless, I felt compelled to write it and make it work well because not having it is even more painful. 

Before I tell you what Plock is [8]_, let me briefly describe what Plone is.

What is Plone, really?
----------------------

What is the complexity I mention above? Briefly, with as few loaded statements as possible:

- **Zope2** "application server". This is something you can ``pip install`` but the results will not be usable [3]_.

- **Zope2 add-ons** AKA "products", most notably the Zope2 Content Management Framework (CMF). This is something you install on top of Zope2 (conceptually but not literally, ``pip install Products.CMFCore``) that provides typical content management features e.g. personalization, workflow, cataloging, etc.

- **Zope3** technologies e.g. the Zope Component Architecture (ZCA). These are things that are included-or-integrated with Zope2 and Plone. [4]_

- **Buildout** technologies e.g. setuptools, console scripts, recipes, extensions, etc. You can't easily build Plone without them, so we may as well declare them as dependencies.

- **Plone** technologies. Plone was originally known as a "skin for CMF" but has become much more than that. 

    - **Archetypes** Legacy content type framework.

    - **Dexterity** Modern content type framework based on modern Zope concepts e.g. "Reuse over reinvention".

    - **Diazo** Modern theming engine based on XSLT that "maps Plone content to generic website themes."

In total, if you ``pip install Plone`` over 200 Python packages are installed [5]_.

What is Plock, really? 
--------------------------------

OK now it's time to explain Plock. Plock is a thing:

- you **install from PyPI** via ``pip install plock``. "Pip installs packages. Plock installs Plone."
- you use to **install Plone** without having to know about tarballs or Buildout.
- you use to **install Plone add-ons** without having to know about Buildout.

In one sentence: Plock runs Buildout so you don't have to, at least initially.

First steps with Plock
----------------------

Step #1
~~~~~~~

The first step with Plock [9]_ is a light bulb moment: "I've heard that Plone is the ultimate open source enterprise CMS and I'd love to try it!" But you aren't willing to download a compressed archive and run the installer nor are you willing to ``pip install zc.buildout`` and figure the rest out for yourself. Enter Plock.

Step #2
~~~~~~~

The second step with Plock is knowing it exists and you can install it with: ``pip install plock``.

Step #3
~~~~~~~

The third step with Plock is using it to install Plone::

    $ plock plone
    Creating virtualenv... (plone)
    Installing buildout...
    Downloading installer (https://launchpad.net/plone/4.3/4.3.4/+download/Plone-4.3.4-r1-UnifiedInstaller.tgz)
    Unpacking installer...
    Unpacking cache...
    Installing eggs...
    Installing cmmi & dist...
    Configuring cache...
    Running buildout...
    Done, now run:
      plone/bin/plone fg

Now Plock's work is done; visit the following URL: ``http:://localhost:8080`` and you should see:

.. image:: /images/plock-screen-1.png
    :alt: Plock Screen 1
    :align: center

Create a Plone site:

.. image:: /images/plock-screen-2.png
    :alt: Plock Screen 2
    :align: center

Start using Plone:

.. image:: /images/plock-screen-3.png
    :alt: Plock Screen 3
    :align: center

Next steps with Plock
---------------------

Installing Add-ons
~~~~~~~~~~~~~~~~~~

Upgrading Plone
~~~~~~~~~~~~~~~

Plock is more than just a way to install the latest stable version of Plone with add-ons quickly and easily. It's also a way to install almost any version of Plone, including the upcoming Plone 5 release.

Step #1
+++++++

Realize Plock has created a ``buildout.cfg`` file you can edit.

Step #2
+++++++

Also realize Plock hosts `Buildout configuration files called Pins <https://github.com/plock/pins>`_.

Step #3
+++++++

Edit your ``buildout.cfg`` file. Change the first ``extends`` URL from::

    [buildout]
    extends =
        https://raw.github.com/plock/pins/master/plone-4-3
    #    https://raw.github.com/plock/pins/master/dev

To::

    [buildout]
    extends =
        https://raw.github.com/plock/pins/master/plone-5-0
    #    https://raw.github.com/plock/pins/master/dev

Run Buildout and start Plone::

    $ bin/buildout
    $ bin/plone fg

Enjoy the Plone 5 running man:

.. image:: /images/plock-screen-5.png
    :alt: Plock Screen 5
    :align: center

.. [1] Whether or not dealing with that complexity is "worth it" I will not address here. Suffice it to say people still use and care about Plone and with Plone 5 coming "real soon now" there is some excitement building.

.. [2] He probably made it many times, and rightfully so.

.. [3] You can create an "instance" after ``pip install zope2`` with ``bin/mkzopeinstance`` but ``$INSTANCE/bin/runzope`` fails with ``ImportError: cannot import name _error_start`` probably due to mismanaged package versions. Maybe we can fix this with version specs included in a dummy package's ``setup.py``?

.. [4] The integration is *not* seemless, an undisputed fact as far as I know.

.. [5] 235

.. [7] Creating and executing a ``buildout.cfg`` file for the end user. Buildout configuration files are written in INI-style text. Ideally the end user sees this file and says "Ah, now I understand how this works."

.. [8] I've also `covered <http://blog.aclark.net/2013/07/19/introducing-plock/>`_ `Plock <http://blog.aclark.net/2013/07/29/whats-new-as-of-plock-0-1-2/>`_ `before <http://blog.aclark.net/2013/12/29/introducing-plock-again/>`_ `here <http://blog.aclark.net/2014/03/20/introducing-plock-pins/>`_.

.. [9] As someone familiar with Python already, because that is the market I like to serve.
