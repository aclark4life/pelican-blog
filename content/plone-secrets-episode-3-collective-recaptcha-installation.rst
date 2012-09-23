Plone secrets: Episode 3 - Collective Recaptcha installation
############################################################
:date: 2011-08-09 12:19
:tags: Plone

***Another one from the: "wow, this approach is totally and completely
non-obvious to beginners" department.***

My kingdom for a (custom) contact form (with captcha)
=====================================================

I don't know if I've made written-mention of this anywhere else, but
`aclark.net`_\ has a new customized `contact form`_ with captcha. ;-)
`|image0|`_ It is customized via `z3c.jbot`_ which is an awesome tool
(more on that later). This in and of itself is not-so-terribly
newsworthy. What is interesting, though, is *how* this new customized
form came to be; and how its features compare to the default contact
form.

So here goes: In Plone, we have a page template called
`contact-info.cpt`_. It's not so special (in that it is pretty
feature-\ *less*, though it will send mail if you ask it to) but it does
the job for most folks. And it almost has to, because customizing it is
beyond the realm of what *anyone* would call "straight forward" or
"reasonable to expect from TTW customizers, integrators, or even
developers"¹.

Why do I say this?

Been there, done that: CMFFormController
========================================

First, let me start with the technology that is used to implement the
contact form. It's called `CMFFormController`_ and it went out of style
in the 1970s, along with disco and bell bottoms. Bell bottoms came back,
but CMFFormController didn't! Don't get me wrong: CMFFormController is a
decent technology/implementation. It works. But it's not very "modern"
by today's coding standards. As such, it will simply be dragged along
Plone-version-after-Plone-version until either: a.) someone wants to
replace it, or b.) it becomes too big of a maintenance burden to support
and someone has to replace it. This is the way of many things, and there
is nothing inherently wrong with this phenomenon. In fact, there are
even good things about it: e.g. the release manager, framework team, and
core developers' ability to publish release-after-solid-release under
such code-aging circumstances is a testament to their skill and
dedication.

BUT… and this is a BIG BUT.

We can do better
================

Leaving this old stuff laying around, with no new stuff to point new
users to does a huge disservice to *all* of our users. It flies
*directly* in the face of one of our core missions: as `Wyn Williams`_
put it once, to be the

    **"best damn enterprise content manage system on the planet".**

Now, I've been around the block, so I am not suggesting we must fix
everything at once. Legacy software can be supported for years and years
and years (and `YEARS`_). What I am suggesting is that we need to make a
very significant effort to **COMPLETELY HIDE** these implementation
details to newcomers. I don't want to tell people in IRC to go to
**portal\_skins** anymore. I want my "OS X Lion release for Plone",
please (sans Vista overtones.) :-)

So how do we get there? Well, in the case of portal\_skins there is talk
of decommissioning **portal\_view\_customizations,** which was supposed
to be the "new portal\_skins" as I understand it. But since half of our
templates are still in CMF skin layers, *and* because this feature was
not technically well received (i.e. it needs *more* features and
development), *and* because **portal\_resources** came along around the
same time as `plone.app.theming`_, folks are considering removing
portal\_view\_customizations. I have no strong opinion about it (other
than I hate the name, too long) and I trust the Framework Team to handle
it. What I do care about is that whatever remains in the ZMI be very
clearly designated as either "new style" or "old style". We can't get
away from the ZMI yet, but portal tools do have title attributes so
let's use them.

Now, we can't ditch **portal\_skins** just yet, and who knows what will
happen with **portal\_view\_customizations**, but the \*minute\* we know
some technology is out of date, we should reveal it in the user
interface (even in the ZMI user interface). E.g.:

`|image2|`_
    Curiously, the attribute that holds this string is lowercase "title"
    (I'd expect camel case Description, though I'm not entirely sure why
    I expect that.)

Hanno Schlichting has made some great progress recently with enhancing
the ZMI for Plone users, especially with regard to\ *file-system vs.
through-the-web* development, and *through-the-plone vs. through-the-zmi
configuration*, e.g.:

`|image3|`_

I love this trend, and would like to see more of it!

Secrets revealed
================

Anyway, I've been dancing around the secrets to be revealed in this blog
post because it is fun to play with the future. And it's important to
work hard toward achieving it. But enough of that, here is what you need
to know today.

Like I said, I customized the contact form.

Old style vs. new style
-----------------------

Back in the "old days" you had to create a CMF skin layer and put a copy
of the template in a directory on the file system, configured as a File
System Directory View. *Everything* used to be customized via skin
layers.

Now-a-days, we have z3c.jbot. Though a bit of a hack², it does exactly
what you'd expect, almost exactly how you'd expect it to. It `doesn't
even require a Python package`_. By convention though, folks typically
do put z3c.jbot template customizations in Python packages.

This requires a few steps.

Step 1: Create a Python package
-------------------------------

First, a Python package. This is relatively simple, so I'm not going to
skip-and-point-you-somewhere-else just yet, I'm going to explain first.
The `gist of it`_ is this:

::

    $ mkdir -p my.package/my/package
    $ touch my.package/setup.py
    $ touch my.package/my/__init__.py
    $ touch my.package/my/package/__init__.py

Now you would edit setup.py and the "middle" \_\_init\_\_.py with code.
Something like this:

::

    #!/bin/sh
    mkdir -p my.package/my/package
    touch my.package/setup.py
    touch my.package/my/__init__.py
    touch my.package/my/package/__init__.py
    cat > my.package/setup.py << EOF
    from setuptools import setup, find_packages
    setup(
        name='my.package',
        packages=find_packages(),
        namespace_packages=[
            'my',
        ]
    )
    EOF
    cat > my.package/my/__init__.py << EOF
    from pkg_resources import declare_namespace
    declare_namespace(__name__)
    EOF

Alternatively, use `ZopeSkel`_ to generate all this boilerplate code for
you. It does a much better, and more complete job than what I have done
here. The important thing is that you *understand what is going on*.

In the case of aclark.net, our Python package is called
`plonetheme.aclarknet`_.

Step 2: Add template overrides
------------------------------

Now that we have a Python package we can start customizing Plone. By
convention, we  create a "templates" directory inside the namespaced
package e.g.:

::

    $ mkdir my.package/my/package/templates

Or you can check out aclark.net's "templates" directory here:

-  `https://github.com/ACLARKNET/aclark\_net\_website/tree/master/src/plonetheme.aclarknet/plonetheme/aclarknet/templates`_

Because of the way z3c.jbot works, in the "templates" directory, we add
files with names that correspond to the Python module we want to
customize. E.g.

-  `https://github.com/ACLARKNET/aclark\_net\_website/blob/master/src/plonetheme.aclarknet/plonetheme/aclarknet/templates/Products.CMFPlone.skins.plone\_templates.contact-info.cpt`_

(For some reason, github thinks that file is binary, so `here are the
contents`_.)

Now, this is the amazing part: in addition to templates in views,
viewlets and portlets, we can customize any `CMF`_ object! E.g. the
`RestrictedPython`_ (more technology anyone?) CMFFormController
validation script used to validate our contact form:

-  `https://github.com/ACLARKNET/aclark\_net\_website/blob/master/src/plonetheme.aclarknet/plonetheme/aclarknet/templates/Products.CMFPlone.skins.plone\_form\_scripts.validate\_site\_feedback.vpy`_

That brings us to adding recaptcha, but first let us finish configuring
template overrides.

Step 3: Configure template overrides
------------------------------------

Now that we have customized Plone templates, we can configure Plone to
use our customizations.

This is done via a technology you may have heard of: `ZCML`_. Using
ZCML, we can tell Plone (or jbot in this case) to use the templates in
our "templates" directory.

The ZCML we are going to use is placed in the "top level" configure.zcml
file in our package. That means we need a top level configure.zcml file:

::

    $ touch my.package/my/package/configure.zcml

Next we add ZCML to "configure our application". Note in addition to the
ZCML used to configure jbot, there is ZCML for Diazo and ZCML to hold
our `Genericsetup customizations:`_

::

    <configure
        xmlns:browser="http://namespaces.zope.org/browser"
        xmlns:genericsetup="http://namespaces.zope.org/genericsetup"
        xmlns:plone="http://namespaces.plone.org/plone"
        xmlns="http://namespaces.zope.org/zope">    <plone:static directory="theme/aclarknet" type="theme" />    <include package="z3c.jbot" file="meta.zcml" />
        <browser:jbot directory="templates" />    <genericsetup:registerProfile
            name="default"
            title="ACLARK.NET, LLC profile"
            description="Installs ACLARK.NET, LLC site
                customizations"
            directory="profiles/default"
            provides="Products.GenericSetup.interfaces.EXTENSION"
            /></configure>

This file is located here:

-  `https://github.com/ACLARKNET/aclark\_net\_website/blob/master/src/plonetheme.aclarknet/plonetheme/aclarknet/configure.zcml`_

In order to see what is really going on, check out this diagram:

`|image4|`_

You can see that everything inside the <configure></configure> tag(s) is
associated with an XML namespace. If you don't add the appropriate
namespace inside the <configure> tag, your configuration will fail
spectacularly (because without the proper XML namespace configured,
there is no code loaded to handle your configuration.)

Step 4: Add recaptcha
---------------------

Now, finally, we get to the exciting part. We have customized our
contact form, but we are receiving a fair amount of spam due to
spammers' ability to automate form submission. To foil the spammers, we
want to add a captcha form that will hopefully require that an actual
human to fill out the form.

Thanks to David Glick and Groundwire, we have `collective.recaptcha`_
which provides an integration of `Google's Recaptcha service`_ into
Plone.

In order to use it, first we add the package to our buildout, e.g.:

::

    …
    [plone]
    # Eggs are Python packages
    eggs +=
    #   Diazo theming
        plonetheme.aclarknet
    #   Add-ons
        collective.portlet.wordpress
        collective.recaptcha# Need zcml for c.recaptcha until 1.1.3 is released
    zcml = collective.recaptcha
    …

See the rest of the file here:

-  `https://raw.github.com/ACLARKNET/aclark\_net\_website/master/buildout.cfg`_

Now run buildout and restart Plone.

With collective.recaptcha installed via buildout, you should now be able
to open http://yoursite:8080/Plone/@@recaptcha-settings to configure
Recaptcha:

 

`|image5|`_

 

(To get a public and private key, you can sign up for recaptcha here:
http://www.google.com/recaptcha)

Lastly, make the appropriate changes to the contact form and validation
script. E.g. `include the captcha image:`_

::

    …
    <tal:block tal:replace="structure
        context/@@captcha/image_tag"/>
    …

And make sure to `validate the submission`_:

::

    …
        # Re-captcha validation
        if not context.restrictedTraverse('@@captcha').verify():
            context.plone_utils.addPortalMessage(_(u'You entered
                an invalid captcha.'), 'error')
            return state.set(status='failure')
        else:
            return state
    …

That's it!

 Notes
======

¹ I'm pushing "reasonable" limits here for argument's sake. For those
who know Plone already, a lot of what might seem impossible to newcomers
is "reasonable" for them. No flames please. Unless you absolutely must.
;-)

² I hear people call it that, though I don't know the details. I assume
it "monkey patches" which template to use at render-time.

 

 

.. _aclark.net: http://aclark.net
.. _contact form: http://aclark.net/contact-info
.. _|image6|: http://aclark4life.files.wordpress.com/2011/08/screen-shot-2011-08-08-at-6-39-21-pm.png
.. _z3c.jbot: http://pypi.python.org/pypi/z3c.jbot
.. _contact-info.cpt: http://svn.plone.org/svn/plone/Products.CMFPlone/trunk/Products/CMFPlone/skins/plone_templates/contact-info.cpt
.. _|image7|: http://laughingsquid.com/
.. _CMFFormController: http://pypi.python.org/pypi/Products.CMFFormController
.. _Wyn Williams: https://twitter.com/#!/asigottech
.. _YEARS: http://pypi.python.org/pypi/Zope2
.. _plone.app.theming: http://pypi.python.org/pypi/plone.app.theming
.. _|image8|: http://aclark4life.files.wordpress.com/2011/08/screen-shot-2011-08-02-at-1-52-10-pm1.png
.. _|image9|: http://aclark4life.files.wordpress.com/2011/08/screen-shot-2011-08-02-at-4-51-49-pm1.png
.. _doesn't even require a Python package: https://github.com/aclark4life/aclark_net_website
.. _gist of it: https://gist.github.com/1123090
.. _ZopeSkel: http://pypi.python.org/pypi/ZopeSkel
.. _plonetheme.aclarknet: https://github.com/ACLARKNET/aclark_net_website/tree/master/src/plonetheme.aclarknet
.. _`https://github.com/ACLARKNET/aclark\_net\_website/tree/master/src/plonetheme.aclarknet/plonetheme/aclarknet/templates`: https://github.com/ACLARKNET/aclark_net_website/tree/master/src/plonetheme.aclarknet/plonetheme/aclarknet/templates
.. _`https://github.com/ACLARKNET/aclark\_net\_website/blob/master/src/plonetheme.aclarknet/plonetheme/aclarknet/templates/Products.CMFPlone.skins.plone\_templates.contact-info.cpt`: https://github.com/ACLARKNET/aclark_net_website/blob/master/src/plonetheme.aclarknet/plonetheme/aclarknet/templates/Products.CMFPlone.skins.plone_templates.contact-info.cpt
.. _here are the contents: http://dpaste.com/589529/
.. _CMF: http://old.zope.org/Products/CMF/
.. _RestrictedPython: http://pypi.python.org/pypi/RestrictedPython
.. _`https://github.com/ACLARKNET/aclark\_net\_website/blob/master/src/plonetheme.aclarknet/plonetheme/aclarknet/templates/Products.CMFPlone.skins.plone\_form\_scripts.validate\_site\_feedback.vpy`: https://github.com/ACLARKNET/aclark_net_website/blob/master/src/plonetheme.aclarknet/plonetheme/aclarknet/templates/Products.CMFPlone.skins.plone_form_scripts.validate_site_feedback.vpy
.. _ZCML: http://plone.org/documentation/manual/theme-reference/buildingblocks/components/wiring
.. _`Genericsetup customizations:`: http://blog.aclark.net/2011/06/20/plone-secrets-episode-1-%e2%80%94-site-actions-contact-link/
.. _`https://github.com/ACLARKNET/aclark\_net\_website/blob/master/src/plonetheme.aclarknet/plonetheme/aclarknet/configure.zcml`: https://github.com/ACLARKNET/aclark_net_website/blob/master/src/plonetheme.aclarknet/plonetheme/aclarknet/configure.zcml
.. _|image10|: http://aclark4life.files.wordpress.com/2011/08/screen-shot-2011-08-09-at-7-01-33-am.png
.. _collective.recaptcha: http://pypi.python.org/pypi/collective.recaptcha
.. _Google's Recaptcha service: http://www.google.com/recaptcha
.. _`https://raw.github.com/ACLARKNET/aclark\_net\_website/master/buildout.cfg`: https://raw.github.com/ACLARKNET/aclark_net_website/master/buildout.cfg
.. _|image11|: http://aclark4life.files.wordpress.com/2011/08/screen-shot-2011-08-09-at-10-49-16-am.png
.. _`include the captcha image:`: http://dpaste.com/589529/
.. _validate the submission: https://github.com/ACLARKNET/aclark_net_website/blob/master/src/plonetheme.aclarknet/plonetheme/aclarknet/templates/Products.CMFPlone.skins.plone_form_scripts.validate_site_feedback.vpy

.. |image0| image:: http://aclark4life.files.wordpress.com/2011/08/screen-shot-2011-08-08-at-6-39-21-pm.png
.. |image1| image:: http://aclark4life.files.wordpress.com/2011/08/1754727518_741e940edf_o.jpg
.. |image2| image:: http://aclark4life.files.wordpress.com/2011/08/screen-shot-2011-08-02-at-1-52-10-pm1.png
.. |image3| image:: http://aclark4life.files.wordpress.com/2011/08/screen-shot-2011-08-02-at-4-51-49-pm1.png
.. |image4| image:: http://aclark4life.files.wordpress.com/2011/08/screen-shot-2011-08-09-at-7-01-33-am.png
.. |image5| image:: http://aclark4life.files.wordpress.com/2011/08/screen-shot-2011-08-09-at-10-49-16-am.png
.. |image6| image:: http://aclark4life.files.wordpress.com/2011/08/screen-shot-2011-08-08-at-6-39-21-pm.png
.. |image7| image:: http://aclark4life.files.wordpress.com/2011/08/1754727518_741e940edf_o.jpg
.. |image8| image:: http://aclark4life.files.wordpress.com/2011/08/screen-shot-2011-08-02-at-1-52-10-pm1.png
.. |image9| image:: http://aclark4life.files.wordpress.com/2011/08/screen-shot-2011-08-02-at-4-51-49-pm1.png
.. |image10| image:: http://aclark4life.files.wordpress.com/2011/08/screen-shot-2011-08-09-at-7-01-33-am.png
.. |image11| image:: http://aclark4life.files.wordpress.com/2011/08/screen-shot-2011-08-09-at-10-49-16-am.png
