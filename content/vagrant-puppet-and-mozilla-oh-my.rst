Vagrant, Puppet and Mozilla, oh my!
###################################
:date: 2011-10-03 17:25
:category: Mozilla, Plone, Python

*Warning: This post is only loosely Python related and not at all Plone
related, but I thought folks might enjoy hearing about Vagrant and
Puppet because these tools may help you do your Plone and Python jobs
better.*

For the past couple weeks I've been working on creating a virtual
machine to bootstrap a kitsune environment. Kitsune is the Django site
that powers support.mozilla.com. I've now reached what I call the **2nd
milestone**.

Milestones
----------

The milestones are as follows:

#. Get the VM running to the point where one can type **./manage.py**
   and receive the help output (and not a traceback). This sounds
   trivial but there is actually a lot of work involved to get to this
   point. Namely, figuring out how to make `Puppet`_ execute each of the
   required steps successfully, together. (You would expect to be able
   to just define the steps in order, but those with this expectation
   will be disappointed. I assume Puppet has their reasons, and they are
   probably even good ones. :-))
#. **Get the VM running to the point where one can open
   http://33.33.33.10:8000 from the host to see kitsune running. Once
   step #1 is done, this is actually easier than it sounds because I'm
   "cheating". Test data has been imported and a syncdb has been run,
   but I'm using supervisor to manage the runserver process (for now).**
#. Get the VM running like it does in production. This will involve
   configuring **Apache**\ and **mod\_wsgi** as well as resolving any
   issues that remain with the app. I'll rely on the kitsune team to
   help with this, as I'm still learning the app. This is the "exciting"
   part for me because I get to learn something new. While Vagrant and
   Puppet are also new to me, I consider these technologies part of my
   "past life" (as a system administrator) and Django sites part of my
   "future life" (as a web developer).

Now about the technologies.

Vagrant
-------

I had heard of `Vagrant`_ before, but never tried it. I am now sorry I
waited so long because the "cool factor" is very high. It requires that
`Virtualbox`_ be installed, which I also danced around for too long
before committing (being a former Parallels user).

.. raw:: html

   </p>

.. raw:: html

   <p>

On OS X Lion[1], installing Vagrant is simply a matter of:

::

    $ gem install vagrant

Once you have \`vagrant\` installed you can do:

::

    $ vagrant init

inside some revision-controlled directory and you have the beginnings of
a virtual machine you can share with the masses. This is how
`kitsune-vagrant`_ was born. Hopefully this shared virtual machine will
eventually make some new developer's life much easier.

.. raw:: html

   </p>

We now arrive at a fork in the road; though Vagrant makes it easy to
follow both paths: Chef or Puppet (it supports both). I don't recall
what made me choose Puppet over Chef, but it might have been that the
`Socorro folks were using it already`_.

Once you decide on Puppet (and assuming you do), it's pretty easy to
figure out that your next move is to create a manifest file for Puppet
to apply[2].

Puppet
------

My knowledge of Puppet is currently quite limited. Specifically, I only
know how to create a manifest file. (Vagrant does the rest!) I imagine
there is much more to Puppet, especially with regard to doing actual
configuration management on production servers. But I have not explored
any of that yet.

.. raw:: html

   </p>

However, I did learn quite a bit about Puppet just from writing the
manifest. The first most important thing I learned is this: **Puppet is
in charge**. It does things the way it wants to and you need to follow
its rules. The first and biggest challenge is to achieve a linear
execution of tasks.

You cannot write rules in order and hope for the best. This will fail
spectacularly when something executes before something else was supposed
to. The way around this is via \`require =>\` statements.

.. raw:: html

   <p>

A grep through kitsune.pp reveals:

::

        require => Exec['git_clone'],
        require => Exec['db_sync'],
        require => Exec['packages_upgrade'],
        require => Exec['packages_update'],
        require => Package[$packages_native],
        require => Exec['git_clone'],
        require => Exec['chown_kitsune'],
        require => Exec['packages_compiled'],
        require => Exec['packages_vendor'],
        require => Exec['db_create'],
        require => Exec['db_import'],
        require => file['/etc/supervisor/supervisord.conf'],
        require => Exec['supervisor_stop'],

This roughly translates to the following workflow logic:

-  Ensure that \`aptitude -y update; aptitude -y upgrade\` have been run
   before you try to install the list of packages we require.
-  Ensure the list of packages we require is installed before we
   checkout the code.
-  Ensure the code has been checked out (and pip install / git submodule
   have been run) before you try to syncdb and run the application.

There is a bit more to it, but with that knowledge you should be able to
`read and understand kitsune.pp in full`_. I learned most of the
remaining required puppeteering from this
site:\ `http://www.puppetcookbook.com/`_.

Mozilla
-------

Oh my! This Mozilla work is a ton of fun[3]; I attribute this in part
due to the structure of their organization: I was invited immediately to
collaborate in IRC with the kitsune team and as a result, we all have
something to show for it[4].

`|image0|`_

Next I will be working on the 3rd milestone! Hope to finish by the end
of this week.

Notes
-----

[1] This did not work on Snow Leopard, because \`gem\` is too old.
However if you \`brew install ruby\` and try again, it should work.

.. raw:: html

   </p>

[2] I didn't bother to investigate Chef, but I am curious about it.

[3] And I hope this is only the beginning.

[4] I hope to get a Mozilla gig but even if I don't, being able to do
this type of work is very rewarding (which is why you will often hear
people in open source say that to get paid for the type of work they do
is a dream come true :-)).

 

.. _Puppet: http://puppetlabs.com/
.. _Vagrant: http://vagrantup.com/
.. _Virtualbox: https://www.virtualbox.org/
.. _kitsune-vagrant: https://github.com/aclark4life/kitsune-vagrant
.. _Socorro folks were using it already: https://github.com/rhelmer/socorro-vagrant
.. _read and understand kitsune.pp in full: https://github.com/aclark4life/kitsune-vagrant/blob/master/manifests/kitsune.pp
.. _`http://www.puppetcookbook.com/`: http://www.puppetcookbook.com/
.. _|image1|: http://aclark4life.files.wordpress.com/2011/10/screen-shot-2011-10-03-at-5-12-42-pm.png

.. |image0| image:: http://aclark4life.files.wordpress.com/2011/10/screen-shot-2011-10-03-at-5-12-42-pm.png
.. |image1| image:: http://aclark4life.files.wordpress.com/2011/10/screen-shot-2011-10-03-at-5-12-42-pm.png
