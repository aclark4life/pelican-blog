No, really, you can (just) use Buildout to install Plone.
================================================================================

:date: 2010-01-07 12:39
:tags: Plone

This is a follow up to my `Getting Excited about Plone as Eggs`_ post, because I can't keep updating that one forever.

Generally speaking, the recommended (and supported) way to install Plone is via the installers, e.g. the `Unified Installer`_. Obviously, if you want things to Just Work™ you should be using the latest stable release, which is why I linked to the 3.3.3 unified installer (although there is no Windows installer for 3.3.3 yet, which is why it's not released on plone.org).

That said, since both Plone and Zope 2 have been packaged as eggs  (Plone became an egg in version 3.2 and Zope 2 became an egg as of Zope 2.12 which is the version of Zope 2 that Plone 4 will use) it has become "mostly trivial" to write a buildout.cfg to install Plone with. That means that you don't even need paster to do it. You can just fire up an editor and type:

::

    [buildout]
    parts = instance

    [instance]
    recipe = plone.recipe.zope2instance
    user = admin:admin
    eggs =
        Plone

Amazing!

Of course there is the nasty bit about PIL, which I get around now-a-days by adding a very specific find-link, e.g.:

::

    [buildout]
    parts = instance
    find-links = http://dist.plone.org/thirdparty/PILwoTk-1.1.6.4.tar.gz

    [instance]
    recipe = plone.recipe.zope2instance
    user = admin:admin
    eggs =
        PILwoTk
        Plone

What you should have at this point is a working Plone, but not necessarily a repeatable buildout. The reason being we have not pinned any egg versions yet, so we are effectively asking for whatever the latest version of Plone is on PyPI. Fun for playing, not fun for production. Fortunately the nice Plone people have created a bunch of version pins for us, so we just need to use them:

::

    [buildout]
    extends = http://dist.plone.org/release/4.0a3/versions.cfg
    versions = versions
    parts = instance
    find-links = http://dist.plone.org/thirdparty/PILwoTk-1.1.6.4.tar.gz

    [instance]
    recipe = plone.recipe.zope2instance
    user = admin:admin
    eggs =
        PILwoTk
        Plone

If you are completely new to buildout and you are thinking to yourself right now "what in the world is this guy talking about?" then you will likely want to install buildout first so you can join in the fun. Fortunately, the nice Python people have made that easy with a package called `Distribute`_.

Following their instructions, you can do this:

::

    $ curl -O http://python-distribute.org/distribute_setup.py
    $ python distribute_setup.py

Then:

::

    $ easy_install zc.buildout
    $ mkdir plone
    $ cd plone
    $ buildout init

After which you will have a buildout.cfg file, and you can follow along with the above steps. Happy?

The best part about all of this is that (on a fast internet connection) it should only be a matter of minutes before you are able to do this:

::

    $ bin/instance fg

and be staring at a thing of beauty.

Of course, if you are running in the foreground (recommended for debugging) you should see something like this:

::

    aclark@Alex-Clarks-MacBook-Pro:~/Developer/public-plone/ > bin/instance fg
    /Users/aclark/Developer/public-plone/parts/instance/bin/runzope -X debug-mode=on
    2010-01-07 12:07:56 INFO ZServer HTTP server started at Thu Jan  7 12:07:56 2010
     Hostname: 0.0.0.0
     Port: 8080
    2010-01-07 12:08:14 INFO Zope Ready to handle requests

If you'd like to get a little less noisy and skip debug mode but still run in the foreground, you can use April 2008's famous addition to plone.recipe.zope2instance:

::

    aclark@Alex-Clarks-MacBook-Pro:~/Developer/public-plone/ > bin/instance console

Sweet, blissful, silent running Plone.

Happy Plone 4'ing all!

.. _Getting Excited about Plone as Eggs: http://blog.aclark.net/2008/12/15/getting-excited-about-plone-as-eggs/
.. _Unified Installer: http://launchpad.net/plone/3.3/3.3.3/+download/Plone-3.3.3-UnifiedInstaller.tgz
.. _Distribute: http://pypi.python.org/pypi/distribute
