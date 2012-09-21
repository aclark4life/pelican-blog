In Defense of PyPI
##################
:date: 2011-01-31 09:19
:tags: Plone, Python
:category: Python

Everyone on the *Python Planet* is probably already familiar with Peter
Fein's recent article `about PyPI use (or lack thereof).`_ But in case
not, particularly striking was the number of folks who joined the "PyPI
bashing" in the comments. In fact, it has inspired me to write this post
"in defense of PyPI". I would like to offer the Python community a
summary of what I think are the general criticisms, along with my
responses as a "sysadmin / developer type".

First let me say this: I love PyPI! And I agree with Peter, if your
package isn't on PyPI it  "doesn't exist". I wouldn't put it quite like
that; but I would say it's fairly important if you are publishing open
source Python code, to consider uploading it to the Python Package
Index.

Why?

Because Everybody Wins
~~~~~~~~~~~~~~~~~~~~~~

Believe it or not, the general Python community is interested in seeing
your code. Whether to use it for an example, or to avoid reinventing the
wheel, or whatever the reason; we'd like a chance to see your code. But
if you don't publish it to PyPI, we may never get that chance!

.. raw:: html

   </p>

For better or worse, PyPI is the canonical place on Earth for Python
packages. It's the CPAN of Python. I understand that not everyone is
100% comfortable with this, but that doesn't make it any less true. If
you accept that "open source is good", and that "Python rules", then you
simply must take this next leap of faith: "PyPI is *the* place for
Python packages".

[waves hand]

Moving on, why else should you consider uploading your packages to PyPI?

Because It Is The "Right" Thing To Do
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Another thing that struck me is the number of folks who (appear to)
confuse "version control" with "distribution". If I'm not mistaken,
Launchpad, Github, and Bitbucket are primarily designed for Bazaar, Git,
and Mercurial hosting respectively. These sites can host your
distribution tarballs, but they certainly weren't *designed and built*
to do so. Rather, they were designed and built to host your source code.

.. raw:: html

   </p>

In some cases, a project may wish to host it's own `distribution
server`_. Whether it be for redundancy (although PyPI has begun to
tackle this) or "branding" or other reasons, I would argue this is the
preferred way of handling it: *in addition to uploading to PyPI, not in
place of it*.

Why?

Because It Is Not That Hard
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ahem… we get it. The situation with easy\_install is "less than ideal".
But this is something to be fixed, not avoided. If you are receiving too
many support requests, may I suggest `simply telling people not to use
easy\_install`_. Or, if the problem is proper packaging, learn how to
`test your packages`_ before uploading them. Due to the large number of
screwed up releases I've made, I've come to rely on a\ `local PyPI`_ and
a virtualenv to test installations. Others use `even simpler methods`_.
And with tools like `mkrelease,`_ it's easy to upload your package to
multiple PyPI locations with just a single command (although
leaping-tall-buildings-in-a single-bound is not yet supported.)

.. raw:: html

   </p>

The point is, please consider helping the community fix the problem
rather than simply avoiding it. There are folks `actively trying to
improve the situation`_ right now.

Let's see, what else?

Because It Does Not Have To Be Perfect
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Over the years I've seen various and sundry criticisms of the PyPI user
interface. Fine. I have not looked into the current development process,
but I assume the author/maintainers would be open to some constructive
criticism and/or development assistance.

.. raw:: html

   </p>

It doesn't have to be Github-sexy to be useful. If you would like to
report a bug or feature request, do it `here`_ (at least, I think that
is the right place.)

Conclusion
~~~~~~~~~~

I hope this convinces at least some folks to consider uploading their
packages to PyPI. If it doesn't, please let me know why in the comments.

.. raw:: html

   </p>

*Did you enjoy reading this article? If so, please consider `helping me
help Plone`_.*

.. _about PyPI use (or lack thereof).: http://blog.wearpants.org/elitism-and-the-importance-of-pypi
.. _distribution server: http://dist.plone.org/
.. _simply telling people not to use easy\_install: http://blog.jazkarta.com/2010/05/15/installing-plone-without-buildout/#comment-162
.. _test your packages: http://groups.google.com/group/pylons-devel/msg/abfe9e7a43f62594
.. _local PyPI: http://pypi.python.org/pypi/Products.PloneSoftwareCenter
.. _even simpler methods: http://groups.google.com/group/pylons-devel/msg/696c69843eecd026
.. _mkrelease,: http://pypi.python.org/pypi/jarn.mkrelease
.. _actively trying to improve the situation: http://wiki.python.org/moin/Distutils/SprintParis
.. _here: http://sourceforge.net/tracker/?group_id=66150
.. _helping me help Plone: http://blog.aclark.net/2011/01/21/help-alex-clark-help-plone/
