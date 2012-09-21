test-plone `tmp`
################
:date: 2012-04-04 14:14
:tags: Plone, Python

Since Day 1 with Plone circa 2004, I've always taken pride in and
greatly enjoyed refining my development environment. It's been stable
for a while now (> 1 year or so) so I thought I'd share.

Operating system
================

Mac OS X Latest (Lion, at the time of this writing)

Terminal
========

Mac OS X Terminal

Editor
======

Vim

Python
======

Yes. All versions, via the collective Python buildout:

-  `https://github.com/collective/buildout.python`_

Plone
=====

Yes. All versions, via pythonpackages.com:

-  `http://docs.pythonpackages.com/en/latest/advanced.html`_

Additional tools
================

A `shell script to run virtualenv, buildout, etc`_:

.. raw:: html

   </p>

[bash] #!/bin/sh if ! [ -n "$1" ] then echo "Usage:nn$0 <dir>n" exit 1
fi if ! [ -d $1 ] then mkdir $1 fi cd $1 virtualenv-2.7 . bin/pip
install zc.buildout bin/buildout init cat << EOF > buildout.cfg
[buildout] extends =
http://build.pythonpackages.com/buildout/plone/4.2.x-dev EOF
bin/buildout bin/plone start sleep 4 echo "Adding Plone site..." curl -d
form.submitted:boolean="True"
http://admin:admin@localhost:8080/@@plone-addsite?site\_id=Plone
bin/plone stop bin/plone fg [/bash]

A `Python script to create temporary directories`_:

[python] #!/usr/bin/env python

import os import tempfile print os.path.abspath(tempfile.mkdtemp())
[/python]

.. raw:: html

   <p>

A default buildout config file:

::

    [buildout]
    eggs-directory = /Users/aclark/Developer/eggs-directory
    download-cache = /Users/aclark/Developer/download-cache
    extends-cache = /Users/aclark/Developer/extends-cache

.. raw:: html

   </p>

Workflow
========

My typical workflow looks like this:

-  Hang in #plone on irc.freenode.net and wait for questions
-  Hear question and get inspired to run Plone
-  Run: **$ test-plone \`tmp\`**

`~ 1 minute later`_ I'm browsing **http://localhost:8080/Plone** and can
install add-ons, check ZMI settings, etc.

.. raw:: html

   </p>

`|image0|`_

Enjoy.

.. _`https://github.com/collective/buildout.python`: https://github.com/collective/buildout.python
.. _`http://docs.pythonpackages.com/en/latest/advanced.html`: http://docs.pythonpackages.com/en/latest/advanced.html
.. _shell script to run virtualenv, buildout, etc: https://github.com/aclark4life/binfiles/blob/master/test-plone
.. _Python script to create temporary directories: https://github.com/aclark4life/binfiles/blob/master/tmp
.. _~ 1 minute later: https://gist.github.com/2304317
.. _|image1|: http://aclark4life.files.wordpress.com/2012/04/screen-shot-2012-04-04-at-3-19-27-pm.png

.. |image0| image:: http://aclark4life.files.wordpress.com/2012/04/screen-shot-2012-04-04-at-3-19-27-pm.png
.. |image1| image:: http://aclark4life.files.wordpress.com/2012/04/screen-shot-2012-04-04-at-3-19-27-pm.png
