Plock Rocks
===========

:date: Fri Apr 24 07:49:07 EDT 2015
:tags: Plone, Python

.. image:: /images/plock-meme.png

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

- **Zope3** technologies e.g. the Zope Component Architecture (ZCA). These are things that are included-in-or-integrated-with Zope2 and/or Plone. [4]_

- **Buildout** technologies e.g. setuptools, console scripts, recipes, extensions, etc. You can't easily build Plone without them, so we may as well declare them as dependencies.

- **Plone** technologies. Plone was originally known as a "skin for CMF" but has become much more than that. None of its technologies should be known outside of the Plone community (unless they should be [6]_) and I like to think of them as "code names" for particular features in Plone. Here's a few:

    - **Archetypes** Legacy content type framework.

    - **Dexterity** Modern content type framework based on modern Zope concepts e.g. "Reuse over reinvention".

    - **Diazo** Modern theming engine based on XSLT that "maps Plone content to generic website themes."

In total, if you ``pip install Plone`` over 200 Python packages are installed [5]_.

What is Plock, really? 
--------------------------------

OK now it's time to explain Plock. Plock is:

- A package you **install from PyPI** via ``pip install plock``. Pip installs packages and Plock installs Plone.
- A tool to **install Plone** in the most fluid, painless way given the size of the software.
- A tool to **install Plone add-ons** in the most fluid, painless way without knowing anything about the Plone ecosystem.

What Plock is not
-----------------

Let me also briefly describe what Plock is not:

- Plock is **not Plone**.
- Plock is not finished.
- Plock is not going away.

First steps with Plock
----------------------

Step #1
~~~~~~~

The first step with Plock [9]_ begins with a light bulb like this: "I've heard about Plone and I'd love to try it!" But you aren't willing to download a compressed archive and run the installer nor are you willing to ``pip install zc.buildout`` and figure the rest out for yourself. Enter Plock.

Step #2
~~~~~~~

The second step with Plock begins with knowing it exists and that you can install it via: ``pip install plock``.

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

Step #4
~~~~~~~

Now visit the following URL: ``http:://localhost:8080`` and you should see:

.. image:: /images/plock-step-4.png


Step #5
~~~~~~~

Create a Plone site::

.. image:: /images/plock-step-5.png

Step #6
~~~~~~~

Start using Plone::

.. image:: /images/plock-step-6.png


Next steps with Plock
---------------------

But Plock is more than just a way to install the latest stable version of Plone quickly and easily. It's also a way to install almost any version of Plone, including the upcoming highly anticipated Plone 5 release.


.. [1] Whether or not dealing with that complexity is "worth it" I will not address here. Suffice it to say people still use and care about Plone and with Plone 5 coming "real soon now", there is some excitement building.

.. [2] He probably made it many times, and rightfully so.

.. [3] You can create an "instance" after ``pip install zope2`` with ``bin/mkzopeinstance`` but ``$INSTANCE/bin/runzope`` fails with ``ImportError: cannot import name _error_start`` probably due to mismanaged package versions. Maybe fixing this with proper version specs in a dummy package's ``setup.py`` could be a thing?

.. [4] The integration is *not* seemless, an undisputed fact as far as I know.

.. [5] 235

.. [6] Many Plone technologies could be useful outside of Plone. But as far as I know, none of them have been.

.. [7] Creating and executing a ``buildout.cfg`` file for the end user. Buildout configuration files are written in INI-style text. Ideally the end user sees this file and says "Ah, now I understand how this works."

.. [8] I've also covered Plock here, here and here.

.. [9] As someone familiar with Python already, because that is the market I like to serve.
