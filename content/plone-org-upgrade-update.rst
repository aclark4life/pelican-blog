Plone.org upgrade update!
================================================================================

:date: 2008-05-01 11:53
:tags: Plone

Thanks again to everyone who contributed to my travel fund. I really appreciate it and being able to work closely with Tarek Ziadé and Matthew Wilkes on PloneSoftwareCenter and PloneOrg was amazing, productive, and fun. Of course being in the company of all the sprinters was a pleasure, and thank you Christophe for the hospitality! The sprint was "successful" in that we got a lot done. See:

-  `http://dev.plone.org/plone/log/PloneOrg/buildouts/trunk/devel`_ and
-  `http://dev.plone.org/collective/log/Products.PloneSoftwareCenter/branches-tarek-distutils-ids`_

for the details.  In short,

-  Matthew and Tarek worked on getting PloneSoftwareCenter ready to host eggs.
-  I worked on creating and configuring the new site instance.
-  Steve McMahon and I egg-i-fied the remaining product dependencies.

Unfortunately, there is still a lot more to do:

-  We need help with `ExternalStorage`_. The problem is too many objects in the ZODB with too many different filesystem paths. In the worst case scenario I can script a fix to set a new filesystem path for the existing objects, but I'm hoping to avoid this. Ideally we'll support a pluggable storage feature that will allow end users to choose between blob, ExternalStorage, and FileSystemStorage, etc.
-  We need to finish the new PloneSoftwareCenter implementation. See `http://dev.plone.org/collective/log/collective.psc.mirroring`_ for more information.
-  We need to test the new PloneSoftwareCenter implementation. Lots of people with lots of buildouts will hopefully not mean lots of problems for the server.
-  I need to finish the nginx and varnish setup (package as .debs).

In the meantime, I've made the \*\*LARGELY NOT FUNCTIONAL\*\* new instance available at `http://new.plone.org`_ for anyone that is interested. Please be aware of the following:

-  Be kind. This is \*just\* Zope. No apache, varnish, nginx. etc. Just Zope.
-  You cannot login. LDAP has not been hooked up yet.
-  This is not the \*real\* content. We will cut off plone.org and drop in the latest Data.fs (and go through all the TTW migration steps again) when we are ready to launch.

I'm targeting the end of May to launch the \*real\* new site. Sorry for the delay (I promised end of April!) Needless to say, I will be actively working on finishing everything between now and then.

We will be remote sprinting in #psc on irc.freenode.net this Sunday @ 2:00PM EDT if you would like to join us!

.. _`http://dev.plone.org/plone/log/PloneOrg/buildouts/trunk/devel`: http://dev.plone.org/plone/log/PloneOrg/buildouts/trunk/devel
.. _`http://dev.plone.org/collective/log/Products.PloneSoftwareCenter/branches-tarek-distutils-ids`: http://dev.plone.org/collective/log/Products.PloneSoftwareCenter/branches-tarek-distutils-ids
.. _ExternalStorage: http://dev.plone.org/collective/browser/ExternalStorage
.. _`http://dev.plone.org/collective/log/collective.psc.mirroring`: http://dev.plone.org/collective/log/collective.psc.mirroring
.. _`http://new.plone.org`: http://new.plone.org
