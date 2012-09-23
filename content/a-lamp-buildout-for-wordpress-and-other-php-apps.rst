A LAMP buildout for Wordpress and other PHP apps
################################################
:date: 2009-04-21 00:23
:tags: Plone

A Buildout for PHP?
-------------------

Having been a Plone Consultant for many years now, I find it very
painful to deal with non-Python-based technologies and I often will go
to great lengths to avoid it. I recently had to deploy a new PHP
application on an older Linux server (RHEL3) and could not bring myself
to compile the packages, search for RPMs, or do any of the mundane,
boring tasks required; so I began to look for an alternative. Enter: the
`LAMP buildout`_. I created and used this to deploy my client's PHP
application. I hope others find it useful, both as an alternative way to
deploy PHP apps, and as an example of the wide variety of things
buildout can be used to do.

It's just that simple?
----------------------

Unfortunately, this was not the blissful experience I had hoped for.
There were some non-obvious configuration parameters that had to be
dealt with. This was tedious and sometimes painful, but achieving the
end result was a uniquely rewarding experience I can assure you! In
fact, most of the problems had to do with the individual software
components and not buildout itself, which was a pleasure to work with
and one of the main reasons I am writing this blog entry. In a Plone
buildout for example, in most cases, the tedious parts are handled for
you and you just need to `add the Plone egg, run buildout, and start
your site`_.

Break it down
-------------

Now, on to the buildout! It was developed and tested on Mac OS X 10.5
then deployed to RHEL3. I had a small problem on RHEL3 with the GD
imaging library so I removed it (and installed it by hand in
/usr/local). Other than that, things went smoothly and I deployed
several PHP apps with it just for kicks, including:

-  Phorum
-  SugarCRM
-  WordPress
-  phpMyAdmin

It builds Apache, PHP, MySQL, GD, and Supervisor. Let's take a look.

First, we define the parts. For each of these, we'll do something useful
to contribute to the end result.

::

    [buildout]
    parts =
    # Aspeli-style line-spacing to emphasize the functionality of each part or group of parts ;-)
        env
        grp    mysql
        apache
        gd
        php    ports
        mycnf
        mysql-bin
        mysql-admin
        mysql_install_db
        apache-conf
        php-conf# Uncomment only one of these at a time
    #    phpmyadmin
    #    sugarcrm
    #    phorum
        wordpress    supervisor

Now that the parts are listed, the rest of the buildout must define
those parts.

First, we add some utilities required by this buildout.

::

    [env]
    recipe = gocept.recipe.env[grp]
    recipe = collective.recipe.grp

Next, we build the core components.

::

    [mysql]
    recipe = hexagonit.recipe.cmmi
    url = http://mysql.mirrors.hoobly.com/Downloads/MySQL-5.1/mysql-5.1.33.tar.gz
    keep-compile-dir = true[apache]
    recipe = hexagonit.recipe.cmmi
    url = http://www.trieuvan.com/apache/httpd/httpd-2.2.11.tar.gz
    configure-options = --enable-so
    keep-compile-dir = true[gd]
    recipe = hexagonit.recipe.cmmi
    url = http://www.libgd.org/releases/gd-2.0.35.tar.gz
    keep-compile-dir = true[php]
    recipe = zc.recipe.cmmi
    environment =
        PATH=${mysql:location}/bin:${env:PATH}
    url = http://us2.php.net/get/php-5.2.9.tar.gz/from/this/mirror
    # Beware, the new line below (i.e. '') may need to be undone.
    extra_options =
      --prefix=${buildout:directory}/parts/apache/php 
      --with-config-file-path=${buildout:directory}/etc/php.ini 
      --with-gd=${buildout:directory}/parts/gd 
      --with-apxs2=${buildout:directory}/parts/apache/bin/apxs 
      --with-mysql=${mysql:location} 
      --enable-mbstring

After that, some configuration. Read the comments below for more
information.

::

    # Make it easy to change the various port settings[ports]
    recipe = plone.recipe.command
    command =
        echo These ports are used to configure this LAMP:
        echo Supervisor: ${ports:supervisor}
        echo Apache: ${ports:apache}
        echo MySQL: ${ports:mysql}
    supervisor = 9001
    apache = 8080
    mysql = 3306# All the mysql compile options[mycnf]
    recipe = plone.recipe.command
    command =
        echo
        echo These options are passed to mysqld_safe: ${mycnf:opt}
        echo
    basedir=${mysql:location}
    datadir=${buildout:directory}/var
    pid=${mycnf:datadir}/mysql.pid
    err = ${mycnf:datadir}/log/mysql.err
    sock = ${mycnf:datadir}/mysql.sock
    # Beware, the new line below (i.e. '') may need to be undone.
    opt = --port=${ports:mysql} --pid-file=${mycnf:pid} --log-error=${mycnf:err} 
    --basedir=${mycnf:basedir} --datadir=${mycnf:datadir} --socket=${mycnf:sock}# Setup the mysql databases.[mysql_install_db]
    recipe = plone.recipe.command
    command =
        ${mysql:location}/bin/mysql_install_db --datadir=${mycnf:datadir}
        echo
        echo After starting supervisord, you may want to run:
        echo ${buildout:directory}/parts/mysql/bin/mysqladmin -u root password 'new-password'
        echo
    update-command = ${mysql_install_db:command}# Generate Config files for Apache and PHP[apache-conf]
    recipe = collective.recipe.template
    input = ${buildout:directory}/templates/httpd.conf.in
    output = ${buildout:directory}/etc/httpd.conf[php-conf]
    recipe = collective.recipe.template
    input = ${buildout:directory}/templates/php.ini.in
    output = ${buildout:directory}/etc/php.ini# Make it easy to run mysql and mysqladmin[mysql-bin]
    recipe = collective.recipe.template
    input = ${buildout:directory}/templates/mysql.in
    output = ${buildout:directory}/bin/mysql[mysql-admin]
    recipe = collective.recipe.template
    input = ${buildout:directory}/templates/mysqladmin.in
    output = ${buildout:directory}/bin/mysqladmin

Now, the parts that download the various PHP apps.

::

    [wordpress]
    recipe = hexagonit.recipe.download
    url = http://wordpress.org/latest.tar.gz
    destination = ${buildout:directory}/htdocs
    strip-top-level-dir = true[phpmyadmin]
    recipe = hexagonit.recipe.download
    url = http://prdownloads.sourceforge.net/phpmyadmin/phpMyAdmin-3.1.3.2-english.tar.bz2
    destination = ${buildout:directory}/htdocs
    strip-top-level-dir = true[sugarcrm]
    recipe = hexagonit.recipe.download
    url = http://www.sugarforge.org/frs/download.php/5252/SugarCE-5.2.0c.zip
    destination = ${buildout:directory}/htdocs
    strip-top-level-dir = true[phorum]
    recipe = hexagonit.recipe.download
    url = http://www.phorum.org/downloads/phorum-5.2.10.tar.gz
    destination = ${buildout:directory}/htdocs
    strip-top-level-dir = true

And the supervisor that will control everything.

::

    [supervisor]
    recipe = collective.recipe.supervisor
    port = ${ports:supervisor}
    serverurl = http://127.0.0.1:${ports:supervisor}
    pp = ${buildout:directory}/eggs/supervisor-3.0a6-py2.4.egg/supervisor/pidproxy.py
    # Beware, the new line below (i.e. '') may need to be undone.
    programs =
        10 mysql ${supervisor:pp} [ ${mycnf:pid} ${mysql:location}/bin/mysqld_safe ${mycnf:opt} ]
        20 apache ${apache:location}/bin/httpd [ -c "ErrorLog /dev/stdout" -DFOREGROUND 
                                                 -f ${buildout:directory}/etc/httpd.conf ]

If you are interested in trying this yourself, please see:

`http://svn.aclark.net/svn/public/buildout/lamp/trunk/`_

and let me know how it goes!

.. _LAMP buildout: http://svn.aclark.net/svn/public/buildout/lamp/trunk/
.. _add the Plone egg, run buildout, and start your site: getting-excited-about-plone-3-2
.. _`http://svn.aclark.net/svn/public/buildout/lamp/trunk/`: http://svn.aclark.net/svn/public/buildout/lamp/trunk/
