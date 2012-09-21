Top 10 reasons &quot;Plone 3.3. Site Admin&quot; book is (still) for you
########################################################################
:date: 2011-05-10 13:34
:tags: Plone, Python

About a year ago, I was frantically trying to finish `Plone 3.3 Site
Administration`_ in time to teach it at Plone Symposium East 2010 (at
Penn State University) as well as publish it. I remember staying up all
night to finish & submit the final drafts then driving 4 hours to Penn
State, then teaching for 8 hours before I was finally able to crash (but
not before consuming a large and delicious cheeseburger and a Yuengling
from the `Nittany Lion Inn`_\ room service, yum).

The class went well and everyone seemed happy with the results (and I am
very grateful to PSU for the opportunity). I remember struggling to get
some Windows users up to speed, so this year I've decided to "require"
students to install Plone before the class (via the `appropriate
installer for their platform`_). Most "site admin-ing" we do will be "ad
hoc" preferably on top of a stand-alone Python installation. But we can
refer to the installer-based Plone as needed (and in fact the
installer-based Plone is all some folks will ever need or want).

The list
--------

Anyway, this post is about this year's class taught from the same
material but updated to account for any changes that have occurred since
the book was first published. Most importantly, it addresses the release
of Plone 4 in the context of the book title "Plone 3.3 Site
Administration".

.. raw:: html

   </p>

So without further ado, why "Plone 3.3 Site Administration" is (still)
for you:

#. **The version reference in the title is (mostly) meaningless**.
   `PACKT`_ insist on incorporating a software version number into the
   title of their books. I would have called it: "Plone Site
   Administration", or "Buildout for Plone".
#. **The book teaches valuable *techniques*, using Plone 3.3 as an
   example**. Most, if not all of the techniques still apply today (i.e.
   w/Plone 4.0.x and Plone 4.1.x). They will likely continue to apply as
   long as Plone continues to rely on `zc.buildout`_.
#. **Plone makes it relatively easy to upgrade** by providing `version
   numbers`_ for all of the packages it requires. In many cases an
   upgrade simply involves referring to a newer list of package
   versions. In the case of upgrading from Plone 3.3.x to Plone 4.0.x,
   the [zope2] section goes away because Zope2 became an egg. (Compare
   `this buildout`_ with `this one`_.) Also Plone 4 buildouts should be
   bootstrapped with Python 2.6 instead of Python 2.4 (as was required
   by Plone 3).
#. **Python tools "goodness"**. This book goes to great lengths to
   demonstrate how Plone fits "naturally" on top of the Python software
   stack. It also includes information about non-Plone-specific
   Python-related technologies like `Distribute`_ and `PIP`_. This (in
   theory) makes Plone more approachable to "regular" Python folk.
#. **The Python buildout**. One of the most useful things the Plone
   community has to offer the Python community at large is the `Python
   buildout`_. If you do development that requires multiple versions of
   Python (e.g. Plone 3.3.x/4.0.x) you could do worse than to rely on
   this buildout to provide them (multiple versions) quickly and easily.
   The book dances around the subject, but the point is: use it.
#. **Cross-platform**. This book goes to great lengths to demonstrate
   the Plone installation process on three popular operating systems:
   Mac OS X, Ubuntu Linux, and Windows. The point is to show off how
   similar the process is across platforms because Python does all the
   hard work, and of course to deal with the cases where it is not
   similar (e.g. it's "hard" to compile `Python on Windows`_).
#. **Add-ons**! A lot of the value of Plone comes from the ability to
   customize it to fit your needs. If that customization has already
   been done by some other member of the community, even better. This is
   one of the core essences of the Plone community: everyone working
   hard to contribute to the available pool of add-ons, and then
   `sharing the results`_. This book aims to make you better at
   evaluating the myriad of options you may be presented with when you
   need to `find and install an add-on`_.
#. **Upgrades**! The final chapter of the book holds your hand and walks
   you through an upgrade from Plone 3.3.x to Plone 4.0.x. It doesn't
   contain anything you can't find at `http://plone.org/upgrade`_ (in
   fact it contains much less information), but in the context of a book
   full of buildout configuration file examples, it should feel more
   like a natural step than an intimidating process.
#. **Security**! The book covers how to deal with security patches,
   *not* in the common case of when a hotfix is released as a Zope 2
   Product or Python egg, but in the `somewhat more obscure case`_ where
   a newer (non-egg) Zope2 release replaces an older one (with a
   vulnerability). The modern equivalent would be a Plone release
   post-security-hotfix release. Such releases simply contain a newer
   KGS (listing package versions that contain the appropriate fixes).
   This "old school" example is included to give readers as broad a
   perspective as possible, so that they may better handle anything they
   may come across in the wild.
#. **All the boring stuff too**. This book also walks you through the
   remaining "hot" topics not covered yet in this list, all from a heavy
   zc.buildout configuration management perspective: site basics (e.g.
   customizing navigation), appearance (AKA theming, strictly "old
   style" sorry), administration (e.g. mail settings, ldap), deployment
   and maintenance (e.g. automating database backups and packing), and
   optimization (e.g. load balancing, supervisor, and `munin graphs`_!)

That's it!

The training
------------

Sound even the *slightest* bit interesting? And/or are these things you
*need* to know about Plone for your job? If so, then you or your
employees will not want to miss my one day class next week at the `Plone
Symposium East 2011`_. In case you (or your employees) are interested,
you can sign up here (separate from the symposium):

-  `http://aclark.net/training`_

Hope to see you there.

The service
-----------

BaaS (Buildout as a Service)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(Yes, I am serious)

.. raw:: html

   </p>

And finally for whatever it is worth, many of the lessons learned from
writing the book from the author's perspective ended up here:

-  dist.aclark.net/build/plone[1]

That is to say: buildouts are living and breathing things[2]; they are
frequently changing in response to what is going on in the Python
package ecosystem around them (even though their primary goal is to
maintain stability and/or to only change when you want to change). When
a change (like a security fix or configuration change) comes along, the
author pushes changes out to the dist server than deploys the dist
server changes to production.

.. raw:: html

   </p>

[1] DISCLAIMER: Please DO NOT RELY ON this "BaaS example" for anything
important, EVER. It's only here for educational purposes (for now at
least).

[2] Yeah, I don't get out much :-)

.. _Plone 3.3 Site Administration: http://aclark.net/training
.. _Nittany Lion Inn: http://www.pshs.psu.edu/NittanyLionInn/nlhome.asp
.. _appropriate installer for their platform: http://plone.org/products/plone/releases/4.0.5
.. _PACKT: http://www.packtpub.com/books/plone
.. _zc.buildout: http://pypi.python.org/pypi/zc.buildout
.. _version numbers: http://dist.plone.org/release/4.1b2/versions.cfg
.. _this buildout: http://dist.aclark.net/build/plone/3.3.x/buildout.cfg
.. _this one: http://dist.aclark.net/build/plone/4.0.x/buildout.cfg
.. _Distribute: http://packages.python.org/distribute/
.. _PIP: http://pypi.python.org/pypi/pip
.. _Python buildout: http://svn.plone.org/svn/collective/buildout/python/
.. _Python on Windows: http://python.org/download/windows/
.. _sharing the results: http://plone.org/products
.. _find and install an add-on: http://pypi.python.org/pypi
.. _`http://plone.org/upgrade`: http://plone.org/upgrade
.. _somewhat more obscure case: http://dist.aclark.net/build/plone/2.1.x/buildout.cfg
.. _munin graphs: http://pypi.python.org/pypi/munin.plone
.. _Plone Symposium East 2011: http://weblion.psu.edu/symposium
.. _`http://aclark.net/training`: http://aclark.net/training
