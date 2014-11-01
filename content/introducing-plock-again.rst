Introducing Plock Again
=======================

:date: 2013-12-29 12:00
:tags: Plone, Python

A few months ago I introduced **Plock: the Plone-installer for the Pip-loving crowd**. Then I got sidetracked with the next version of Plock lingering unreleased in master. With the holidays underway I had a chance to revisit Plock and discovered a few things:

- I still like the idea of Plock.
- I got carried away adding miscellaneous features to Plock, which only served to ruin the elegance of the idea.
- I particularly like the idea of moving my `hosted configuration files <https://github.com/plock/pins>`_ from PythonPackages to Plock. They always felt out of place in PythonPackages but I didn't have a better place to put them until now.

What is Plock?
--------------

So what is Plock today?

- A Plone-installer for the Pip-loving crowd. That means someone with Python 2.7 and Pip should be able to install Plone in a matter of minutes with: ``pip install plock ; plock .``

- A set of hosted configuration files for Plone called **Plock Pins**. [1]_

- A command line utility with a sharp focus.

Features
~~~~~~~~

I've recently removed several extraneous features from Plock to sharpen the focus on installing Plone and its add-ons. Check out the Plock 0.1.9 ``--help``::

    $ plock -h
    usage: plock [-h] [-v] [-e] [-a ADD_ON] [-l] [-w] [-r] [install_dir]

    Plock is a Plone Installer for the Pip-Loving Crowd

    positional arguments:
      install_dir

    optional arguments:
      -h, --help            show this help message and exit
      -v, --version         show program's version number and exit
      -e, --expert          expert mode
      -a ADD_ON, --add-on ADD_ON
                            install add-ons from PyPI
      -l, --list-addons     list add-ons from PyPI
      -w, --write-config    write buildout.cfg
      -r, --raw             unformatted output, use with -l


Install Plone
+++++++++++++

The main focus is on installing Plone to a user-specified installation directory e.g.::

    $ plock .

Install Add-ons
+++++++++++++++

Additionally you may specify an add-on to install e.g.::

    $ plock -a Products.PloneFormGen .

Add-on installations are cumulative, so:: 

    $ plock -a Products.PloneFormGen .
    $ plock -a collective.loremipsum .

will result in a ``buildout.cfg`` file that looks like this::

    [buildout]
    extends = https://raw.github.com/plock/pins/master/plone-4-3

    [plone]
    eggs = 
        ${addon:packages}
        ${base:packages}
        Products.PloneFormGen
        collective.loremipsum

Add-ons that don't install via Buildout **will not break your installation** e.g.::

    $ plock -a asdf .
    Plock is installing Plone............. error: buildout failed.

When Buildout fails, Plock restores the previous working ``buildout.cfg`` for you.

List Add-ons
++++++++++++

Because Plone is more fun with add-ons and because add-ons can be hard to find, Plock will list (and alpha-sort) all the Plone add-ons available from PyPI:: 

    1) 73.unlockItems                           - A small tool for unlocking web_dav locked item in a plone portal.
    2) actionbar.panel                          - Provides a (old) facebook style action panel at the bottom of your  Plone site
    3) adi.init                                 - Deletes Plone's default contents        
    4) adi.samplecontent                        - Deletes Plone's default content and adds some sample content
    5) adi.slickstyle                           - A slick style for Plone portals, easily extendable for your own styles.
    6) anthill.querytool                        - GUI for AdvancedQuery with some extensions - searching the easy way for Plone
    7) anthill.skinner                          - Skinning for plone made easy            
    8) anz.dashboard                            - Plone netvibes like dashboard implementation
    9) anz.ijabbar                              - Integrate iJab(an open source XMPP web chat client recommended by xmpp.org) to your plone site.
    10) archetypes.clippingimage                 - Image field and/or patch with clipping support for Plone/Archetypes.
    …
    1,256) zkaffold                                 - Build out demonstration content for plone
    1,257) ZopeSkel                                 - Templates and code generator for quickstarting Python, Zope and Plone projects.
    1,258) zopeskel.diazotheme                      - Paster templates for Plone Diazo theme package
    1,259) zopeskel.niteoweb                        - Paster templates for standard NiteoWeb Plone projects
    1,260) zopyx.ecardsng                           - An ECard implementation for Plone       
    1,261) zopyx.ipsumplone                         - Lorem ipsum text and image demo content for Plone
    1,262) zopyx.multieventcalendar                 - A multi-event calendar for Plone 3.X    
    1,263) zopyx.plone.cassandra                    - Show all assigned local roles within a subtree for any Plone 4 site
    1,264) zopyx.plone.migration                    - Export/import scripts for migration Plone 2+3 to Plone 4
    1,265) zopyx.smartprintng.plone                 - Produce & Publisher server integration with Plone

Write config
++++++++++++

Lastly, because sometimes you want to write a configuration file without installing Plone there is::

    $ plock -w .
    Wrote buildout.cfg.

which will result in::

    $ cat buildout.cfg
    [buildout]
    extends = https://raw.github.com/plock/pins/master/plone-4-3

.. [1] Extending configuration files over the internet is not a universally accepted technique due to the inherent security risk, but it's how I've worked with Plone for years. I once added a "secure" feature to Plock but removed it recently due to the maintenance burden. Plock is now primarily insecure but true to its original goal of simplicity. Maybe security can be re-added later in some semi-elegant way (e.g. cert verification by the client?).
