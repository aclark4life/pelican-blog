Plone secrets: Episode 2 - Collective Python buildout
#####################################################
:date: 2011-07-06 12:45
:tags: Plone, Python

You know who uses the (Plone) Collective Python buildout? Me neither,
because we don't have any good statistics on its use (that I know of).
If it were a Python package, we could at least `count the number of
times it has been downloaded`_.

You know who should use it? Everyone.

*[dramatic pause…]*

OK maybe not everyone, but at least everyone that regularly develops
with **multiple versions of Python**. Here's why.

Actively maintained
===================

Check out this `log`_:

`|image0|`_

It has been going strong for over 3 years.

.. raw:: html

   </p>

If I recall correctly, it was born out of the frustration¹ of having to
compile Python on Mac OS X Leopard. Python *never* compiles correctly on
new versions of OS X (which is a complete mystery to me given that Apple
ships with Python, don't they think people will want to compile it?).

Easy to install
===============

Got Subversion? Then you *can haz* the Collective Python buildout². You
will also need to bootstrap it with whatever Python version you happen
to have laying around. I won't go into detail about this; but suffice it
to say depending on your OS, one of the following or something like it
should work:

::

    $ aptitude install python2.5

Or:

::

    $ brew install python

If you are on Windows, give up (unless you have a Microsoft C compiler).
Sorry.

.. raw:: html

   </p>

.. raw:: html

   <p>

Now, check out the code from the repository (if you are a member of the
`Collective`_ and may potentially contribute something back, make sure
you use https):

::

    $ svn co http://svn.plone.org/svn/collective/buildout/python

Next, bootstrap and run the buildout:

::

    $ cd python
    $ python bootstrap.py -d
    $ bin/buildout

That's it. The buildout should go merrily on it's way compiling Python
2.4 through 3.2. When it finishes, you can install it in /opt (or
wherever you like) with the following command (you might need sudo):

::

    $ bin/install-links

Then you should see:

::

    $ /bin/ls -1 /opt/local/bin
    easy_install-2.4
    easy_install-2.5
    easy_install-2.6
    easy_install-2.7
    easy_install-3.2
    pip-2.4
    pip-2.5
    pip-2.6
    pip-2.7
    pip-3.2
    python2.4
    python2.5
    python2.6
    python2.7
    python3.2
    virtualenv-2.4
    virtualenv-2.5
    virtualenv-2.6
    virtualenv-2.7
    virtualenv-3.2

Easy to configure
=================

Now you can add **/opt/local/bin** to your environment PATH variable.
This will make it easy to choose a particular Python, PIP, or Virtualenv
at your leisure.

.. raw:: html

   </p>

Unfortunately, if you pip install something, it will end up in the
checkout instead of */opt/local/bin*.

.. raw:: html

   <p>

To get around this, I usually pick one Python for daily use, and add its
bin directory to my environment PATH variable:

::

    $ echo $PATH | tr ':' 'n'
    /sbin
    /usr/sbin
    /usr/local/bin
    /opt/local/bin
    /Users/aclark/Developer/collective/python/python-2.7/bin
    /usr/bin
    /bin
    /sbin
    /usr/X11/bin

After various pip installs, my 2.7 bin directory contains the usual
tools of the trade:

::

    $ /bin/ls -1 /Users/aclark/Developer/collective/python/
    python-2.7/bin
    __dotcloud_git_ssh
    activate
    activate.csh
    activate.fish
    activate_this.py
    bfg2pyramid
    checkoutmanager
    cloudservers
    dotcloud
    easy_install
    easy_install-2.7
    eye
    flake8
    fsdump
    fsoids
    fsrefs
    fstail
    hg
    mako-render
    mkrelease
    paster
    pilconvert.py
    pildriver.py
    pilfile.py
    pilfont.py
    pilprint.py
    pip
    pip-2.7
    playerpiano
    pygmentize
    python
    python2.7
    recorderpiano
    repozo
    rfc2397
    rst2html.py
    rst2latex.py
    rst2man.py
    rst2newlatex.py
    rst2odt.py
    rst2odt_prepstyles.py
    rst2pseudoxml.py
    rst2s5.py
    rst2xml.py
    rstpep2html.py
    runzeo
    sphinx-autogen
    sphinx-build
    sphinx-quickstart
    vanity
    zconfig
    zconfig_schema2html
    zdaemon
    zeoctl
    zeopack
    zeopasswd

Wrap it up, I'll take it
========================

That's it! There is not too much more to say, other than I hope you find
this post useful and will consider using the `Collective Python
buildout`_.

.. raw:: html

   </p>

Of course, comments are always welcome.

Notes
-----

¹ Experienced by its creator, `fschulze`_.

.. raw:: html

   </p>

² It will likely end up on `Github`_ at some point.

 

.. _count the number of times it has been downloaded: http://blog.aclark.net/2011/06/16/youre-so-vain-so-why-not-use-vanity/
.. _log: http://goo.gl/BJw33
.. _|image1|: http://aclark4life.files.wordpress.com/2011/06/screen-shot-2011-06-29-at-1-27-12-pm.png
.. _Collective: http://dev.plone.org/collective
.. _Collective Python buildout: http://svn.plone.org/svn/collective/buildout/python
.. _fschulze: http://twitter.com/fschulze
.. _Github: http://github.com/collective

.. |image0| image:: http://aclark4life.files.wordpress.com/2011/06/screen-shot-2011-06-29-at-1-27-12-pm.png
.. |image1| image:: http://aclark4life.files.wordpress.com/2011/06/screen-shot-2011-06-29-at-1-27-12-pm.png
