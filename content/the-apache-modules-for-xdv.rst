The Apache modules for XDV
##########################
:date: 2010-07-12 08:25
:tags: Plone

I was recently tasked with consolidating our various **business services** (website, software repository, mailing lists, ldap, etc.) on to a single virtual machine (ostensibly to save money, although it didn't quite work out that way). The Apache modules for XDV presented themselves as an attractive technique to use, in helping me achieve my goals.

Background
----------

Previously, I had been blissfully running http://aclark.net with NGINX, Plone 4 trunk, and XDV on a small virtual machine and absolutely loving it.

Additionally, I had separate virtual machines for my Wordpress blog (blog.aclark.net) and Subversion software repository (svn.aclark.net).  The isolation of these services made them easy to manage and still relatively cheap to run them all.

And in fact, I have come to rely heavily on the ability to (1.) rapidly create a virtual machine, (2.) install a bunch of vendor packages that Just Work™, and (3.) build out whatever was left i.e. whatever could not be easily installed via OS vendor packages. This usually translates loosely into "I use Buildout for my Plone sites, and an OS vendor package installer for everything else".

That said, even though I already knew the hazards of trying to cram too many services on to a single "shared" host, and didn't really want to do that dance again, it seemed reasonable at the time to at least try and consolidate them on to a single virtual machine (it sounds crazy in hindsight).

First choice: NGINX
~~~~~~~~~~~~~~~~~~~

Like I said earlier, the forked version of NGINX available on the `HTML-XSLT website`_ is an absolute pleasure to use. But when I pondered consolidating services I knew it would not be easy, and maybe even impossible to run Wordpress behind NGINX.

Second choice: Apache
~~~~~~~~~~~~~~~~~~~~~

So I thought to myself, "I know, I'll just switch to the Apache modules for XDV" and that will solve my PHP/Plone "integration" problems for the time being. (Another way to solve them would be to use the `XDV middleware`_ along with `Zope 2.13`_'s WSGI support; I will be trying that next.)

But not so fast.

Problems
--------

Of course, things don't always go as planned.

First problem
~~~~~~~~~~~~~

The Apache modules for XDV do not work exactly "as advertised" on any of the "modern" OS platforms I tried (Debian, various Ubuntus, and Arch Linux). They compile fine against the operating system's Apache, but do not run properly. See `this thread`_ on the Deliverance mailing list (and I challenge anyone reading this to correct me! :-D)

"Fine," I thought, I'll just create a buildout to deploy everything. I `wrote a book`_ about deploying Plone websites with Buildout. This should be easy, right?

Wrong.

Second problem
~~~~~~~~~~~~~~

It's hard to create such a buildout for a variety of reasons, but most noticeably in my mind is the "library soup" you may encounter on any modern system. For example, I started off by trying to include all the dependencies in the buildout. But I ended up leaving things out, like libxml2 and libxslt relying instead on the operating system vendor packages. Because even though I tried desperately to tell every other dependency about the included libxml2 and libxslt2, I still ended up with an annoying "missing symbols" error at the end (meaning I likely missed a compiler flag along the way).

These errors can be very frustrating, and even worse: **sporadic**.  Sometimes you may inadvertently add or remove a system dependency during the build process. So you could be relying on a system package and not even know it until later when it is too late (i.e. when you are enjoying some unplanned and unexpected down time).

So there I went again. It took several days I didn't really have, and the results were not what I expected, but I'm still somewhat happy with them. Now, I want to share this buildout particularly with folks considering using the Apache modules for XDV (`http://code.google.com/p/html-xslt/`_). Because while it would be much easier if the Apache modules Just Worked™ with OS vendor packages, in the event that they don't (which is what I experienced) folks may find this buildout helpful. (That, and Jon Stahl requested it on Facebook :-D).

Conclusion
----------

Anyway, I'm quite happy with the buildout and I am sharing it in hopes that it will move the Apache/XDV story forward.

In addition to compiling Apache with mod\_depends and mod\_transform, it includes Subversion, Trac, mod\_wsgi, PHP and Wordpress. As I mentioned earlier, it is not really my preference to cram all this stuff in to one buildout, but as long as it is reliable and consistent, I don't mind it too much. It also handles the theme compilation for a variety of services, which is accomplished via a command recipe that executes calls to *bin/xdvcompiler*.

Incidentally, I have no particular allegiance to, or dislike of Apache: more like a love/hate relationship; it can be very useful in a variety of situations, while at the same time confounding. But regardless, I would like to see the Apache XDV modules be able to deliver the same rock solid performance as the NGINX fork.

Kudos to Laurence Rowe (et al.) for the Apache modules! I hope this blog entry will facilitate a push to get people using them with their *operating system vendor's Apache packages*, which may inspire Laurence to continue developing them, and most importantly to fix bugs ;-).

Normally, I like to factor out the reusable bits first, but this buildout is presented in it's entirety as I am using it (minus some customer bits), for whatever that is worth. Here is a look at the "main" buildout.cfg file, most of which should be self-explanatory. Click around this site to see the results:

::

    [buildout]
    #extends = http://svn.aclark.net/svn/public/buildout/apache/trunk/buildout.cfg
    extends = apache.cfg
    parts =
     bootstrap
     xdv
     apache
     apreq2
     apache-config
     apache-config-aclark
     apache-config-admin
     apache-config-svn
     apache-config-trac
     apache-config-ssl
     apache-config-mailman
     php
     php-conf
     mod-depends
     mod-transform
     python
     distribute
     trac
     theme-aclark
     theme-public
     theme-support
     theme-blog
     mod-wsgi
     subversion
     subversion-python
     supervisor[apache]
    configure-options +=
     --with-included-apr
     --with-ldap
     --enable-authnz-ldap
     --enable-ldap
     --enable-ssl
     --enable-dav
     --enable-dav-fs
     --enable-dav-lock[mod-depends]
    recipe = hexagonit.recipe.cmmi
    url = http://html-xslt.googlecode.com/files/mod-depends-html-xslt.tgz
    configure-options = --with-apxs=${apache:location}/bin/apxs[mod-transform]
    recipe = hexagonit.recipe.cmmi
    url = http://html-xslt.googlecode.com/files/mod-transform-html-xslt.tgz
    configure-options =
     --with-apxs=${apache:location}/bin/apxs
     --with-apr=${apache:location}/bin/apr-1-config
     --with-apr-util=${apache:location}/bin/apu-1-config
    environment-section = environment[environment]
    PATH = %(PATH)s:${apreq2:location}/bin
    LIBS = -lxml2 -lxslt[apreq2]
    recipe = hexagonit.recipe.cmmi
    url = http://www.bizdirusa.com/mirrors/apache/httpd/libapreq/libapreq2-2.12.tar.gz
    configure-options = --with-apache2-apxs=${apache:location}/bin/apxs[libxml2]
    recipe = hexagonit.recipe.cmmi
    url = ftp://xmlsoft.org/libxml2/libxml2-2.7.7.tar.gz
    configure-options =
     --with-python=no[libxslt]
    recipe = hexagonit.recipe.cmmi
    url = ftp://xmlsoft.org/libxml2/libxslt-1.1.26.tar.gz
    configure-options =
     --with-python=no[php]
    recipe = hexagonit.recipe.cmmi
    url = http://us2.php.net/get/php-5.3.2.tar.gz/from/this/mirror
    configure-options = --prefix=${buildout:directory}/parts/apache/php
    --with-apxs2=${buildout:directory}/parts/apache/bin/apxs
    --with-config-file-path=${buildout:directory}/etc/php.ini
    --enable-mbstring --with-mysql=/usr/bin[php-conf]
    recipe = collective.recipe.template
    input = ${buildout:directory}/templates/php.ini.in
    output = ${buildout:directory}/etc/php.ini[apache-config-aclark]
    recipe = collective.recipe.template
    input = ${buildout:directory}/templates/aclark.in
    output = ${buildout:directory}/etc/aclark[apache-config-admin]
    recipe = collective.recipe.template
    input = ${buildout:directory}/templates/admin.in
    output = ${buildout:directory}/etc/admin[apache-config-svn]
    recipe = collective.recipe.template
    input = ${buildout:directory}/templates/svn.in
    output = ${buildout:directory}/etc/svn[apache-config-trac]
    recipe = collective.recipe.template
    input = ${buildout:directory}/templates/trac.in
    output = ${buildout:directory}/etc/trac[apache-config-ssl]
    recipe = collective.recipe.template
    input = ${buildout:directory}/templates/ssl.in
    output = ${buildout:directory}/etc/ssl[apache-config-mailman]
    recipe = collective.recipe.template
    input = ${buildout:directory}/templates/mailman.in
    output = ${buildout:directory}/etc/mailman[ports]
    production = 80[subversion]
    recipe = hexagonit.recipe.cmmi
    url = http://subversion.tigris.org/downloads/subversion-1.6.12.tar.gz
    configure-options = --with-apxs=${apache:location}/bin/apxs
    make-targets =
     install
     swig-py
     install-swig-py[mod-wsgi]
    recipe = hexagonit.recipe.cmmi
    url = http://modwsgi.googlecode.com/files/mod_wsgi-3.2.tar.gz
    configure-options =
     --with-apxs=${apache:location}/bin/apxs
     --with-python=${buildout:directory}/parts/python/bin/python[subversion-python]
    recipe = plone.recipe.command
    libdir = ${python:location}/lib/python2.6/site-packages
    command =
     rm -rf ${subversion-python:libdir}/svn
     rm -rf ${subversion-python:libdir}/libsvn
     cp -prv ${subversion:location}/lib/svn-python/libsvn ${subversion-python:libdir}
     cp -prv ${subversion:location}/lib/svn-python/svn ${subversion-python:libdir}
    update-command = ${subversion-python:command}[python]
    recipe = hexagonit.recipe.cmmi
    url = http://www.python.org/ftp/python/2.6.5/Python-2.6.5.tgz
    configure-options = --enable-shared[python-exe]
    executable = ${buildout:directory}/parts/python/bin/python[distribute]
    recipe = plone.recipe.command
    command =
     wget http://python-distribute.org/distribute_setup.py
     ${python-exe:executable} distribute_setup.py[xdv]
    recipe = zc.recipe.egg[trac]
    recipe = plone.recipe.command
    command =
     ${buildout:directory}/parts/python/bin/easy_install Trac
     ${buildout:directory}/parts/python/bin/easy_install TracSubversionLocation[theme-public]
    recipe = plone.recipe.command
    command =
     ${buildout:bin-directory}/xdvcompiler 
     /srv/trac/public/theme/rules.xml 
     /srv/trac/public/theme/index.html 
     --output=${buildout:directory}/etc/trac-public.xsl
    update-command = ${:command}[theme-support]
    recipe = plone.recipe.command
    command =
     ${buildout:bin-directory}/xdvcompiler 
     /srv/trac/support/theme/rules.xml 
     /srv/trac/support/theme/index.html 
     --output=${buildout:directory}/etc/trac-support.xsl
    update-command = ${:command}[theme-aclark]
    recipe = plone.recipe.command
    command =
     ${buildout:bin-directory}/xdvcompiler 
     /srv/aclark/theme/rules.xml 
     /srv/aclark/theme/index.html 
     --output=${buildout:directory}/etc/theme-aclark.xsl
    update-command = ${:command}[theme-blog]
    recipe = plone.recipe.command
    command =
     ${buildout:bin-directory}/xdvcompiler 
     /srv/blog/theme/rules.xml 
     /srv/blog/theme/index.html 
     --output=${buildout:directory}/etc/theme-blog.xsl
    update-command = ${:command}

You can check out the rest of the buildout `here`_ (themed with XDV :-)). And if you enjoy this post, please feel free to pick up a copy of `Plone 3.3 Site Administration`_ from PACKT Publishing, due out any day now (I am expecting to review pre-finals this week some time).

.. _HTML-XSLT website: http://code.google.com/p/html-xslt/
.. _XDV middleware: http://pypi.python.org/pypi/dv.xdvserver
.. _Zope 2.13: http://pypi.python.org/pypi/Zope2/2.13.0a1
.. _this thread: http://www.coactivate.org/projects/deliverance/lists/deliverance-discussion/archive/2010/06/1276982495896/forum_view
.. _wrote a book: http://blog.aclark.net/2010/03/30/blood-sweat-tears-and-a-new-plone-book/
.. _`http://code.google.com/p/html-xslt/`: http://code.google.com/p/html-xslt/
.. _here: http://svn.aclark.net/trac/public/browser/buildout/aclark/apache-xdv/trunk
.. _Plone 3.3 Site Administration: http://aclark.net
