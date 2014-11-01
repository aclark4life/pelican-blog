Mozilla and PyPI
================================================================================

:date: 2011-09-22 12:03
:tags: Plone, Python

The `last time I wrote about PyPI`_ some folks mistook the subject to be `PyPy`_, so let me be clear: this article is about the `Python Packaging Index`_.

I recently began doing some volunteer work for Mozilla[1], working on a `virtual machine setup`_ to make kitsune development easier (kitsune is the code name for the Django site that powers `support.mozilla.com`_).

Git submodules
--------------

In doing so, I came across an interesting command from their `installation docs`_:

::

    $ git submodule update --init --recursive

I can recall some vague rumblings about git submodules prior to this incident, but nothing I'd call "familiarity". So, I shrugged it off and went about the business of creating the VM (and resisting the urge to use `zc.buildout`_ to do it):

-  On day 1, I created a `VirtualBox`_ VM using the latest Ubuntu Server and was able to assemble and run the application by following the instructions.
-  On day 2, I began to `"vagrantize"`_ the process. Here I ran into a bit of trouble with the git-submodule command[2]. This led me to seek alternative methods to install the various Python packages it was trying to install (when stuck on a problem I often like to pursue the alternatives immediately, so I have them if I need them.)

Zamboni
-------

Then, in the Mozilla IRC channel #sumodev (**su**\ pport **mo**\ zilla) some nice Mozillian (willkg) pointed me to this gem:

- `http://mozweb.readthedocs.org/en/latest/packaging.html`_

Which in turn led me to the following two links:

- `http://jbalogh.github.com/zamboni/topics/packages/`_
- `http://playdoh.readthedocs.org/en/latest/packages.html#packages`_

Again, faint rumblings… this time about zamboni (not THAT Zamboni). I know I've heard of it, but I wouldn't call myself familiar with it. So, I innocently read the following:

    **Python projects can incur a number of dependencies. ``pip`` can be handy, but we’ve had better luck with distributing a ``vendor`` library.**

At which point I immediately thought to myself:

    **Yeah… I hear that.**

Followed a few seconds later by:

    **Wait… what?!?**

Playdoh
-------

Some time/research later[3], I (re)discovered that zamboni is the codename for `addons.mozilla.org`_\ [4]. And `Playdoh`_ is the code name for Mozilla's base Django project setup. If you aren't familiar with Playdoh, please do give it a whirl[5].

PyPI
----

While all of this is very, very interesting to me, I am primarily a "systems and processes" guy; and what ultimately stuck with me after two days of Mozilla-ing is the following blurb from the Playdoh packaging documentation:

    **The ``/vendor`` library is supposed to contain all packages and repositories. It enables the project to be deployed as one package onto many machines, without relying on PyPI-based installations on each target machine.**

"Nooooooooooooooo", I am now saying to myself over and over. "Without relying on PyPI-based installations on each target machine." Another "noooooooooooooooo!" :-) I certainly don't fault Mozilla for taking this approach, but it makes me sad that large organizations like Mozilla are passing over PyPI in favor of alternative methods of distributing Python software.

Let us all now hang our heads, for a moment of pause and reflection.

*[a minute passes]*

The future
----------

I can't speak for anyone else, but I would certainly like to see this change in the future. I would LOVE to see PyPI become a place that Mozilla felt confident it could use to deploy Python software. And this is something I'd love to work on *for* Mozilla, if given the opportunity[6].

Great for Python == great for Mozilla?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It's obvious what's in it for Python, but what's in for Mozilla?

Simple.

I happen to share Mozilla's vision for an open web and open source in general. And it's great to see them embracing & using Python for their web projects! Without a doubt,  they are interested in giving back to the Python community (e.g. via Playdoh and the Django community, in this case.) So I suspect they'd be open to helping the Python community fix a long standing issue: the stability and reliability of the Python Package Index. It would certainly benefit them in the long run to simplify their build process to the point where git-submodule was no longer needed[7].

Notes
-----

[1] I am actively courting Mozilla in hopes of landing a gig by the end of the year. So all you Mozillians who know me personally, please put in a good word! And all you Mozillians I have not met yet: nice to meet you! :-)

[2] The problem turned out to be git-submodule failing to run because things like: grep and sed were missing from the PATH. Easily fixed by modifying the puppet configuration, but not easily discovered because git-submodule itself returned zero! Some guy on #puppet was very helpful in getting me to print out debug info.

[3] More help from friendly Mozillians in #webdev:

    11:13 < groovecoder> aclark: yeah, zamboni is amo 11:13 < kumar> playdoh was extracted from zamboni and other apps 11:13 < kumar> but zamboni itself does not eat the playdoh dog food, actually 11:15 < kumar> aclark also, in case you're not steeped in our initialisms, amo is addons.mozilla.org

[4] There is a great presentation about it here: `http://www.slideshare.net/andymckay/anatomy-of-a-large-django-site-7590098`_.)

[5] More from kumar (emphasis is my own):

    11:25 < kumar> **Playdoh is starting to stabilize** so it would be **good to see some use of it outside Mozilla**; this would probably help us catch Mozilla-specific things that need extraction

[6] LARGE HINT ;-)

[7] Again, not that there is anything wrong with what Mozilla is doing here. As a systems guy, I just happen to gravitate toward simplifying processes by eliminating steps.

.. _last time I wrote about PyPI: http://blog.aclark.net/in-defense-of-pypi
.. _PyPy: http://pypy.org/
.. _Python Packaging Index: http://pypi.python.org/pypi
.. _virtual machine setup: https://github.com/aclark4life/kitsune-vagrant
.. _support.mozilla.com: http://support.mozilla.com
.. _installation docs: https://github.com/jsocol/kitsune/blob/master/docs/installation.rst
.. _zc.buildout: http://pypi.python.org/pypi/zc.buildout/1.5.2
.. _VirtualBox: http://virtualbox.org
.. _"vagrantize": http://vagrantup.com
.. _`http://mozweb.readthedocs.org/en/latest/packaging.html`: http://mozweb.readthedocs.org/en/latest/packaging.html
.. _`http://jbalogh.github.com/zamboni/topics/packages/`: http://jbalogh.github.com/zamboni/topics/packages/
.. _`http://playdoh.readthedocs.org/en/latest/packages.html#packages`: http://playdoh.readthedocs.org/en/latest/packages.html#packages
.. _addons.mozilla.org: https://addons.mozilla.org
.. _Playdoh: http://playdoh.readthedocs.org/
.. _`http://www.slideshare.net/andymckay/anatomy-of-a-large-django-site-7590098`: http://www.slideshare.net/andymckay/anatomy-of-a-large-django-site-7590098
