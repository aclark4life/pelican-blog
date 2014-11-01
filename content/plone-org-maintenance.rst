Plone.org maintenance
================================================================================

:date: 2011-11-29 00:54
:tags: Plone

Plans
-----

I am planning to do some work on the plone.org server and website by the
end of the year, including:

Upgrade to the latest 4.2.x series

Switch from xdv to `plone.app.theming`_

-  Reduce the number of NGINXes running on the server by 1 (we currently have an nginx doing the xdv transform)
-  Repackage the current plone.org theme as plonetheme.ploneorg

Clean up the server

-  Separate vendor package configs from buildout generated configs
-  Remove archived files

Prune tickets on `dev.plone.org`_

I've done some of this work already, earlier this year:

-  `https://github.com/plone/Products.PloneOrg/commits/4.1-compat`_

Pitch
-----

To ensure it gets done by the end of the year, I would like to add this project to my calendar as paid work. So if you are able to help out by donating some portion of the goal, I would appreciate it. Please use the chip-in below to contribute to this effort.

.. _plone.app.theming: http://pythonpackages.com/info/plone.app.theming
.. _dev.plone.org: http://dev.plone.org/
.. _`https://github.com/plone/Products.PloneOrg/commits/4.1-compat`: https://github.com/plone/Products.PloneOrg/commits/4.1-compat
