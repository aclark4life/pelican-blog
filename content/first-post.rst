First Post
##########
:date: 2007-10-17 08:55
:tags: Plone

`|image0|`_\ Why? Because I can (read: `Plone`_ allows me to do so) but
also:

-  I have been reading a lot of `Plone blogs`_ lately and they have
   inspired me to write my own.
-  I want to interact with other Plonistas.
-  I want to get my web 2.0 **ON**. ;-)

To that end, this post is about my `build tools`_ and how I love them.

Note: there are **much** better ways to accomplish what I'm doing here.
I'm reminding *myself* this as much as the reader. So why do I continue
to use them? Good question! I'll save the answer for another post, but
for now you should be aware of these (better) alternatives:

-  `Buildout`_

-  `Buildit`_

-  `Instance Manager`_

I used buildout for the first time at the `Baarn UI Sprint 2007`_ and
really enjoyed it. I have also used and enjoyed Chris McDonough's
buildit. That may be where I end up (and there are several more to
choose from) but for now I still enjoy typing:

::

    newzope test-site ProductA ProductB ProductC

and having a working instance a few seconds later (with Product[A,B,C]
installed)! Of course this requires I have a working Zope already... and
that I edit Zope's skel/etc/zope.conf... but hey nothing is perfect and
old habits die hard.

.. _|image1|: http://aclark4life.files.wordpress.com/2007/10/look-at-me.jpg
.. _Plone: http://plone.org/
.. _Plone blogs: http://planet.plone.org/
.. _build tools: http://svn.plone.org/svn/collective/newzope
.. _Buildout: http://dev.plone.org/plone/browser/ploneout/trunk/README.txt
.. _Buildit: http://agendaless.com/Members/chrism/software/buildit
.. _Instance Manager: http://plone.org/products/instancemanager
.. _Baarn UI Sprint 2007: http://plone.org/events/sprints/baarn-ui-sprint-2007/

.. |image0| image:: http://aclark4life.files.wordpress.com/2007/10/look-at-me.jpg
.. |image1| image:: http://aclark4life.files.wordpress.com/2007/10/look-at-me.jpg
