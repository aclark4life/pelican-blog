New website for 2011!
#####################
:date: 2011-01-19 18:56
:tags: Plone

Edit: In addition to "cool overlays", I added a couple Plone-core todo
items (that I may like to PLIP/implement)

Purpose-driven
--------------

Since `December 23, 2010`_, a new website has been in development at
ACLARK.NET, LLC. It took approximately one month to complete; and we are
proud to present it to the world today! We are particularly proud that
this website can serve a dual-purpose: to make us look good, and to
serve as an example of how easy and fun it is to install and use Plone.

Look ma, no package!
--------------------

One of the requirements I had in developing a new website was that I
would ditch my old Products.aclark\_net package in favor of… nothing.
(Sort of.)

What I mean is, the entire website was developed and deployed within a
single, small buildout:
`https://github.com/aclark4life/aclark\_net\_website`_.

The buildout is meant to be instructional (!) so if you have questions,
please ask them in the comments.

::

    [buildout]
    # Extends import buildout config files from elsewhere
    extends =
    #    http://dist.aclark.net/build/plone/4.1.x/buildout.cfg
        http://dist.aclark.net/build/plone/4.1.x/zeo.cfg
        http://good-py.appspot.com/release/collective.xdv/1.0# Parts define what this buildout does
    parts += trac xdv staging production blog[plone]
    # Eggs are Python packages
    eggs +=
    # "New style" theming in Plone
        collective.xdv
    # "New style" template overrides
        z3c.jbot# Plone is a modern web application that uses the Zope Toolkit
    # internally to provide complex functionality in a manageable way.
    #
    # The Zope Toolkit features the Zope component architecure; and
    # components are configured via the Zope Configuration Markup Language (ZCML).
    #
    # Rather than create a Python package to do simple customizations, we add
    # our ZCML here and the plone.recipe.zope2instance will add it to our
    # Zope 2 instance configuration file(s) for us whenever we run bin/buildout.
    zcml-additional =
    # Add static resource dir
        <configure
            xmlns:browser="http://namespaces.zope.org/browser"
        >
        <browser:resourceDirectory
            name="static"
            directory="${buildout:directory}/static"
        />
    # Add custom templates dir
        <include
            package="z3c.jbot"
            file="meta.zcml"
        />
        <browser:jbot
            directory="${buildout:directory}/templates"
        />
        </configure>[blog]
    # Compile the blog theme
    recipe = plone.recipe.command
    command =
        bin/xdvcompiler -r theme/rules/blog.xml -t theme/templates/blog.html -o theme/blog.xsl
    update-command = ${:command}[trac]
    # Compile the trac theme
    recipe = plone.recipe.command
    command =
        bin/xdvcompiler -r theme/rules/trac.xml -t theme/templates/trac.html -o theme/trac.xsl
    update-command = ${:command}# This creates bin/xdvcompiler
    [xdv]
    recipe = zc.recipe.egg# Hostout makes Fabric integration easy
    [staging]
    recipe = collective.hostout
    host = aclark.net
    path = /srv/staging[production]
    recipe = collective.hostout
    host = aclark.net
    path = /srv/aclark_net_website[versions]
    plone.registry = 1.0b4
    plone.app.registry = 1.0b5

Diazo
-----

For the first time ever, I decided to try deploying Diazo (formerly XDV)
within Plone itself. That meant installing `collective.xdv`_ in Plone
and pointing it to a rules.xml file. This only works for Plone, though.
Wordpress and Trac are still themed outside Plone, by compiling their
themes with xdvcompiler and pointing Apache to the resulting .xsl files.

Content
-------

I am obsessive about content. I am also obsessive about simplicity. And
in today's world of `need-it-now`_, I have become conditioned to "do"
now and ask questions later (which is not always recommended, by the
way). That meant that for this website, rather than migrate content
(which in some cases was contained in custom fields added by Archetypes
schema extender) I opted to setup a "clean" Plone and copy/paste/edit
content.

On a small site like ours, this was a no-brainer for me. But it
definitely exposes a weakness of Plone. Now that theming has improved,
we really need a better "content story". To me, that is starting to mean
focusing on satisfying a "simple" use case like exporting and importing
content in Plone. There are folks `working on this`_ of course, it just
needs to advance to the point where we can offer it in the Plone core
IMHO.

Todo
----

Of course there is always more to do. The first thing that jumps out
that is missing from this deployment is "cool (Javascript) overlays" or
"pop-ups," depending on who you ask. I didn't have time to add them
prior to launch, but I will most likely add them later `because I can`_.

A couple more Plone-core related features I would love to see
implemented (technically, Diazo is not in the core yet):

-  I want to add GenericSetup (GS) profiles outside Python packages
   (i.e. in the buildout via ZCML). Currently GenericSetup expects to be
   passed a context which is (I think) the old-style Zope 2 product
   object in the ZODB. But I can't think of a reason why GS couldn't be
   made to work sans that requirement (I'm just speculating though, I
   haven't looked at the code yet).
-  I wish Diazo (collective.xdv) could be configured via GenericSetup.
   I'd like to configure the path to the rules.xml file in something
   like profiles/default/diazo.xml such that when a Plone site is
   created and the Diazo import step is run, the path to the rules file
   is set automatically.

Conclusion
~~~~~~~~~~

This is certainly one of the most fun times I've head developing a Plone
website (which is nice when you are in the Plone website business). I
attribute that directly to all of the awesome folks involved in the
project. I can't list everyone here, but I will "shout out" to some of
the folks who I think were instrumental in getting us here: Eric Steele
& the entire Plone 4 framework team, for their work on Plone 4. Hanno
Schlichting for making Plone fast again. Martin Aspeli and Laurence Rowe
for Diazo. And David Glick, for being "always on" (and my own personal
devil's advocate).

And really, everyone involved in the Plone project on a day to day
basis. Plone development and consulting can be frustrating at times, but
more often than not it is a magical experience, due in no small part due
to the seemingly never-ending supply of cool and dedicated folks.

A look back
~~~~~~~~~~~

Also, I've been doing this long enough now that it's now very
entertaining (to me at least) to look back at the various incarnations
of the ACLARK.NET, LLC website over the years (these are guestimates):

-  Circa 2006: Plone 2.5 with a Cereblue skin I purchased for $50 :-)
-  Circa 2007: Plone 3.0 with a custom "old style" theme that I designed
   (and I'm not a designer).
-  Circa 2008: Plone 3.3 with XDV (now Diazo) plus "open source" theme.
-  Circa 2011: Plone 4 with collective.xdv, z3c.jbot, and "open source"
   buildout and theme, and nothing else.

To the future
-------------

Onwards Plone team! Here is to 2011.

.. _December 23, 2010: https://github.com/aclark4life/aclark_net_website/commit/514a46a652d9ffb393fd7f83a296306761c995b7
.. _`https://github.com/aclark4life/aclark\_net\_website`: https://github.com/aclark4life/aclark_net_website
.. _collective.xdv: http://pypi.python.org/pypi/collective.xdv
.. _need-it-now: http://twitter.com/aclark4life
.. _working on this: http://pypi.python.org/pypi/collective.transmogrifier
.. _because I can: http://www.stevemcmahon.com/steves-blog/tools
