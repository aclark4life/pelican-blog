A report on plonetheme.*
========================

:date: 2010-11-04 11:09
:tags: Plone

By now, most of us are familiar with XDV and how awesome it is for theming Plone (or any website). You should also be aware that XDV has been renamed to **Diazo**, and collective.xdv is now called **plone.app.theming**.

But let us not forget the humble "old style" theme just yet! Sometimes they come in very handy, and may even be preferable in some cases depending on what you are trying to accomplish.

I just gave **plonetheme**.\* a quick spin and thought I'd share the process and results with anyone that might find it useful.

Step 1
------

Get a list of all the **plonetheme** packages on PyPI:

::

    $ pip search plonetheme

Step 2
------

Create a buildout:

::

    $ virtualenv plone-theme-test
    $ bin/easy_install zc.buildout
    $ bin/buildout init

Step 3
------

Edit your buildout.cfg to include the following:

::

    [buildout]
    extends = http://dist.aclark.net/buildout/plone/4.0.x/buildout.cfg
    parts =
     plone[plone]
    eggs +=
     ${theme:eggs}zcml +=
     ${theme:eggs}[theme]
    eggs =# Deps that the themes should have added
     collective.contentleadimage
     collective.flowplayer
     z3c.jbot#    Products.categorynavigator
    #
    # XXX Products.categorynavigator is a dep of plonetheme.mvob but it
    # has a NameError
    # ZopeXMLConfigurationError: File "/Users/aclark/Developer/packages…
    # NameError: name 'ImportException' is not defined# themes
     plonetheme.notredame
     plonetheme.fui
     plonetheme.sunburst
     plonetheme.colorcontext
     plonetheme.twinapex
    #    plonetheme.mvob
     plonetheme.peerstheme
     plonetheme.nautica05
     plonetheme.stylized
     plonetheme.labs
     plonetheme.sait2009
     plonetheme.cultureCab
     plonetheme.xtheme
     plonetheme.mimbo
     plonetheme.python
     plonetheme.terrafirma
     plonetheme.solemnity
     plonetheme.level2
     plonetheme.tidyblog
     plonetheme.andreas01
     plonetheme.blueblog
     plonetheme.delicious2
    #    plonetheme.hamnavoe
     plonetheme.greencommunity
     plonetheme.subordinate
     plonetheme.bluegray
     plonetheme.p2
     plonetheme.aclark_twitter
     plonetheme.relic
     plonetheme.classic
    #    plonetheme.simplicity
     plonetheme.netsightintranet
     plonetheme.keepitsimple
     plonetheme.andreas02
     plonetheme.essay
     plonetheme.ReOrg
    #    plonetheme.Bangalore
     plonetheme.nonzero
     plonetheme.cleantheme
     plonetheme.minimalist
     plonetheme.inbusiness
    #    plonetheme.corporatemale
     plonetheme.portaltwodotoh
     plonetheme.rcom
     plonetheme.equipoteih
     plonetheme.pyar
     plonetheme.basic# XXX plonetheme.GreenEarthTheme3_0 has zope.configuration.config…
    # error
    #    plonetheme.GreenEarthTheme3_0
    #zope.configuration.config.ConfigurationExecutionError: <type …
    #  in:
    #  File "/Users/aclark/Developer/packages/plonetheme.GreenEarthTheme…
    #     <cmf:registerDirectory
    #         name="GreenEarthTheme3_0_templates"/> plonetheme.criticas
     plonetheme.gemstone
    #    plonetheme.bronzecube
     plonetheme.lithium
     plonetheme.overlappedtabs

Step 4
------

Run buildout; start Plone; play around!

Conclusion
-----------

The whole effort (including writing the blog post) took only an hour or two, for whatever that is worth (not including the actual theme review, unfortunately!). I find the results interesting and I thought you might too.

Process
-------

Dependencies
~~~~~~~~~~~~

You'll notice in the **[theme]** section, comments about various packages that were not included with all of the various themes.

As far as I can tell, it is in the best interest of "old style" theme developers to specify these packages in their setup.py files with the install_requires parameter!

OK, it's actually in my best interest because then I have to do less work, but you get the idea.

Broken or missing packages
~~~~~~~~~~~~~~~~~~~~~~~~~~

The **plonetheme**.\* packages that are just commented out (without an XXX note) did not make it past the bin/buildout step (for whatever reason, usually a broken package).

Themes
------

My favorite theme (right after plonetheme.aclark\_twitter, that is) is… nevermind! I wanted to report on that but I still have to go through all the themes! (By installing each one at a time, testing, then uninstalling before moving to the next one.)

Packaging
---------

Just my opinion, but if you are adding functionality to Plone, it's probably not (just) a theme. So I would separate that functionality from your **plonetheme**.\* code.

Problems
--------

jbot modifies default Plone theme?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

I've noticed this before in both Plone Classic and now Sunburst when jbot is installed. No idea what the actual cause is:

Disclaimer
----------

Designed for Plone 4?
~~~~~~~~~~~~~~~~~~~~~

Before you say it (I know you are thinking it), I know not all of these themes are designed to work with Plone 4. I dont' have a good answer about how to approach that problem (I just know that when looking for themes, I don't really care. I just "want it to work".)

Bug report please?
~~~~~~~~~~~~~~~~~~

I know, I know. I should open a ticket for the jbot thing.

And now off to play!

P.S. I will report on the install process in the comments.

So far, *Andreas* installed, worked, and looked nice while *Bluegray Theme 1.0.0b2* required a ZMI undo ;-)
