Plone Add-On Development for "Unix Hackers"
===========================================

:date: Sun May 31 10:12:03 EDT 2015
:tags: Plone, Python

With Plone 5 heating up, it's time for me to go "all in" on Plone again. To that end, here's a new tutorial for "Unix Hackers"; i.e. **command-line savvy developers who may be totally unfamiliar with Python but want to learn Plone**.

Assumptions & Caveats
---------------------

Namespace packages
~~~~~~~~~~~~~~~~~~

I don't particularly like the overhead associated with namespace packages in Python; I frequently avoid them. That said, I'm comfortable-enough with their existence in Python to adhere to their (over?) usage in Plone. Feel free to skip them, but in this tutorial I'll use a namespace package because that's what you will encounter in the real world. In this case, skipping them would mean using the package name "hello_world" instead of "hello.world". The former has no namespace, the latter has the namespace "hello" (With hello.world released, I could later support development and release of hello.there, hello.nasty, hello.goodbye, etc.)


Code generators
~~~~~~~~~~~~~~~

I don't particularly like code/template generators either. But I appreciate their value and occassionally use them. That said, I'd rather have none than a bad one or worse, more than one. 

.. raw:: html

    <script src="https://gist.github.com/aclark4life/ffcea3a79b6339591c24.js"></script>
