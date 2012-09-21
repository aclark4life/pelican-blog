Bootstrapping a Buildout 1.6 release
####################################
:date: 2012-08-13 21:10
:tags: Plone, Python
:category: Plone

A lot of work has been done on Buildout lately, most notably:

-  Jim Fulton is `working on Buildout 2`_.
-  Ross Patterson has greatly `improved Buildout performance`_.
-  Domen Kožar has `provided a patch`_ that takes a conservative
   approach to Ross's performance improvements.
-  I have offered to do a release.

And there are a `handful of other changes`_ in `trunk on svn.zope.org`_,
of which my favorite is:

    The buildout init command now accepts distribution requirements and
    paths to set up a custom interpreter part that has the distributions
    or parts in the path. For example:: $ python bootstrap.py init
    BeautifulSoup

So with that, I am **planning to do a zc.buildout 1.6 release within 24
hours** or so of now. Please add a comment or weigh in on
`distutils-sig`_ if you object. We have run the tests on Windows, and
discovered only pre-existing failures. We are also preparing to do
"Buildout 2 prophylactic releases" (i.e. releases that make 1.x continue
to work when 2.x is released) in the 1.6.x series.

.. raw:: html

   </p>

.. _working on Buildout 2: https://github.com/buildout/buildout/commits/master
.. _improved Buildout performance: http://rpatterson.net/blog/buildout-performance-improvements
.. _provided a patch: http://zope3.pov.lt/trac/changeset/127507
.. _handful of other changes: http://mail.python.org/pipermail/distutils-sig/2012-July/018779.html
.. _trunk on svn.zope.org: http://zope3.pov.lt/trac/browser/zc.buildout/trunk/CHANGES.txt?rev=127507#L4
.. _distutils-sig: http://mail.python.org/mailman/listinfo/distutils-sig
