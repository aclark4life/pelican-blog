Getting excited about Plone as eggs
###################################
:date: 2008-12-15 12:17
:tags: Plone

.. raw:: html

   <div class="portalMessage">

.. raw:: html

   <div style="color:black;">

Updated for 4.x

.. raw:: html

   </div>

.. raw:: html

   </div>

I'm really excited about this, as it greatly simplifies the development
and deployment story for `Plone`_. For example, you can now create a
Plone buildout.cfg file as follows:

::

    [buildout]
    extends =
        http://dist.plone.org/release/4.0a1/versions.cfgversions = versions
    find-links = http://dist.plone.org/thirdparty/PILwoTk-1.1.6.4.tar.gz
    parts =
        instance[instance]
    recipe = plone.recipe.zope2instance
    user = admin:admin
    eggs =
        PILwoTk
        Plone

For full instructions, see:
`http://svn.aclark.net/svn/public/buildout/plone/trunk/README.txt`_

.. raw:: html

   </p>

Thanks framework team and core developers for this impressive release!

.. _Plone: http://plone.org
.. _`http://svn.aclark.net/svn/public/buildout/plone/trunk/README.txt`: http://svn.aclark.net/svn/public/buildout/plone/trunk/README.txt
