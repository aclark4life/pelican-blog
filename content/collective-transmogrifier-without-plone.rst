collective.transmogrifier without Plone?
########################################
:date: 2011-04-15 20:31
:tags: Plone

Yes!

Since I began drinking the `collective.transmogrifier`_ Kool Aid a few
months back, I've gotten quite excited about the possibility of being
able to use it outside Plone, i.e. like "regular" Python people would
do.

It just so happens I have a current project that requires me to import
content to Plone 2.5; it took me a while to realize I could just setup a
Plone 4 instance, run transmogrifier in it, and import content from it
(i.e. from the file system) to Plone 2.5 over XML-RPC. But something
about having to include Plone 4 in that scenario rubbed me the wrong
way: Plone 4 is not needed, it's just executing the pipeline.

*(I also don't like the idea of having to create a Python package and a
GenericSetup profile in order to facilitate a migration.)*

Goals
-----

So in addition to working on getting `mr.migrator`_ to be able to
configure and execute pipelines (currently only GenericSetup profiles
and Python code are supported), I thought I'd experiment with removing
the CMFCore dependency.

The initial, *experimental* results can be seen in action here:

-  `https://github.com/aclark4life/mr\_migrator\_demo`_

From the `README`_:

::

    Introduction
    ============This demo is:* Proof of concept for mr.migrator: A tool that provides the ability to
      register and execute collective.transmogrifier pipelines without creating a
      Python package. It's Miller Time™.* Also proof of concept for collective.transmogrifier with the CMFCore
      dependency removed (and a zope.component dependency added in its place).
      It's Scotch time™.Explanation
    -----------In order to work, it currently relies on:* https://svn.plone.org/svn/collective/collective.transmogrifier/branches/aclark-mr-migrator-compat
    * https://svn.plone.org/svn/collective/transmogrify.filesystem/branches/aclark-mr-migrator-compat
    * git@github.com:aclark4life/transmogrify.ploneremote.git These are, respectively:* A branch of c.transmogrifier with a setuptools entry point plugin system
      added, and the CMFCore dependencies removed (gracefully, I hope).* A branch of t.filesystem with the collective.transmogrifier entry point
      specified (and some CMFCore dependencies removed).* A fork of t.ploneremote with the collective.transmogrifier entry point
      specified (and some CMFCore dependencies remove).
    …

It's a work in progress, but it actually imports content. You may try it
locally, as explained in the rest of the `README`_:

::

    Installation
    ------------You can try out this demo::    $ git clone git@github.com:aclark4life/mr_migrator_demo.git
        $ cd mr_migrator_demo
        $ python bootstrap.py
        $ bin/buildoutElsewhere, setup a Plone site listenining on localhost:8080 with a Plone site
    object called "Plone" and then:    $ bin/mr.migratorYou should end up with content in Plone that looks like this:
    …

I hope this helps move the state of the art forward a bit; it would be
great to share this technology with the rest of the Python world. And in
case you are curious about the changes, you can read the revision log
here:

-  `http://dev.plone.org/collective/log/collective.transmogrifier/branches/aclark-mr-migrator-compat`_

Start with the following revision, and click through the next 8 commits:

-  `http://dev.plone.org/collective/changeset/237628/collective.transmogrifier/branches/aclark-mr-migrator-compat`_

Comments welcome.

Credits
-------

Thanks Martijn Pieters for creating collective.transmogrifier; thanks
Martin Aspeli and Dylan Jay for their blueprints; and thanks Dylan Jay
for bringing transmogrifier to the masses via mr.migrator.

.. _collective.transmogrifier: http://pypi.python.org/pypi/collective.transmogrifier
.. _mr.migrator: https://github.com/collective/mr.migrator
.. _`https://github.com/aclark4life/mr\_migrator\_demo`: https://github.com/aclark4life/mr_migrator_demo
.. _README: https://github.com/aclark4life/mr_migrator_demo/raw/master/README.txt
.. _foo: ../wp-content/uploads/2011/04/content.png
.. _|image1|: http://blog.aclark.net/wp-content/uploads/2011/04/content1.png
.. _`http://dev.plone.org/collective/log/collective.transmogrifier/branches/aclark-mr-migrator-compat`: http://dev.plone.org/collective/log/collective.transmogrifier/branches/aclark-mr-migrator-compat
.. _`http://dev.plone.org/collective/changeset/237628/collective.transmogrifier/branches/aclark-mr-migrator-compat`: http://dev.plone.org/collective/changeset/237628/collective.transmogrifier/branches/aclark-mr-migrator-compat

.. |image0| image:: http://blog.aclark.net/wp-content/uploads/2011/04/content1.png
