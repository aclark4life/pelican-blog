I love checkoutmanager and dotfiles
===================================
:date: 2013-02-08 12:00
:tags: Django, Mozilla, Plone, Python

*An ode to my OS X development workstation setup* [1]_

I am big on setting up my development environment, and enjoying the environment I work in. And I'm very thankful to the folks who make my life easier, including the authors of:

- `Python <http://www.ohloh.net/p/python/contributors/summary>`_: Python Core Developers
- `dotfiles <http://pypi.python.org/pypi/dotfiles>`_: Jon Bernard
- `checkoutmanager <http://pypi.python.org/pypi/checkoutmanager>`_: Reinout Van Rees

I also love **repetition**. So picture if you will, a new **Macbook Air or Pro** ready to serve as my development workstation. I like to perform, and study, the steps required to turn a new laptop in to my development workstation. So here we go. In this article, I will walk through the steps required to turn a new machine in to my developer workstation. Do follow along!

Shell
-----

One of the first things I do on a new system is change my shell to **Zsh** in ``System Preferences -> Users & Groups -> Current User -> Right Click -> Advanced Options...``. Don't forget to ``Click the lock to make changes`` first.

.. image:: https://raw.github.com/ACLARKNET/aclarknet.github.com/master/images/zsh.png

Zsh
~~~

Why **Zsh**? One of my favorite features is **shared history between open sessions**. So I can run a command in one window, and then run the same command from another window by fetching it from the history (with CTRL-R).

XCode
-----

After I take possession of my new laptop (running **Mountain Lion**, the newest OS X at the time of this writing), I head to the App Store to download XCode. [2]_ Among many other things, XCode gives me the GNU C Compiler and allows me to type "gcc" in my ``Applications -> Utilities -> Terminal``.

.. image:: https://raw.github.com/ACLARKNET/aclarknet.github.com/master/images/gcc.png

Python
------

.. image:: https://raw.github.com/ACLARKNET/aclarknet.github.com/master/images/homebrew.png

Now I need a Python interpreter [3]_. For development I use the `Collective Python Buildout <https://github.com/collective/buildout.python>`_ but I also enjoy using `Homebrew's <http://mxcl.github.com/homebrew/>`_ Python 2.7. I use Homebrew for a variety of other things too (e.g. mobile-shell AKA mosh) so here we go::

    $ ruby -e "$(curl -fsSL https://raw.github.com/mxcl/homebrew/go)"

… follow instructions …

::

    $ brew install python


Git
---

I think OS X (or XCode) includes git, but just in case::

    $ brew install git

Dotfiles
--------

At this point, I can begin to get serious about turning this new machine in to my developer workstation. And that means: **installing my private ssh key** so I can check out code without typing a password, of course. Normally this would be tedious, but with git and dotfiles it's not so bad. This is what I do from my home directory::

    $ git clone https://super_secret_url/dotfiles.git Dotfiles

I use https which requires a password for the first time only. Then I edit ``Dotfiles/.git/config`` and change the repository URL to ``git@super_secret_url/dotfiles.git``. So every subsequent pull and push will require no password. And to "install" these dotfiles, I do [6]_::

    $ pip install dotfiles
    $ dotfiles -s --force

Note: the dotfiles command finds my dotfiles in the default directory "Dotfiles" and create symbolic links to them.

Distribute & Pip
~~~~~~~~~~~~~~~~

Homebrew's Python includes pip, but even if it didn't::

    $ curl -O http://python-distribute.org/distribute_setup.py
    $ /usr/local/bin/python distribute_setup.py
    $ {easy_install, pip install} dotfiles

In other words, you can always install Distribute [4]_. After which you can use ``easy_install`` or ``pip`` to install dotfiles. (You can read up on the differences. TL;DR: neither is "better" or "worse", it's just a question of which tradeoffs you are willing to make. I tend to use pip just because it's newer and I like its requirements.txt feature, but easy_install is still very well supported as part of the Distribute project.)

Checkoutmanager
---------------

Now I need some things to develop. Since I work on a bunch of different projects, I need a way to keep track of what should be checked out at any given time. So I do this [5]_::

    $ pip install checkoutmanager
    $ checkoutmanager co

This creates and populates my ``~/Developer`` directory with code. And it "just works" because I keep a ``.checkoutmanager.cfg`` in my Dotfiles repository. It currently looks like this::

    [aclark]
    basedir = /Users/aclark/Developer/aclark
    checkouts =
        git@github.com:aclark4life/aclark4life.github.com.git resume
        git@github.com:aclark4life/desktops.git
        git@github.com:aclark4life/hireme.git
        git@github.com:aclark4life/projects.git
        git@github.com:aclark4life/reinstall.git
        git@github.com:ACLARKNET/tweets.git
        git@github.com:aclark4life/usesthis.git
    vcs = git

    [alt]
    basedir = /Users/aclark/Developer/alt
    checkouts =
        git@github.com:alt-aclark-net/alt-aclark-net.github.com.git
        git@github.com:alt-aclark-net/dexter.git
        git@github.com:alt-aclark-net/headstraight.git
    vcs = git

    [buildout]
    basedir = /Users/aclark/Developer/buildout
    checkouts =
        git@github.com:collective/buildout.bootstrap.git
        git@github.com:buildout/buildout.git
        git@github.com:buildout/buildout.github.com.git
    vcs = git

    [distribute]
    basedir = /Users/aclark/Developer
    checkouts = ssh://hg@bitbucket.org/tarek/distribute
    vcs = hg

    [clients]
    basedir = /Users/aclark/Developer
    checkouts =
    ; Bunch o client repos                
    vcs = git

    [clients-hg]
    basedir = /Users/aclark/Developer
    checkouts =
    ; Bunch o client repos                
    vcs = hg

    [dcpython]
    basedir = /Users/aclark/Developer/dcpython
    checkouts =
        git@github.com:DCPython/dcpython.github.com.git
        git@github.com:DCPython/pyramid-tutorials.git
    vcs = git

    [misc]
    basedir = /Users/aclark/Developer
    checkouts =
        git@github.com:ACLARKNET/aclarknet.github.com.git blog
        git@github.com:ACLARKNET/new_style.git
        git@github.com:aclark4life/binfiles.git
    ;    git@github.com:aclark4life/pyramid_python_3.git
        git@github.com:aclark4life/vanity.git
        git@github.com:aclark4life/zope2-heroku.git
        git@github.com:aclark4life/zope2_bootstrap.git
        git@github.com:codekoala/django-axes.git
        git@github.com:collective/buildout.python
    vcs = git

    [pillow]
    basedir = /Users/aclark/Developer/pillow
    checkouts =
        git@github.com:python-imaging/Pillow.git
        git@github.com:python-imaging/python-imaging.github.com.git
    vcs = git

    [plethorasociety]
    basedir = /Users/aclark/Developer/plethorasociety
    checkouts = 
        git@github.com:plethorasociety/plethorasociety.github.com.git
    vcs = git

    [plone]
    basedir = /Users/aclark/Developer/plone
    checkouts = 
        git@github.com:aclark4life/Plone-Debug-Assistant.git
        git@github.com:aclark4life/collective.recipe.bluebream.git
        git@github.com:aclark4life/event_days_indexer.git
        git@github.com:aclark4life/hello_plone.git
        git@github.com:aclark4life/mr_migrator_demo.git
        git@github.com:aclark4life/parse2plone.git
        git@github.com:aclark4life/plone_1_fun.git
        git@github.com:aclark4life/plone_addon_upgrade.git
        git@github.com:aclark4life/plone_guide.git
        git@github.com:aclark4life/plone_workflow_events.git
        git@github.com:aclark4life/schemaextender-facetednav-demo.git
        git@github.com:aclark4life/silly_content_import.git
        git@github.com:aclark4life/transmogrify.extract.git
        git@github.com:aclark4life/transmogrify.regexp.git
        git@github.com:aclark4life/viewlets_dont_suck.git
        git@github.com:aclark4life/wordpress2plone.git
        git@github.com:collective/Products.AttachmentField.git
        git@github.com:collective/Products.CalendarX.git
        git@github.com:collective/Products.EventRegistration.git
        git@github.com:collective/Products.PloneSoftwareCenter.git
        git@github.com:collective/Products.ifQuotes.git
        git@github.com:collective/Products.naked_plone.git
        git@github.com:collective/buildout.plonetest.git
        git@github.com:collective/collective.contacts.git
        git@github.com:collective/collective.controlpanel.edit_css.git
        git@github.com:collective/collective.developermanual.git
        git@github.com:collective/collective.formtoy.git
        git@github.com:collective/collective.github.com.git
        git@github.com:collective/collective.googleanalytics.git
        git@github.com:collective/collective.package.git
        git@github.com:collective/collective.project.git
        git@github.com:collective/collective.recaptcha.git
        git@github.com:collective/collective.recipe.grp.git
        git@github.com:collective/collective.recipe.rsync.git
        git@github.com:collective/collective.rip.git
        git@github.com:collective/collective.stats.git
        git@github.com:collective/funnelweb.git
        git@github.com:collective/github-collective.git
        git@github.com:collective/mr.migrator.git
        git@github.com:collective/plonecom-buildout.git
        git@github.com:collective/plonecom.theme.git
        git@github.com:collective/plonetheme.coolblue.git
        git@github.com:collective/plonetheme.freshpick.git
        git@github.com:collective/plonetheme.grungeera.git
        git@github.com:collective/plonetheme.keepitsimple.git
        git@github.com:collective/plonetheme.unilluminated.git
        git@github.com:collective/transmogrify.filesystem.git
        git@github.com:plone/Installers-OS-X.git
        git@github.com:plone/Products.PloneOrg.git
        git@github.com:plone/admin-docs.git
        git@github.com:plone/buildout.coredev.git
        git@github.com:plone/planet.plone.org.git
        git@github.com:plone/plone.api.git
        git@github.com:plone/plone.github.com.git
        git@github.com:plone/ploneorg.admin.git
        git@github.com:plone/plonetheme.ploneorg.git
    vcs = git

    [pythonpackages]
    basedir = /Users/aclark/Developer/pythonpackages
    checkouts = 
        git@github.com:aclark4life/buildout-apache-mysql.git
        git@github.com:aclark4life/buildout-munin.git
        git@github.com:aclark4life/buildout-mysql.git
        git@github.com:aclark4life/buildout-nginx.git
        git@github.com:aclark4life/buildout-plone-haproxy.git
        git@github.com:aclark4life/buildout-plone-varnish.git
        git@github.com:aclark4life/buildout-zenoss.git
        git@bitbucket.org:pythonpackages/pythonpackages.com.git vanity_app
        git@github.com:pythonpackages/buildout-apache-modwsgi.git
        git@github.com:pythonpackages/buildout-bluebream.git
        git@github.com:pythonpackages/buildout-django.git
        git@github.com:pythonpackages/buildout-jenkins.git
        git@github.com:pythonpackages/buildout-plone-getpaid.git
        git@github.com:pythonpackages/buildout-plone.git
        git@github.com:pythonpackages/buildout-wordpress.git
        git@github.com:pythonpackages/buildout-zope2.git
        git@github.com:pythonpackages/experimental.pythonpackages.git
        git@github.com:pythonpackages/github-services.git pythonpackages-github-services
        git@github.com:pythonpackages/pyramidpypi.git pythonpackages-index
        git@github.com:pythonpackages/pythonpackages-blog.git
        git@github.com:pythonpackages/pythonpackages-docs.git
        git@github.com:pythonpackages/pythonpackages-graphs.git
        git@github.com:pythonpackages/pythonpackages-paste.git
        git@github.com:pythonpackages/pythonpackages-scaffolds.git
        git@github.com:pythonpackages/pythonpackages.sendpickedversions.git
        git@github.com:pythonpackages/pythonpackages-whiskers.git
        git@github.com:pythonpackages/pythonpackages.git
    vcs = git

    [toys]
    basedir = /Users/aclark/Developer/toys
    checkouts =
        git@github.com:aclark4life/basic_pyramid_zodb.git
        git@github.com:aclark4life/github_repos_cloner.git
        git@github.com:aclark4life/other.git
        git@github.com:aclark4life/python_study.git
        git@github.com:aclark4life/django-hello.git
    vcs = git

Now it's time to bootstrap the Collective Python Buildout, which gives me **all versions of Python, ever** [7]_. And off we go::

    $ cd Developer/buildout.python
    $ python bootstrap.py

Finally, there is some PATH configuration required to make all of this seemless. The Collective Python Buildout gets installed in /opt while brew's stuff is in /usr/local. My PATH config currently looks like this::

    export PATH=/usr/local/bin:/usr/local/sbin:/opt/local/bin:/Users/aclark/Developer/buildout.python/python-2.7/bin:$PATH
    export PATH=~/Developer/binfiles:/usr/local/share/npm/bin:$PATH

With the above configuration, I default to the Python 2.7 in the Collective Python Buildout. That means that is the "python" or "virtualenv" I get when I typoe those commands. I use the full path or expanded binary name when I need them e.g. /usr/local/bin/python or python3.3.

That's it! I hope you will check out dotfiles and checkoutmanager for all your development needs.

.. [1] Not really an ode: http://en.wikipedia.org/wiki/Ode
.. [2] I know about Kenneth Reitz's XCode Command line Tools only, but if I recall correctly there is some "gotcha" that has bitten me more than once if I use that instead of the full XCode. I wish I could remember what it was now, but it's not coming to me. If it works for you though, great!
.. [3] I know about the system Python, and for small things like checkoutmanager and dotfiles I don't mind using it. But there is merit in avoiding it because Apple treats it like "their" Python and makes decisions for you that you may prefer to make yourself. E.g. I believe they use a crippled version of the readline library.
.. [4] Distribute is a more actively maintained fork of the venerable setuptools library (which itself is built on top of the Python standard library's distutils). Are we having fun yet?
.. [5] I also alias checkoutmanager to cm :-)
.. [6] I force because I want to replace the newly created .ssh dir with the one I keep in my Dotfiles repository.
.. [7] Well, 2.4 through 3.3 at last count.
