RE: collective.recipe.supervisor: Thank you!
############################################
:date: 2008-08-10 05:24
:tags: Plone

Since I `last wrote about supervisor`_ it's become even more easy and
more fun to add it to your buildout with
`collective.recipe.supervisor`_. I **really** appreciate what this
recipe allows me to do (because it makes my job/life so much easier) and
I want to publicly thank `Mustapha Benali, Author & Hanno Schlichting,
Contributor`_.

Now, it is as simple as editing your buildout.cfg like so:

.. raw:: html

   <p>

1. Add a part for supervisor:

::

    [buildout]
        parts =
            ...
            supervisor

2. Create the part:

::

    [supervisor]
    recipe = collective.recipe.supervisor
    programs =
        10 zeo ${zeo:location}/bin/runzeo ${zeo:location}
        20 instance ${instance:location}/bin/runzope ${instance:location} true

3. Run buildout:

::

    ...
    Installing supervisor.
    Getting distribution for 'supervisor'.
    Got supervisor 3.0a6.
    Getting distribution for 'elementtree>=1.2.6,<1.2.7'.
    zip_safe flag not set; analyzing archive contents...
    Got elementtree 1.2.6-20050316.
    Getting distribution for 'meld3>=0.6.4'.
    zip_safe flag not set; analyzing archive contents...
    Got meld3 0.6.5.
    Getting distribution for 'medusa>=0.5.4'.
    zip_safe flag not set; analyzing archive contents...
    Got medusa 0.5.4.
    Generated script '/Users/aclark/Developer/supervisor-recipe-test/bin/supervisord'.
    Generated script '/Users/aclark/Developer/supervisor-recipe-test/bin/memmon'.
    Generated script '/Users/aclark/Developer/supervisor-recipe-test/bin/supervisorctl'.

4. Start supervisor in the foreground:

::

    $ bin/supervisord -e debug -n
    2008-08-27 06:40:34,805 INFO Increased RLIMIT_NOFILE limit to 1024
    2008-08-27 06:40:35,036 INFO RPC interface 'supervisor' initialized
    2008-08-27 06:40:35,036 WARN cElementTree not installed,
        using slower XML parser for XML-RPC
    2008-08-27 06:40:35,036 CRIT Server 'inet_http_server' running without
        any HTTP authentication checking
    2008-08-27 06:40:35,037 INFO supervisord started with pid 99684
    2008-08-27 06:40:36,041 INFO spawned: 'zeo' with pid 99686
    2008-08-27 06:40:36,049 INFO spawned: 'instance' with pid 99687
    2008-08-27 06:40:37,051 INFO success: zeo entered RUNNING state,
        process has stayed up for > than 1 seconds (startsecs)
    2008-08-27 06:40:37,051 INFO success: instance entered RUNNING state,
        process has stayed up for > than 1 seconds (startsecs)
    2008-08-27 06:40:41,574 DEBG 'instance' stdout output:
    2008-08-27 06:40:41 INFO ZServer HTTP server started at Wed Aug 27 06:40:41 2008
        Hostname: localhost
        Port: 8080...2008-08-27 06:41:28,396 DEBG 'instance' stdout output:
    2008-08-27 06:41:28 INFO Application New disk product detected,
        determining if we need to fix up any ZClasses.2008-08-27 06:41:28,452 DEBG 'instance' stdout output:
    2008-08-27 06:41:28 INFO Zope Ready to handle requests

5. When everything looks ok, start supervisor 'for real':

::

    bin/supervisord

6. Once running, you can:

-  Check status:

::

    $ supervisorctl status
    instance                         RUNNING    pid 99889, uptime 0:00:04
    zeo                              RUNNING    pid 99888, uptime 0:00:04

-  Start/stop Zope/ZEO in various ways:

::

    $ bin/supervisorctl stop instance
    instance: stopped$ bin/supervisorctl stop zeo
    zeo: stopped$ bin/supervisorctl start zeo
    zeo: started$ bin/supervisorctl start instance
    instance: started$ bin/supervisorctl stop all
    zeo: stopped
    instance: stopped$ bin/supervisorctl start  all
    zeo: startedinstance: started

and generally go about your business, unfettered.

.. raw:: html

   </p>

.. _last wrote about supervisor: /Members/aclark/supervisor-rocks/
.. _collective.recipe.supervisor: http://pypi.python.org/pypi/collective.recipe.supervisor/0.4
.. _Mustapha Benali, Author & Hanno Schlichting, Contributor: http://pypi.python.org/pypi/collective.recipe.supervisor/0.4#contributors
