A sane buildout for repoze.zope2 + Plone?
=========================================

:date: 2009-06-18 22:09
:tags: Plone

(This is also a follow-up of sorts to `Martin Aspeli's excellent
introduction to repoze and Plone from last year`_.)

A Tale of Two Buildouts
-----------------------

There are two stories going on here, both of which `Martin Aspeli
recently described in great detail`_ and `Chris McDonough tackled last
year`_. For the purposes of this blog entry, I'll refer to the issue as
the "index vs. find-links" conundrum in buildout  (find-links in
buildout are equivalent to distribution\_links in setuptools).

For those that want strict repeatability, using the index parameter is
the clear winner. It simply forces buildout to do the right thing now
and forever, by limiting what packages it can select from. For those
that want functionality and don't mind the occasional egg-out-of-whack
(i.e. unexpected upgrade), then using the find-links parameter can
provide a "sexy" way to get decent results quickly (but may, and
probably will, shoot you in the foot later).

Sexy, but Dangerous
-------------------

Let's start with the sexy, but with less repeat-ability method first.
Using this method we are not specifying our own index. Therefore you are
free to add any package from `PyPI`_ or `plone.org`_ as you see fit.
This is essentially why people like this method (the counter argument is
that it is simple to add any additional egg you may want to your index,
but we'll get to that later).

So a simple buildout using this method might look like this:

    0. virtualenv plone; cd plone

    1. bin/easy\_install zc.buildout

    2. bin/buildout init

    3. Edit buildout.cfg:

::

    [buildout]
    extends =
    # Using Martin Aspeli's good-py, thanks!
        http://good-py.appspot.com/release/repoze.zope2/1.0
        http://dist.plone.org/release/3.3rc3/versions.cfg
    versions = versions
    find-links =
        http://dist.repoze.org/zope2/latest
        http://dist.repoze.org/zope2/dev/
        http://dist.plone.org/release/3.3rc3
    parts = instance[instance]
    recipe = zc.recipe.egg
    dependent-scripts = true
    eggs =
        repoze.zope2
        Plone
        PIL

    4. bin/buildout

A few more steps are required, which we could certainly automate in
buildout, but for now I'll just list them here:

    5. bin/mkzopeinstance

    6. bin/addzope2user admin admin

Now, the moment we've all been waiting for… the fun part!

    7. bin/paster serve etc/zope2.ini

You should see something like:

::

    [aclark@alex-clarks-macbook-pro]~/Developer/plone% bin/paster serve etc/zope2.ini
    2009-06-18 22:52:24 INFO Marshall libxml2-python not available. Unable to register libxml2 based marshallers.
    2009-06-18 22:52:27 WARNING ZODB.FileStorage Ignoring index for /Users/aclark/Developer/p3-repoze-2/var/Data.fsDeprecationWarning: zope.app.annotation has moved to zope.annotation. Import of zope.app.annotation will become
    unsupported in Zope 3.5
    /Users/aclark/Developer/plone/eggs/zopelib-2.10.7.0-py2.4-macosx-10.5-i386.egg/zope/configuration/xmlconfig.py:323:
      __import__(arguments[0])
    ------
    2009-06-18T22:52:24 INFO Marshall libxml2-python not available. Unable to register libxml2 based marshallers.
    ------
    2009-06-18T22:52:27 WARNING ZODB.FileStorage Ignoring index for /Users/aclark/Developer/plone/var/Data.fs
    Starting server in PID 26900.
    zserver on port 8080

At this point, you should be able to login to
http://localhost:8080/manage and create a Plone site.

Of course, we did a sloppy job here, creating the Zope2 instance in the
root of the buildout, etc. It is possible that
`plone.recipe.zope2install`_ may help us in the future by supporting
repoze.zope2 instances (or maybe it does already, I didn't try).

Next up?

Boring, but Repeatable
----------------------

I kid, but this is actually a very serious concern for many people, and
rightfully so. The notion that your buildout will work the same today as
it does in one year from now may be a strict requirement for your
project. If it is, we can accommodate you (I hope) with the "index"
buildout that follows. The downside is that \*you\* can't control what I
put in the index. However, you can certainly create your own index using
this technique.

An arguably even simpler buildout using this technique might look like
this:

    0. virtualenv plone; cd plone

    1. bin/easy\_install zc.buildout

    2. bin/buildout init

    3. Edit buildout.cfg:

::

    [buildout]
    index = http://dist.plone.org/experimental/release/3.3rc3/simple/
    parts = instance[instance]
    recipe = zc.recipe.egg
    dependent-scripts = true
    eggs =
        repoze.zope2
        Plone
        PIL

    4. bin/buildout

    5. bin/mkzopeinstance

    6. bin/addzope2user admin admin

    7. bin/paster serve etc/zope2.ini

In Conclusion
-------------

Depending on what my needs are, I might choose either of these
techniques. We can also hold out for `multi-index support in
setuptools`_. That would seemingly make everyone happy. In the meantime,
I can tell you I'd definitely reach for a buildout sans custom index
first, then ask questions later (i.e. wait for bleeding toes) but that
is just me. If people find the "index" technique generally useful, I'd
be willing to support package sheperding and `index generating with
basketweaver`_. Just let me know. If it really catches on, we could
rename `http://dist.plone.org/experimental/release/3.3rc3/`_ to
http://dist.plone.org/repoze/release/3.3rc3/. Of course, if anyone
objects to this or finds it confusing, I can just as easily remove it
(from dist.plone.org).

Special thanks to `Chris McDonough`_ and `Martin Aspeli`_ for helping me
scratch my itch!

Finally, please don't rely on any of this "in production" yet unless you
know what you are doing. I tested these techniques up to the point of
starting Zope (via paste) and adding a Plone site, nothing more! :-)

I, however, am getting a new server next week and will be hosting this
site on `repoze.zope2`_ very shortly ;-)

.. _Martin Aspeli's excellent introduction to repoze and Plone from last year: http://www.martinaspeli.net/articles/rolling-out-repoze
.. _Martin Aspeli recently described in great detail: http://www.martinaspeli.net/articles/scrambled-eggs
.. _Chris McDonough tackled last year: http://plope.com/Members/chrism/distribution_links_considered_harmful
.. _PyPI: http://pypi.python.org/simple/
.. _plone.org: http://plone.org/products/simple
.. _plone.recipe.zope2install: http://pypi.python.org/pypi/plone.recipe.zope2instance/3.2
.. _multi-index support in setuptools: http://bugs.python.org/setuptools/issue32
.. _index generating with basketweaver: http://pypi.python.org/pypi/basketweaver/0.1.2-r6
.. _`http://dist.plone.org/experimental/release/3.3rc3/`: http://dist.plone.org/experimental/release/3.3rc3/
.. _Chris McDonough: http://plope.com/
.. _Martin Aspeli: http://www.martinaspeli.net/
.. _repoze.zope2: http://repoze.org/quickstart.html#repoze.zope2
