Hello Plone
================================================================================

:date: 2011-08-20 20:27
:tags: Plone, Python

This is a Plone "Hello, World!" style tutorial/application for Python programmers. See https://github.com/aclark4life/hello_plone for more.

.. Note:: This post has been edited post-publication to improve the wording.

.. Warning:: This is not a particularly good example since a template can be specified via ZCML. However once you understand hello_plone you will understand the difference between the two approaches.

Step 1 - Setup
--------------------------------------------------------------------------------

Create a directory called ``hello_plone`` and inside it create a ``virtualenv``::

    $ mkdir hello_plone
    $ cd hello_plone
    $ virtualenv-2.7 .

Then install Buildout::

    $ bin/pip install zc.buildout

Then create an empty buildout::

    $ bin/buildout init

Then add a Plone buildout::

    [buildout]
    extends = https://raw.github.com/plock/pins/plone-4-3

Now run Buildout::

    $ bin/buildout

And start Plone::

    $ bin/plone fg

Open http://localhost:8080. 

Click the button and follow the steps. You don't need to select any additional add-ons from the list. Afterward, you should see your Plone site here: http://localhost:8080/Plone.

Step 2 - Develop
--------------------------------------------------------------------------------

Plone is customized via Python packages called Add-ons (née Products). So first we need to create a Python package::

    $ mkdir -p my.app/my/app
    $ touch my.app/my/app/__init__.py
    $ touch my.app/my/__init__.py

Next we add our Python package to the buildout. The ``develop`` line makes the buildout aware of the Python package. The ``eggs`` line makes Plone aware of it::

    [buildout]
    develop = ./my.app
    extends = https://raw.github.com/plock/pins/plone-4-3

    [plone]
    eggs += my.app

Now we can add some view code::

    from Products.Five.browser.pagetemplatefile import 
        ViewPageTemplateFile
    from zope.publisher.browser import BrowserPage

    class Hello(BrowserPage):
        """
        """

        template = ViewPageTemplateFile('hello.pt')

        def __call__(self):
            return self.template()

And load the view code via `ZCML <http://developer.plone.org/components/zcml.html>`_::

    <configure
        xmlns:browser="http://namespaces.zope.org/browser">

        <browser:page
            class=".hello.hello"
            for="*"
            name="hello"
            permission="zope2.View"
            />

    </configure>

And add a `template <http://developer.plone.org/templates_css_and_javascripts/template_basics.html>`_::

    <div metal:use-macro="here/main_template/macros/master">

        <div metal:fill-slot="main">

            <h1>Hello world!</h1>

        </div>

    </div>

Step 3 - Next steps
--------------------------------------------------------------------------------

- Easy through-the-web form generation with `PloneFormGen <http://developer.plone.org/reference_manuals/active/ploneformgen/>`_.
- Content types with `Dexterity <http://developer.plone.org/content/dexterity.html>`_.
- Theming with `Diazo <http://developer.plone.org/templates_css_and_javascripts/diazo.html>`_. 
