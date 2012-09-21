Hostout rules
#############
:date: 2011-01-26 15:17
:tags: Plone

*As in "dominates", not a "list of rules" :-)*

I spent a long time avoiding `collective.hostout`_ for reasons I will
call "technical stylistic differences" with the author Dylan Jay.

But then I grew up (and in cases of Plone growth like this, I usually
end up crediting the probably-much-younger-than-me-in-years,
but-certainly-much-more-possessive-of-sage-like-wisdom-than-me-Martin-Aspeli;
and this time is certainly no exception. So thanks Martin!)

As it turns out, Hostout (as I like to call it now, because we are on a
first name basis) is awesome! Let me break down the awesomeness for you.

Buildout
~~~~~~~~

It starts with Buildout. I won't bore you with the details of why
Buildout is awesome, but I will mention one key feature:

-  INI-style configuration, y'all.

Sometimes you just want to specify something like:

::

    [foo]
    bar = baz

and be done. I am not making this up folks. There is something about
INI-style configuration that transcends time and space, and reaches
across partisan-aisles to bring folks together in a "let's just get this
done" sort of way. Of course not everyone likes them, but if you are a
technical person and don't like them, I guarantee you at least
understand them and can see why they might be appropriate in some cases
over another technology.

.. raw:: html

   </p>

Anyway, back to the awesomeness.

Fabric
~~~~~~

Fabric is awesome! I won't bore you with the details of why Fabric is
awesome. But I will mention one key feature:

-  SSH, people. SSH.

Sometimes you just want to type:

::

    $ fab -H foo.com bar

and be done. Fabric lets you execute the Python code you wrote in a
function called "bar", inside a (local) file called fabfile.py, on a
(remote) host called foo.com. All with the touch of a button, so to
speak. That is to say, you create a local fabfile.py file, and Fabric
runs the code remotely for you on any number of hosts you give it.
Brilliant.

.. raw:: html

   </p>

Now, what could be better than these two technologies? These two
technologies *together*, that's what. (See where I am going with this?)
And what could be better than joining these two technologies? Joining
them with *absolutely no effort required on your part whatsoever*,
that's what.

I have a long history of touting software that makes my job (and life)
easier, and Hostout fits right in with that tradition. I'm just sorry it
took me this long to try it out.

Hostout
~~~~~~~

As compelling as it is to write "pure Python" in fab files, and it is,
sometimes you just want to be done. And Hostout helps you get there. I
will explain in a minute, but first a slight detour.

Back story
^^^^^^^^^^

I recently blogged about the relaunch of this website `here`_. Shortly
after the launch, I realized I needed a quick and easy way to deploy my
staging site to production. I pitched the idea of a utility called
"mr.pusher" to accomplish this task to Dylan, with the caveat that I was
interested in making it work with Hostout.

.. raw:: html

   </p>

As it turns out, between Hostout and a recipe I created years ago called
`collective.recipe.rsync`_, "mr.pusher" almost already existed. Now back
to the story.

Fabric integration made easy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Since I knew I wanted to be able to execute a "push" command remotely, I
figured I would finally get acclimated with Hostout.

.. raw:: html

   </p>

.. raw:: html

   <p>

After a small wrestling match in my head with the docs, I came up with
`this`_:

::

    # Hostout makes Fabric integration easy
    [staging]
    recipe = collective.hostout
    host = aclark.net
    path = /srv/staging[production]
    recipe = collective.hostout
    host = aclark.net
    path = /srv/aclark_net_website

At this point (after running buildout) I was able to perform such great
feats of remote administration (on my already-deployed-sans-hostout
sites) as:

::

    $ bin/hostout staging run git pull
    $ bin/hostout staging run bin/buildout -c staging.cfg

Armed with this ability, I added the following to my `staging.cfg:`_

::

    # Create scripts to deploy staging data to production.
    # Be VERY careful with this. You could easily overwrite your
    # live production data if you either forget to use the script
    # option, or accidentally run the bin/rsync-filestorage-to-production
    # script without stopping the production site first.
    [filestorage-to-production]
    recipe = collective.recipe.rsync
    source = var/filestorage/Data.fs
    target = ../aclark_net_website/var/filestorage/Data.fs
    script = true[blobstorage-to-production]
    recipe = collective.recipe.rsync
    source = var/blobstorage/
    target = ../aclark_net_website/var/blobstorage/
    script = true

The result was two scripts I could use to "push" staging to production,
but only after stopping the production site first:

::

    $ bin/hostout production run bin/supervisorctl shutdown
    $ bin/hostout staging run bin/rsync-filestorage-to-production
    $ bin/hostout staging run bin/rsync-blobstorage-to-production
    $ bin/hostout production run bin/supervisord

And we're deployed! This technique is particularly elegant when used in
combination with a\ `custom 503`_.

Conclusion
~~~~~~~~~~

I really like this setup, and I really appreciate what Hostout gets me
"for free"; I didn't have to create a fabfile.py, I just configured my
staging and production host parameters in buildout.cfg and off I went.

.. raw:: html

   </p>

Of course, there is always room for improvement. The next most logical
step for me would be to add cloud integration. If I could provision a
new Rackspace cloud server via buildout, and then host-it-out, I think
the future will have arrived. And since that is exactly what
`hostout.cloud`_ appears to do, welcome to the future!

Alex Clark (January 2011)

*Did you enjoy reading this article? Please consider `helping me help
Plone in February 2011`_.*

.. _collective.hostout: http://pypi.python.org/pypi/collective.hostout
.. _here: http://blog.aclark.net/2011/01/19/new-website-for-2011/
.. _collective.recipe.rsync: http://pypi.python.org/pypi/collective.recipe.rsync
.. _this: https://github.com/aclark4life/aclark_net_website/blob/master/buildout.cfg#L64
.. _`staging.cfg:`: https://github.com/aclark4life/aclark_net_website/blob/master/staging.cfg
.. _custom 503: https://github.com/aclark4life/aclark_net_website/blob/master/apache.conf
.. _hostout.cloud: http://pypi.python.org/pypi/hostout.cloud
.. _helping me help Plone in February 2011: http://blog.aclark.net/2011/01/21/help-alex-clark-help-plone/
