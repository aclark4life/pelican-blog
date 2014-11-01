Plone Secrets Episode 1 Site Actions Contact Link
=================================================

:date: 2011-06-20 12:31
:tags: Plone

Today I am introducing a new category of blog entry called **Plone secrets**.

The goal is to describe a set of developer/integrator techniques that are extremely valuable, but completely non-obvious to newcomers.

The first episode, called: **Site actions contact link**, is really just a technique that involves the Zope Management Interface, Plone interface, file system, Diazo, and quite possibly a few other technologies. This is no secret, but certainly convoluted. Noticeably absent is anything Python-related, unless you count the `plonetheme.aclarknet` namespace package.

We begin by pointing your attention to the new "Contact us today!" link on aclark.net.

This is a gratuitous rip off of any Plone firm's website that has contact info in the upper right of their site (e.g.  http://sixfeetup.com).

I knew I wanted to do "my version" of adding contact info to the upper right, and I think I've seen someone use this exact technique somewhere else (I would credit them if I could remember.)

Long story short: Plone 4's sunburst theme has a nice JavaScript drop down menu for the personal tools menu. As long as I was willing to give up a link to the login form (which I don't like displaying on public sites anyway), I could use this JavaScript menu to quickly and easily provide a link to my contact form.

It "only" required the following:

Step 1
------

-  Get the personal tools menu to show up in my site. This was accomplished via the following Diazo rule:

::

    <prepend content='//*[@id="portal-personaltools"]'
         theme='//*[@id="search"]' />

Note also that I am using the early-supported XPath syntax, but the more friendly CSS syntax is supported now too. See http://diazo.org for more information.

For the full set of Diazo rules for this site, see here:

-  Plone: https://github.com/ACLARKNET/aclark_net_website/blob/master/src/plonetheme.aclarknet/plonetheme/aclarknet/theme/aclarknet/rules.xml
-  Wordpress: https://github.com/ACLARKNET/aclark_net_website/blob/master/theme/blog.xml

Step 2
------

Next, we need to create and display only the "Contact us today!" link, which also involves disabling the "Log in" link. These tricks can be performed in the Zope Management Interface via the portal_actions tool.

First, browse to `Site Setup -> Zope Management Interface -> portal_actions -> user` and create a `contact` action.

Fill in the appropriate fields and click `Save changes`.

Finally, hide the `Log in` action by unchecking `Visible` and clicking `Save changes`.

Step 3
------

Lastly and most importantly, persist your work on the file system outside of the database. You don't want to be forced to recreate this site action ever again through the web.

This involves exporting the action via portal setup, and adding it to your package's GenericSetup profile. Browse to `Site Setup -> Zope Management Interface -> portal_setup -> Export. Check the `Action providers` step.

Then scroll all the way down to bottom and click `Export selected steps`.

This will give you a tarred/gzipped file that when extracted will give you an `actions.xml` file. Edit this file to include only the action you created, like so:

::

    <?xml version="1.0"?> </object>
    </object>

You can find this file in its entirety here:

- https://github.com/ACLARKNET/aclark_net_website/blob/master/src/plonetheme.aclarknet/plonetheme/aclarknet/profiles/default/actions.xml

You also have to register a default profile in your package with ZCML (more technology!), like so:

::

    <genericsetup:registerProfile
     name="default"
     title="ACLARK.NET, LLC profile"
     description="Installs ACLARK.NET, LLC site customizations"
     directory="profiles/default"
     provides="Products.GenericSetup.interfaces.EXTENSION"
     />

You can find this file in its entirety here:

- https://github.com/ACLARKNET/aclark_net_website/blob/master/src/plonetheme.aclarknet/plonetheme/aclarknet/configure.zcml

Step 4
------

Style the results. This is more like Step 3.5, but still important.  Because we are doing Diazo theming, styling is easy. It's just a matter of editing the style sheet on the file system like you would expect to do in any web project. Of course, you need to know a bit about CSS and the CSS ids that Plone uses:

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

- https://github.com/ACLARKNET/aclark_net_website/blob/master/src/plonetheme.aclarknet/plonetheme/aclarknet/theme/aclarknet/static/css/plone.css#L519

And of course, these styles apply to the public facing site.

Results
-------

That's it!

I hope this post captures the essence of why I think many folks may be intimidated by Plone: in more cases than not, one must understand way too many technologies in order to get the job done. I hope to continue to demystify Plone through a series of "Plone secrets" posts, and ultimately I think the Plone project hopes to resolve these issues once and for all, however long that takes.

I will speculate that long term Plone will move away from Zope 2, and everything from the Zope Management Interface that was useful will be recreated in Plone (i.e. ported). Or rather, that is what I would like to see happen.
