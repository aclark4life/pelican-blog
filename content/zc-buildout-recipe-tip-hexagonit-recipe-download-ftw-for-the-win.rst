zc.buildout recipe tip: hexagonit.recipe.download FTW! (For the win)
####################################################################
:date: 2007-11-28 21:36
:tags: Plone

Sometimes an "old style" product is distributed as foo.tar.gz and
extracts to foo/, but the product is actually called Bar! This can be a
problem when using the **plone.recipe.productdistros** recipe because
when 'Bar' is extracted to parts/productdistros/foo, it will not work.

Fortunately, there is **hexagonit.recipe.download**, which allows you to
specify a destination. For example, **ZNagios** (an add-on product that
integrates Zope with Nagios) is available as a tarball here:

-  `http://svn.gocept.com/viewcvs/ZNagios/trunk.tar.gz?view=tar`_

If we use productdistros, we end up with ZNagios installed in
parts/productdistros/trunk. No good. But if we use
hexagonit.recipe.download we can control the destination. e.g.

::

    [buildout]
    parts =
        ...
        znagios[znagios]
    recipe = hexagonit.recipe.download
    url = http://svn.gocept.com/viewcvs/ZNagios/trunk.tar.gz?view=tar
    destination = products/ZNagios
    strip-top-level-dir = True

After running buildout, you should have the following in your buildout
products/ directory:

::

    /products/ZNagios
    /products/ZNagios/COPYRIGHT.txt
    /products/ZNagios/LICENSE.txt
    /products/ZNagios/README.txt
    /products/ZNagios/__init__.py
    /products/ZNagios/check_zope.py
    /products/ZNagios/munin_client.py
    /products/ZNagios/version.txt
    /products/ZNagios/zeo_munin.py
    /products/ZNagios/zope.cfg

As always, there are `better ways to do this`_ but getting it done is
nice too. Comments welcome! :-)

.. raw:: html

   </p>

.. _`http://svn.gocept.com/viewcvs/ZNagios/trunk.tar.gz?view=tar`: http://svn.gocept.com/viewcvs/ZNagios/trunk.tar.gz?view=tar
.. _better ways to do this: http://dev.plone.org/plone/changeset/21090
