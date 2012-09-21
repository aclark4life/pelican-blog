Zope2 Bootstrap
###############
:date: 2012-06-12 10:27
:tags: Plone, Python
:category: Plone

*Bootstrap all the things, including Zope2.*

`zope2\_bootstrap`_ is a new Python package that `monkey patches`_ Zope2
in order to:

-  Replace `manage\_page\_styles.css.dtml`_ styles with `Twitter
   Bootstrap`_ styles.
-  Adds CSS classes to `main`_ and/or `manage\_main`_ tables.
-  Inserts a Plone logo (if Plone is installed) above
   `manage\_tabs.dtml`_ tabs (h/t:
   `https://github.com/plone/Products.CMFPlone/blob/master/Products/CMFPlone/patches/addzmiplonesite.py`_).
-  Inserts a ZMI warning (if Plone is installed) below
   `manage\_tabs.dtml`_ tabs.

`|image0|`_

.. raw:: html

   </p>

`|image1|`_

In the next version, I'll try to import `Twitter Bootstrap JavaScript`_
for even more goodness. Enjoy, and give feedback in the comments, or
`here`_.

.. _zope2\_bootstrap: http://pypi.python.org/pypi/zope2_bootstrap
.. _monkey patches: http://pypi.python.org/pypi/collective.monkeypatcher
.. _manage\_page\_styles.css.dtml: http://zope3.pov.lt/trac/browser/Zope/trunk/src/App/dtml/manage_page_style.css.dtml
.. _Twitter Bootstrap: http://twitter.github.com/bootstrap/base-css.html
.. _main: http://zope3.pov.lt/trac/browser/Zope/trunk/src/OFS/dtml/main.dtml
.. _manage\_main: http://zope3.pov.lt/trac/browser/Products.ExternalEditor/trunk/Products/ExternalEditor/manage_main.dtml
.. _manage\_tabs.dtml: http://zope3.pov.lt/trac/browser/Products.ExternalEditor/trunk/Products/ExternalEditor/manage_tabs.dtml
.. _`https://github.com/plone/Products.CMFPlone/blob/master/Products/CMFPlone/patches/addzmiplonesite.py`: https://github.com/plone/Products.CMFPlone/blob/master/Products/CMFPlone/patches/addzmiplonesite.py
.. _|image2|: http://aclark4life.files.wordpress.com/2012/06/screenshot1.png
.. _|image3|: http://aclark4life.files.wordpress.com/2012/06/screenshot.png
.. _Twitter Bootstrap JavaScript: http://twitter.github.com/bootstrap/javascript.html
.. _here: https://github.com/aclark4life/zope2_bootstrap/issues

.. |image0| image:: http://aclark4life.files.wordpress.com/2012/06/screenshot1.png
.. |image1| image:: http://aclark4life.files.wordpress.com/2012/06/screenshot.png
.. |image2| image:: http://aclark4life.files.wordpress.com/2012/06/screenshot1.png
.. |image3| image:: http://aclark4life.files.wordpress.com/2012/06/screenshot.png
