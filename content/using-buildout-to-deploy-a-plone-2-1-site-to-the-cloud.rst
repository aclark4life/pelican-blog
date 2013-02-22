Using Buildout to deploy a Plone 2.1 site to the cloud
######################################################
:date: 2010-03-15 21:03
:tags: Plone

Believe it or not, there are still Plone 2.1 sites in production. (And 1.0 sites too, for that matter. Just look for the tell-tale '/help' sign, e.g. `http://www.zope.org/help`_, if you suspect Plone 1).

I know, because I just `deployed one`_ (a cool artist's site if you have a couple hours to kill…). But I didn't do it the "old way" with Zope 2 instances created by hand on clunky physical servers, I used `Buildout`_ and the `Cloud`_.

Aside #1
~~~~~~~~

As an aside: it was really bothering me lately that you couldn't (easily) find older Plone releases at `SourceForge`_. This is by design to avoid confusion, but still confusing. So when I needed the most recent 2.1.x tarball I decided to scratch my itch and fix the "problem".  I started gathering the `hard to find`_ releases and putting them `here`_. OK… so I only gathered one release (2.1.4), but I swear I had good intentions. If you'd like to see any additional releases "moved" to dist.plone.org, please let me know in the comments.

Aside #2
~~~~~~~~

Another aside: I should mention here the advent of a tool that promises to simplify deployment of Python-based web applications to the cloud (or supported service, which technically does not have to be "cloud-based") via the use of APIs (in particular, the `Rackspace Cloud`_ API, which is the only one supported so far): `Silver Lining`_! The idea of using this tool got me so excited, I spent some time experimenting with setting up a new host with it (and purchasing their service). But when I realized it was not quite ready for production (i.e. "`if you want to use Silver Lining, Silver Lining is not for you`_\ " :-)), I ended up using the Rackspace Cloud **web interface**.

I was so impressed with it.

I literally moved all of my (granted, relatively small number of client sites) to their service within a matter of 1-2 months. Now, I know what you are thinking, and I do intend to explore other services (in fact, I have tried `Slicehost`_ and it was OK), but this service made my life so much easier I wanted to mention some of its key features:

-  "On the fly" requisitioning. You can add/remove hosts anytime and you only pay for the time they are up.
-  "On the fly" resizing of hosts. In my testing and real world experience, the resizing (e.g. move from a host with 256MB RAM and 10GB disk to 500MB RAM and 20GB disk) was painless (literally only cost a few minutes of downtime).
-  The potential for all of this to be done remotely via a command line tool like Silver Lining.

Aside #3
~~~~~~~~

A third and final aside: the status quo of WSGI support for Plone. Since `Zope 2 is not supported`_ by Silver Lining, the key to deploying Plone sites with it is currently to use `repoze.zope2`_. `Nate Aune`_ has recently made some progress with this, and more work is scheduled for\ `Plone Symposium East`_. My latest swipe at WSGI-Plone is here: `http://svn.aclark.net/svn/public/buildout/plone/branches/3.x-wsgi/`_

The actual point
~~~~~~~~~~~~~~~~

And finally, to the point of this blog entry! I have created a generic Plone 2.1 buildout for anyone interested. You can find it here:\ `http://svn.aclark.net/svn/public/buildout/plone/branches/2.1.x/`_.  Using it is simple, as described in the `README.txt`_:

::

     $ svn export http://svn.aclark.net/svn/public/buildout/plone/branches/2.1.x/ plone
     $ cd plone
     $ python2.4 bootstrap.py
     $ bin/buildout
     $ bin/instance fg

Since Plone 2.1 community support has expired for this release, and since Plone 2.1 shipped with Python 2.3 (if I recall correctly), this is definitely "unsupported use of Plone". But when you need it, you need it. I have yet to experience any issues related to the Python version, for whatever that is worth (possibly due to the fact that Plone 2.1 originally shipped with Python 2.3 and Zope 2.7, then Zope 2.8 came along which worked with Python 2.4. Just a guess).

.. _`http://www.zope.org/help`: http://www.zope.org/help
.. _deployed one: http://harryroseman.com
.. _Buildout: http://pypi.python.org/pypi/zc.buildout
.. _Cloud: http://rackspacecloud.com
.. _SourceForge: http://sourceforge.net/projects/plone/
.. _hard to find: http://downloads.sourceforge.net/project/plone/OldFiles/Plone-2.1.4.tar.gz
.. _here: http://dist.plone.org/archive/
.. _Rackspace Cloud: http://rackspacecloud.com
.. _Silver Lining: http://cloudsilverlining.org
.. _if you want to use Silver Lining, Silver Lining is not for you: http://cloudsilverlining.org/#who-should-use-silver-lining
.. _Slicehost: http://www.slicehost.com/
.. _Zope 2 is not supported: http://cloudsilverlining.org/#the-application
.. _repoze.zope2: http://repoze.org/quickstart.html#repoze.zope2
.. _Nate Aune: http://jazkarta.com
.. _Plone Symposium East: http://weblion.psu.edu/events/plone-symposium-east-2010
.. _`http://svn.aclark.net/svn/public/buildout/plone/branches/3.x-wsgi/`: http://svn.aclark.net/svn/public/buildout/plone/branches/3.x-wsgi/
.. _`http://svn.aclark.net/svn/public/buildout/plone/branches/2.1.x/`: http://svn.aclark.net/svn/public/buildout/plone/branches/2.1.x/
.. _README.txt: http://svn.aclark.net/svn/public/buildout/plone/branches/2.1.x/README.txt
