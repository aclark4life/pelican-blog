Supervisor rocks!
#################
:date: 2008-05-15 07:41
:category: Plone

`|image0|`_\ (This is essentially a reiteration of `Carlos' previous
blog entry`_. :-))

It just occurred to me that we should probably be using `Supervisor`_
all over the place in our buildouts. Here's why:

-  Starting and stopping Zope and ZEO separately is no fun.
-  Using Supervisor is easy and fun.

Here's how to do it:

-  Add a part to your buildout.cfg file (this is the fun part):

::

    parts =...supervisor...[supervisor]recipe = zc.recipe.eggegg = supervisor

-  Create a configuration file (this is not as fun; we need a recipe for
   this!) in your buildout called etc/supervisord.conf and add the
   following (cargo-cult style):

::

    [inet_http_server]port=127.0.0.1:9999#username=admin#password=admin[supervisord]logfile=%(here)s/../var/log/supervisord.loglogfile_maxbytes=50MBlogfile_backups=10loglevel=infopidfile=%(here)s/../var/supervisord.pidnodaemon=false[rpcinterface:supervisor]supervisor.rpcinterface_factory =     supervisor.rpcinterface:make_main_rpcinterface[supervisorctl]serverurl=http://127.0.0.1:9999[program:zeo]command = %(here)s/../parts/zeo/bin/runzeopriority = 10[program:zope]command = %(here)s/../parts/instance/bin/runzopepriority = 20redirect_stderr = true

(Uncomment the admin lines if you want to password protect your
supervisor.)

.. raw:: html

   </p>

.. raw:: html

   <p>

That's it! Now you can run buildout as normal:

::

    bin/buildout

and then start  supervisor:

::

    bin/supervisord

and then use supervisorctl to start and stop your Zope and ZEO at the
same time (for fun and profit):

::

    bin/supervisorctl start allbin/supervisorctl stop all

You even get a nice web interface for free:

.. raw:: html

   </p>

`|Supervisor rocks!|`_

.. raw:: html

   <p>

How cool is that? Incidentally, one thing I have always found confusing
is how to stop supervisord:

::

    bin/supervisorctl shutdown

So as you can see I'm happy about this, but what would make me even
happier is:

-  A buildout recipe that generates a supervisord.conf file 'on the fly'
   (i.e. when buildout runs).
-  A paster template that includes Supervisor and ZEO (perhaps a cross
   between plone\_hosting and plone3\_buildout?).
-  A Unified Installer that includes Supervisor.
-  A port of Supervisor to Windows (/me ducks).

Thoughts?

.. raw:: html

   </p>

Thanks Chris McDonough of `Agendaless Consulting`_ and Mike Naberezny of
`Maintainable Software,`_ plus `contributors`_ for creating/maintaining
Supervisor and making my job easier :-)

(And thanks Chris and Carlos for the example configuration files `here`_
and `here`_.)

.. _|image2|: http://aclark4life.files.wordpress.com/2008/05/supervisor.png
.. _Carlos' previous blog entry: http://blog.delaguardia.com.mx/index.php?op=ViewArticle&articleId=106&blogId=1
.. _Supervisor: http://supervisord.org
.. _|image3|: /Members/aclark/supervisor-rocks/image/image_view_fullscreen
.. _Agendaless Consulting: http://agendaless.com/
.. _Maintainable Software,: http://maintainable.com/
.. _contributors: http://supervisord.org/contributors/
.. _here: http://svn.repoze.org/buildouts/repoze.zope2/trunk/etc/supervisord.conf
.. _here: http://blog.delaguardia.com.mx/index.php?op=ViewArticle&articleId=106&blogId=1

.. |image0| image:: http://aclark4life.files.wordpress.com/2008/05/supervisor.png
.. |Supervisor rocks!| image:: Picture2.png/image_preview
.. |image2| image:: http://aclark4life.files.wordpress.com/2008/05/supervisor.png
.. |image3| image:: Picture2.png/image_preview
