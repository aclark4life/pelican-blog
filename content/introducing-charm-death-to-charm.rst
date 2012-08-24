Introducing charm; death to charm!
##################################
:date: 2011-03-29 17:20
:category: Plone

[caption id="attachment\_2290" align="alignright" width="373"
caption="First slide of my talk, from "back in the day"
(http://blip.tv/file/761624/)"]`|image0|`_\ [/caption]

A long time ago (several years ago, or more) one of my first Plone jobs
was importing content from the file system (put there by another CMS) to
a client's Plone 2.5 website (see: `http://blip.tv/file/761624/`_).

Some time later (last year or so) the client decided they wanted to
scoop up even more content from the file system (we only grabbed the
last few years prior to launch!)

Unfortunately, the old migration code was truly a horror. So I've been
having a hard time making myself run it again (I was just learning
Python at the time.)

About charm
-----------

This is where *charm* comes in; formerly `mr.importer`_, formerly
`parse2plone`_. Get it? The third time is a… I had the "big idea" to
rewrite, then open source the code I wrote for the client.
Unfortunately, the rewrite became a horror too.

.. raw:: html

   </p>

First, it was not well received amongst the more reusable approaches
based on `collective.transmogrifier`_, and rightfully so. While it was
unpleasant to be told I was heading in the wrong direction, it was
***even more*** unpleasant to find out "they" were right. :-)

Second, as "they" predicted, I got to the point where I couldn't read or
maintain it any more (and I ***just*** wrote it).

So, I decided to revert to a version which had much fewer configuration
options, because making it configurable became a huge distraction.
What's left is:

-  The code is "readable", for some value of readable (PEP8/pyflakes
   compliant) and it's in a single module: `charm.py`_.
-  The concept is "simple", for some value of simple; it's a recipe that
   creates a script for you, that you run via:

::

    $ bin/plone run bin/charm /path/to/files

-  The results are "impressive" for some value of impressive; it imports
   content from the file system into Plone:

::

    2011-03-21 11:51:20,302 - charm - INFO - Imported 19 folders,
    1 images, 20 pages, and 2 files.

-  It won't crash (!), for some value of "keeps going"; it tries to do
   try/except on operations more likely to fail  e.g. create\_parts (via
   --ignore-errors). This aims to ensure you at least get some content
   in your site post-execution.

::

    $ bin/plone run bin/charm html --ignore-errors
    ...
    2011-03-22 07:24:32,821 - charm - INFO - creating folder 'id' inside
                              parent folder '/Plone'
    2011-03-22 07:24:32,822 - charm - INFO - Keep going! Ignoring error
                              'The id "id" is invalid - it is already in use.'

-  It has some tests, 34% coverage at the time of this writing:

::

    619    34%   charm   (/Users/aclark/Developer/charm/charm.py)

-  Has "cool" features, for some value of cool. Most notably, the
   "collapse" feature (AKA "slugify"):

::

    $ bin/plone run bin/charm html --collapse
    ...
    2011-03-22 07:13:28,673 - charm - INFO - path 'html/2011/01/01/test-collapse',
                              has subdirs '', and files 'index.html'
    ...
    2011-03-22 07:13:28,693 - charm - INFO - object 'test-collapse-20110101.html'
                              does not exist inside '/Plone'
    2011-03-22 07:13:28,693 - charm - INFO - creating page 'test-collapse-20110101.html'
                              inside parent folder '/Plone'

-  And the "publish" feature to optionally publish content after
   creation:

::

    $ bin/plone run bin/charm html --collapse --publish
    ...
    2011-03-22 07:13:29,008 - charm - INFO - publishing page 'test-collapse-20110101.html'

And a few more things, but as you can see we are quickly approaching the
point where more functionality does not necessarily mean better
software. It's hard to build something complex AND make it easy to use,
which is why I am moving on.

Charming demo
-------------

In writing this blog entry and releasing charm 1.0b4 I wanted to make
sure to demonstrate how it works, so here is a screencast. This is how I
envision content importing should work in Plone (or at least this is how
I envision a "simple" way it could work.)

.. raw:: html

   </p>

[caption id="attachment\_2312" align="aligncenter" width="478"
caption="Click to watch screencast"]\ `|image1|`_\ [/caption]

After charm
-----------

After I began writing *charm*, I began to collaborate with Dylan Jay on
funnelweb and beyond (e.g. `mr.migrator`_). And I am now more determined
than ever to write reusable code.

.. raw:: html

   </p>

.. _|image2|: http://aclark4life.files.wordpress.com/2011/03/screen-shot-2011-03-22-at-7-56-17-am.png
.. _`http://blip.tv/file/761624/`: http://blip.tv/file/761624/
.. _mr.importer: http://pypi.python.org/pypi/mr.importer
.. _parse2plone: http://pypi.python.org/pypi/parse2plone
.. _collective.transmogrifier: http://pypi.python.org/pypi/collective.transmogrifier
.. _charm.py: https://github.com/collective/charm/blob/master/charm.py
.. _|image3|: http://blip.tv/file/4950056
.. _mr.migrator: https://github.com/collective/mr.migrator

.. |image0| image:: http://aclark4life.files.wordpress.com/2011/03/screen-shot-2011-03-22-at-7-56-17-am.png
.. |image1| image:: http://aclark4life.files.wordpress.com/2011/03/screen-shot-2011-03-29-at-5-04-01-pm.png
.. |image2| image:: http://aclark4life.files.wordpress.com/2011/03/screen-shot-2011-03-22-at-7-56-17-am.png
.. |image3| image:: http://aclark4life.files.wordpress.com/2011/03/screen-shot-2011-03-29-at-5-04-01-pm.png
