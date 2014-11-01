Hello Plone Updated
===================

:date: 2014-01-11 12:30
:tags: Plone, Python

.. image:: images/hello-plone-updated.jpg
    :alt: alternate text

Over two years ago I wrote a blog entry called `"Hello, Plone!" <http://blog.aclark.net/2011/08/20/hello-plone/>`_. I've just updated it in order to:

- Change the wording
- Update the links 
- Add some comments

What's changed?
---------------

As change in technology is constant, you can expect a few details to differ between then and now. Though I generally don't like the term "best practice" I do like to write about "how I do it now" vs "how I did it then".

Buildout
~~~~~~~~

Since "Hello, Plone!" was published Buildout 2.0.0 was released and **Buildout has given up on attempting to provide module isolation** in the same way Virtualenv that does. Why? Virtualenv does it better. So if you want to isolate your development from a larger Python installation, use Virtualenv. I routinely use both Buildout and Virtualenv.

Buildout hosting
~~~~~~~~~~~~~~~~

Ever since I wrote `Plone 3.3 Site Administration <http://www.packtpub.com/plone-33-site-administration/book>`_ I've been maintaining a collection of buildouts. Most recently, I've moved them to a project called `Plock <http://plock.github.io>`_. You can also find a bunch of archived buildouts here: https://github.com/buildouts.

ZopeSkel
~~~~~~~~

For folks new to Plone and Python development, it's often helpful to use a code generator to get started developing. The original ``hello_plone`` included some ZopeSkel instructions. In this round, I've opted to include manual instructions instead e.g.::

    $ mkdir -p my.app/my/app
    $ touch my.app/my/app/__init__.py
    $ touch my.app/my/__init__.py
    $ touch my.app/my/app/configure.zcml

Why? Generally speaking, I now prefer to educate folks about Python packaging more so than code generation.

Check out the new old post here: http://blog.aclark.net/2011/08/20/hello-plone/.
