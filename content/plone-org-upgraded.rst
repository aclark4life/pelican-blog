Plone.org upgraded
==================

:date: 2013-06-22
:tags: Plone, Python

Recently at the behest of Liz Leddy, I `upgraded plone.org from Plone 4.2 to Plone 4.3 <https://github.com/plone/Products.PloneOrg/commit/b04105f7c9cacf3880c12effba5ffe261d4b5163>`_. It's been a while since I had the pleasure, so I thought I'd make some notes: for myself, the AI Team and anyone else interested in the process.

Background
----------

1. Plone.org is one of the **oldest Plone sites in existence**, having been launched circa Plone 1 and upgraded in place ever since.
#. It functions remarkably well, given #1.
#. It's not without its issues, but all of them are manageable — for some value of manageable.
#. It's often very time consuming to work on.

Pre-Process
-----------

1. The first step is always to get a local copy::

    $ git clone git@github.com:plone/Products.PloneOrg.git
    $ cd Products.PloneOrg
    $ cp buildout.cfg.in buildout.cfg

#. Edit ``buildout.cfg`` to extend the ``database.cfg``::

    [buildout]
    # Rename to buildout.cfg and uncomment one of the profiles below
    extends =

    # Plone only, unthemed
    #    conf/develop.cfg

    # Copy data local (with plone.org account)
        conf/database.cfg

    # Production (for use on plone.org server)
    #    conf/production.cfg

    # Staging (for use on plone.org server)
    # and Deployment (for use by Jenkins, admins and developers), 
    #   fabric can be added to any of primary configurations 

    #    conf/staging.cfg
    #    conf/fabric.cfg

    # Developer Database Drop; makes developer-friendly copies
    # of plone.org's content.
    #    conf/devdrop.cfg


#. Bootstrap and run Buildout::

    $ virtualenv-2.7 .
    $ bin/pip install zc.buildout
    $ bin/buildout

#. Make the appropriate configuration changes i.e. change ``extends`` from 4.2 to 4.3::

    [buildout]
    develop = .
    extends = 
        http://dist.plone.org/release/4.3.1/versions.cfg
        versions.cfg
        sources.cfg
    extensions = 
    #    buildout.dumppickedversions
        buildout.threatlevel
        mr.developer

    versions = versions
    sources-dir = sources
    eggs =
        Pillow
        Products.PloneOrg
        Products.PloneHotfix20130618

    # get us a user and group variable
    [env]
    recipe = gocept.recipe.env
    [grp]
    recipe = collective.recipe.grp

#. Run the upgrade locally. With plone.org data this takes about 45 minutes to an hour [1]_.

.. image:: https://raw.github.com/ACLARKNET/blog/gh-pages/images/upgrade.png
    :alt: alternate text

#. If the upgrade succeeds, you are ready to launch. If it fails, fix the errors before proceeding.

Process
-------

We know from upgrading locally that the process will take about 45 minutes to an hour, so you should **allocate about 2 hours to do the upgrade**.

#. Announce the upgrade: preferably a week or two in advance. The plone-developers and plone-users lists are probably sufficient, but you can create a plone.org news item too if you are feeling extra-ambitious. I only had a small window to perform this maintenance, so I skipped this step and proceeded directly to the next one.

#. Add a status message to plone.org to indicate a maintenance window is in progress. I chose to customize the ``main_template`` to accomplish this, but ideally we'd have some functionality in Plone that allowed site administrators to easily configure status messages.

.. image:: https://raw.github.com/ACLARKNET/blog/gh-pages/images/upgrade-message.png
    :alt: alternate text

#. Disable logins. Since the upgrade takes a long time, we don't want content being edited during this process. I chose to use David Glick's technique of disabling PAS. I moved the ldap authentication plugin to the Active Plugin list, thus disabling PAS such that only ZODB users could login. But ideally we'd have some feature in Plone to allow site administrators to disable logins.

.. image:: https://raw.github.com/ACLARKNET/blog/gh-pages/images/pas.png
    :alt: alternate text

#. Run the upgrade. I forgot to mention earlier something very important: **On plone.org, you can't access Zope from the internet.** And you can't run the upgrade without accessing Zope. Hence run the following command to access the server, then access Plone via ``http://localhost:8080``::

    $ ssh -L 8080:10.57.0.107:5011 direct.plone.org

#. After the upgrade finishes, click around to make sure you didn't break anything. In my case, I broke something — I normally move ``portal_skins/custom`` out of the way before upgrading, but this time I forgot. And when I experienced minor JavaScript issues, I forgot to examine custom; which currently looks like this:

.. image:: https://raw.github.com/ACLARKNET/blog/gh-pages/images/custom.png
    :alt: alternate text

Even if I had remembered, I didn't want to spend the next few hours examining database customizations. Fortunately, before I realized I had forgotten to check custom, I emailed the plone-developers list — and Nathan Van Gheem to the rescue! He fixed some JavaScript in custom, then I cleared the cache(s). Ideally Plone would report on database customizations during the upgrade process: to indicate the potential for breakage and encourage the site administrator to round-trip those customizations back to the file system.

Conclusion
----------

That's it! I hope this helps folks wrap their head around the plone.org upgrade process. A few closing thoughts:

- With Cloudflare in front, we probably don't need Varnish anymore.
- Leaving a note in ``portal_skins/custom`` to encourage folks to "please keep this area clean" — does not work.
- plone.com anyone? I don't know the future of plone.org and I have mixed feelings about it: on the one hand, I'm proud to help maintain such an old and venerable system. On the other hand, I think plone.org should be retired in a way similar to old.zope.org. What do you think?

.. [1] It shouldn't take this long. See: https://github.com/plone/Products.PloneOrg/commit/b04105f7c9cacf3880c12effba5ffe261d4b5163#commitcomment-3384259 for a discussion about this issue.
