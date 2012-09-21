Plone secrets: Episode 1 — Site actions contact link
####################################################
:date: 2011-06-20 12:31
:tags: Plone

Today I am introducing a new category of blog entry called **Plone
secrets**.

The goal is to describe a set of developer/integrator techniques that
are extremely valuable, but completely non-obvious to newcomers.

The first episode, called: **Site actions contact link**, is really just
a technique that involves the Zope Management Interface, Plone
interface, file system, Diazo, and quite possibly a few other
technologies. This is no secret, but certainly convoluted. Noticeably
absent is anything Python-related, unless you count the
\`plonetheme.aclarknet\` namespace package.

We begin by pointing your attention to the new "Contact us today!" link
on aclark.net.

`|image0|`_

This is a gratuitous rip off of any Plone firm's website that has
contact info in the upper right of their site (e.g.
http://sixfeetup.com).

.. raw:: html

   </p>

I knew I wanted to do "my version" of adding contact info to the upper
right, and I think I've seen someone use this exact technique somewhere
else (I would credit them if I could remember.)

Long story short: Plone 4's sunburst theme has a nice JavaScript drop
down menu for the personal tools menu. As long as I was willing to give
up a link to the login form (which I don't like displaying on public
sites anyway), I could use this JavaScript menu to quickly and easily
provide a link to my contact form.

It "only" required the following:

Step 1
======

-  Get the personal tools menu to show up in my site. This was
   accomplished via the following Diazo rule:

::

    <prepend content='//*[@id="portal-personaltools"]'
         theme='//*[@id="search"]' />

Note also that I am using the early-supported XPath syntax, but the more
friendly CSS syntax is supported now too. See `http://diazo.org`_ for
more information.

.. raw:: html

   </p>

For the full set of Diazo rules for this site, see here:

-  Plone:
   `https://github.com/ACLARKNET/aclark\_net\_website/blob/master/src/plonetheme.aclarknet/plonetheme/aclarknet/theme/aclarknet/rules.xml`_
-  Wordpress:
   `https://github.com/ACLARKNET/aclark\_net\_website/blob/master/theme/blog.xml`_

Step 2
======

Next, we need to create and display only the "Contact us today!" link,
which also involves disabling the "Log in" link. These tricks can be
performed in the Zope Management Interface via the portal\_actions tool.

.. raw:: html

   </p>

First, browse to \`Site Setup -> Zope Management Interface ->
portal\_actions -> user\` and create a \`contact\` action:

`|image1|`_

Fill in the appropriate fields and click \`Save changes\`:

`|image2|`_

Finally, hide the \`Log in\` action by unchecking \`Visible\` and
clicking \`Save changes\`:

`|image3|`_

Step 3
======

Lastly and most importantly, persist your work on the file system
outside of the database. You don't want to be forced to recreate this
site action ever again through the web.

.. raw:: html

   </p>

This involves exporting the action via portal setup, and adding it to
your package's GenericSetup profile. Browse to \`Site Setup -> Zope
Management Interface -> portal\_setup -> Export. Check the \`Action
providers\` step:

`|image4|`_

Then scroll all the way down to bottom and click \`Export selected
steps\`:

`|image5|`_

 

This will give you a tarred/gzipped file that when extracted will give
you an \`actions.xml\` file. Edit this file to include only the action
you created, like so:

.. raw:: html

   <p>

 

::

    <?xml version="1.0"?> </object>
    </object>

You can find this file in its entirety here:

-  `https://github.com/ACLARKNET/aclark\_net\_website/blob/master/src/plonetheme.aclarknet/plonetheme/aclarknet/profiles/default/actions.xml`_

You also have to register a default profile in your package with ZCML
(more technology!), like so:

::

    <genericsetup:registerProfile
     name="default"
     title="ACLARK.NET, LLC profile"
     description="Installs ACLARK.NET, LLC site customizations"
     directory="profiles/default"
     provides="Products.GenericSetup.interfaces.EXTENSION"
     />

You can find this file in its entirety here:

-  `https://github.com/ACLARKNET/aclark\_net\_website/blob/master/src/plonetheme.aclarknet/plonetheme/aclarknet/configure.zcml`_

Step 4
======

Style the results. This is more like Step 3.5, but still important.
Because we are doing Diazo theming, styling is easy. It's just a matter
of editing the style sheet on the file system like you would expect to
do in any web project. Of course, you need to know a bit about CSS and
the CSS ids that Plone uses:

::

    #personaltools-contact {
        color: #AA001F;
        background: white;
        text-transform: uppercase;
        font-size: 150%;
    }
    #portal-personaltools {
        background: white;
    }

You can find this file in its entirety here:

-  `https://github.com/ACLARKNET/aclark\_net\_website/blob/master/src/plonetheme.aclarknet/plonetheme/aclarknet/theme/aclarknet/static/css/plone.css#L519`_

And of course, these styles apply to the public facing site.

.. raw:: html

   </p>

`|image6|`_

Results
=======

On a new Plone site, the option to install this customization will look
like so:

.. raw:: html

   </p>

`|image7|`_

And the action will look like this, when you are logged in (else you
will see only the "Contact us today!" link):

`|image8|`_

That's it!

I hope this post captures the essence of why I think many folks may be
intimidated by Plone: in more cases than not, one must understand way
too many technologies in order to get the job done. I hope to continue
to demystify Plone through a series of "Plone secrets" posts, and
ultimately I think the Plone project hopes to resolve these issues once
and for all, however long that takes.

I will speculate that long term Plone will move away from Zope 2, and
everything from the Zope Management Interface that was useful will be
recreated in Plone (i.e. ported). Or rather, that is what I would like
to see happen.

.. _|image9|: http://aclark4life.files.wordpress.com/2011/06/screen-shot-2011-06-19-at-11-26-09-pm.png
.. _`http://diazo.org`: http://diazo.org
.. _`https://github.com/ACLARKNET/aclark\_net\_website/blob/master/src/plonetheme.aclarknet/plonetheme/aclarknet/theme/aclarknet/rules.xml`: https://github.com/ACLARKNET/aclark_net_website/blob/master/src/plonetheme.aclarknet/plonetheme/aclarknet/theme/aclarknet/rules.xml
.. _`https://github.com/ACLARKNET/aclark\_net\_website/blob/master/theme/blog.xml`: https://github.com/ACLARKNET/aclark_net_website/blob/master/theme/blog.xml
.. _|image10|: http://aclark4life.files.wordpress.com/2011/06/screen-shot-2011-06-20-at-11-00-56-am1.png
.. _|image11|: http://aclark4life.files.wordpress.com/2011/06/screen-shot-2011-06-20-at-11-06-44-am.png
.. _|image12|: http://aclark4life.files.wordpress.com/2011/06/screen-shot-2011-06-20-at-11-14-05-am.png
.. _|image13|: http://aclark4life.files.wordpress.com/2011/06/screen-shot-2011-06-20-at-11-24-11-am.png
.. _|image14|: http://aclark4life.files.wordpress.com/2011/06/screen-shot-2011-06-20-at-11-24-28-am1.png
.. _`https://github.com/ACLARKNET/aclark\_net\_website/blob/master/src/plonetheme.aclarknet/plonetheme/aclarknet/profiles/default/actions.xml`: https://github.com/ACLARKNET/aclark_net_website/blob/master/src/plonetheme.aclarknet/plonetheme/aclarknet/profiles/default/actions.xml
.. _`https://github.com/ACLARKNET/aclark\_net\_website/blob/master/src/plonetheme.aclarknet/plonetheme/aclarknet/configure.zcml`: https://github.com/ACLARKNET/aclark_net_website/blob/master/src/plonetheme.aclarknet/plonetheme/aclarknet/configure.zcml
.. _`https://github.com/ACLARKNET/aclark\_net\_website/blob/master/src/plonetheme.aclarknet/plonetheme/aclarknet/theme/aclarknet/static/css/plone.css#L519`: https://github.com/ACLARKNET/aclark_net_website/blob/master/src/plonetheme.aclarknet/plonetheme/aclarknet/theme/aclarknet/static/css/plone.css#L519
.. _|image15|: http://aclark4life.files.wordpress.com/2011/06/screen-shot-2011-06-20-at-2-49-19-pm.png
.. _|image16|: http://aclark4life.files.wordpress.com/2011/06/screen-shot-2011-06-20-at-12-19-01-pm.png
.. _|image17|: http://aclark4life.files.wordpress.com/2011/06/screen-shot-2011-06-20-at-12-07-46-pm.png

.. |image0| image:: http://aclark4life.files.wordpress.com/2011/06/screen-shot-2011-06-19-at-11-26-09-pm.png
.. |image1| image:: http://aclark4life.files.wordpress.com/2011/06/screen-shot-2011-06-20-at-11-00-56-am1.png
.. |image2| image:: http://aclark4life.files.wordpress.com/2011/06/screen-shot-2011-06-20-at-11-06-44-am.png
.. |image3| image:: http://aclark4life.files.wordpress.com/2011/06/screen-shot-2011-06-20-at-11-14-05-am.png
.. |image4| image:: http://aclark4life.files.wordpress.com/2011/06/screen-shot-2011-06-20-at-11-24-11-am.png
.. |image5| image:: http://aclark4life.files.wordpress.com/2011/06/screen-shot-2011-06-20-at-11-24-28-am1.png
.. |image6| image:: http://aclark4life.files.wordpress.com/2011/06/screen-shot-2011-06-20-at-2-49-19-pm.png
.. |image7| image:: http://aclark4life.files.wordpress.com/2011/06/screen-shot-2011-06-20-at-12-19-01-pm.png
.. |image8| image:: http://aclark4life.files.wordpress.com/2011/06/screen-shot-2011-06-20-at-12-07-46-pm.png
.. |image9| image:: http://aclark4life.files.wordpress.com/2011/06/screen-shot-2011-06-19-at-11-26-09-pm.png
.. |image10| image:: http://aclark4life.files.wordpress.com/2011/06/screen-shot-2011-06-20-at-11-00-56-am1.png
.. |image11| image:: http://aclark4life.files.wordpress.com/2011/06/screen-shot-2011-06-20-at-11-06-44-am.png
.. |image12| image:: http://aclark4life.files.wordpress.com/2011/06/screen-shot-2011-06-20-at-11-14-05-am.png
.. |image13| image:: http://aclark4life.files.wordpress.com/2011/06/screen-shot-2011-06-20-at-11-24-11-am.png
.. |image14| image:: http://aclark4life.files.wordpress.com/2011/06/screen-shot-2011-06-20-at-11-24-28-am1.png
.. |image15| image:: http://aclark4life.files.wordpress.com/2011/06/screen-shot-2011-06-20-at-2-49-19-pm.png
.. |image16| image:: http://aclark4life.files.wordpress.com/2011/06/screen-shot-2011-06-20-at-12-19-01-pm.png
.. |image17| image:: http://aclark4life.files.wordpress.com/2011/06/screen-shot-2011-06-20-at-12-07-46-pm.png
