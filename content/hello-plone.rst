Hello Plone
###########

:date: 2011-08-20 20:27
:tags: Plone, Python

This is a "hello world" style tutorial/application for Plone, aimed squarely at Python developers. I have created a project on Github too, to hold the code:

- `https://github.com/aclark4life/hello\_plone`_

Step 1 - Setup
==============

Everyone in the Python world loves virtualenv, so this step will be a familiar one. Inside the hello\_plone repo, I first create a virtualenv:

::

    $ virtualenv .

I then install some additional tools:

::

    $ bin/pip install zc.buildout

As you see, Plone uses Buildout. One day it may not, but for now it does. Get over it. ;-) (Or better yet, help us figure out how to make Buildout optional in Plone. Many would welcome the improvement, and hail you as their conquering hero!) Until then:

::

    $ bin/buildout init

Edit your buildout.cfg and put this in it:

::

    [buildout]
    extends = http://raw.github.com/pythonpackages/buildout-plone/master/4.3.x

That's it. Now run buildout:

::

    $ bin/buildout

It will take some time to download all the packages, but you only have to do this once. Afterward, you can configure a global packages directory and share that amongst all your development projects. See the `zc.buildout 1.5.2 page on PyPI`_ to find out more. When it finishes, do this:

::

    $ bin/plone fg

Then open http://localhost:8080. 

Click the button and follow the steps. You don't need to select any additional add-ons from the list. Afterward, you should get a Plone site here: http://localhost:8080/Plone.

Step 2 - Develop
================

There are a ton of things you can do in Plone, but it is primarily a "content management system" meaning, "you put your website in it."¹ And I don't mean your "crazy cool next gen web app" website. I mean your web. site. The one you use for you or your business or church or band or bridge club or whatever. Since this is a "hello world" demonstration, I am going to show you how to start writing Python code whose results will "show up on the screen" in short order. After that, I'll point you to some next steps. So, to develop we need a Python package. Create your own, or use zopeskel (paster wrapped in some "user friendliness"). Or use paster with the zopeskel templates installed.

::

    $ bin/pip install zopeskel
    $ bin/zopeskel plone_basic my.app

    plone: A project for Plone add-ons

    …

Now that we have a Python package, we want to "load it in Plone". To do that, we need to add the package to our buildout. Fortunately, buildout has a mechanism for this particular use case built in. It's called a "develop egg", and it is configured via the \`develop\` parameter available in the \`buildout\` section. Additionally, we need to "tell Plone" about our develop egg too. But this is done in the same way you tell Plone about any other package. You add it to the \`eggs\` parameter of the \`plone.recipe.zope2instance\` section. So now we have:

::

    [buildout]
    develop = ./my.app
    extends = http://build.pythonpackages.com/buildout/plone/4.2.x-dev

    [plone]
    eggs += my.app

Now let's write some code. We are going to: "wire up a template to a view", say "hello world!" then "call it a day". This is accomplished via some "goo" maintained by the `Zope Toolkit project`_:

::

    from Products.Five.browser.pagetemplatefile import 
        ViewPageTemplateFile
    from zope.publisher.browser import BrowserPage

    class Hello(BrowserPage):
        """
        Wire up some goo
        """

        template = ViewPageTemplateFile('hello.pt')

        def __call__(self):
            return self.template()

And it can go in: ***my.app/my/app/hello.py*.** Now, because Plone uses the `Zope component architecture`_, we need to "wire up" the "component" we just created. This is done via the `Zope Configuration Markup Language`_:

::

    <configure
        xmlns:browser="http://namespaces.zope.org/browser">

        <browser:page

            for="*"
            name="hello"
            permission="zope2.View"
            />

    </configure>

And it goes in: ***my.app/my/app/configure.zcml***. It "just works" because we include an `entry point in our setup.py`_ to make it so (paster took care of that, in this case.) Lastly, create: ***my.app/my/app/hello.pt.*** And put "Hello world!" in it. Stop and start Plone (i.e. CTRL-C, bin/plone fg) and then open: http://localhost:8080/Plone/hello.

Nice, but a little boring. At the very least, let us get our "hello world!" to show up "in Plone". To do this, we simply invoke Plone's main\_template and insert our text into the main content area. Add the following to ***my.app/my/app/hello.pt.***

::

    <div metal:use-macro="here/main_template/macros/master">

        <div metal:fill-slot="main">

            <h1>Hello world!</h1>

        </div>

    </div>

As you can see, we are using `Zope Page Templates`_. ZPTs must be valid XHTML, much to the `chagrin of Django's creators`_. But in addition to the main con: "making humans edit XML is sadistic!") there are some pros too e.g. "Play nicely with editing tools." In other words, get over it.  ;-) (Or better yet, add support for using alternative template languages in Plone. I have no idea what the technical feasibility is, but it might be worth some effort.)

Step 3 - Fun/profit!
====================

That's not so bad you say? (That is what I am hoping you will say!) Great. Some good next steps are:

-  Theming with Diazo and `plone.app.theming`_.
-  Content types with Dexterity and `plone.app.dexterity`_.
-  Easy through-the-web form generation with `PloneFormGen`_.

Also, check out the Plone `community managed developer documentation`_ on readthedocs.org for more! ¹ c.f. SNL skit w/Rob Schnieder and/or Adam Sander too, apparently: `http://www.youtube.com/watch?v=muA5EBmpDhA`_ I like the Rob Schnieder ones better :-)

.. _`https://github.com/aclark4life/hello\_plone`: https://github.com/aclark4life/hello_plone
.. _zc.buildout 1.5.2 page on PyPI: http://pypi.python.org/pypi/zc.buildout/1.5.2#user-defaults
.. _Zope Toolkit project: http://docs.zope.org/zopetoolkit/
.. _Zope component architecture: http://pypi.python.org/pypi/zope.component/3.10.0
.. _Zope Configuration Markup Language: http://pypi.python.org/pypi/zope.configuration/3.7.4
.. _entry point in our setup.py: http://pypi.python.org/pypi/z3c.autoinclude/0.3.4
.. _Zope Page Templates: http://docs.zope.org/zope2/zope2book/ZPT.html
.. _chagrin of Django's creators: https://docs.djangoproject.com/en/dev/topics/templates/#templates
.. _plone.app.theming: http://pypi.python.org/pypi/plone.app.theming/1.0b8
.. _plone.app.dexterity: http://pypi.python.org/pypi/plone.app.dexterity/1.0.1
.. _PloneFormGen: http://pypi.python.org/pypi/Products.PloneFormGen/1.7b5
.. _community managed developer documentation: http://collective-docs.readthedocs.org
.. _`http://www.youtube.com/watch?v=muA5EBmpDhA`: http://www.youtube.com/watch?v=muA5EBmpDhA
