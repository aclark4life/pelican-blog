We Pioneer
==========

:date: 2014-05-03 10:15
:tags: Django, Plone, Python

.. image:: /images/we-pioneer.jpg
    :alt: alternate text

One of the subjects I find myself thinking about a lot is: Plone (surprise!) In Plone-land, we deliver the **best Python-based CMS money can't buy on top of an aging Zope 2 "application server"** mixed with newer Zope, Python, and other technologies. In short, this is a challenge.

Diazo
-----

Further to the point, I think about "new tech" vs "old tech" a lot and how to happily marry the two. Here is one concrete example of my thought process. Diazo is the "new theming engine" in Plone which allows folks to perform complex XSLT transformations via a simple XML rule set. It sounds great, and it often is. But something won't let my mind reach the "Ahhhh this is great technology!" point. Instead, I often find myself thinking "This is great technology, BUT…" which I don't want to think when I'm thinking about Plone. 

Pioneering
~~~~~~~~~~

However I'm beginning to settle on an "acceptable thought process", to describe how Diazo fits on top of 10 years of legacy Plone technology: it's **pioneering**. As I have observed over the years, Plone developers have taken great pride in being the "first to market" with cutting edge and useful CMS features other vendors would love to include in their product.

*But are other CMS vendors watching?*

Issues
~~~~~~

Of issue with Diazo is: 

1. **Most web developers are familiar with the concept of editing templates to affect output** (AKA "customization"). When Zope 2 was young, the only place to easily customize templates was within the web application itself, with changes persisted to the ZODB. Then "ZODB dread" [1]_ happened and folks began to customize templates on the file system with software version control in place. During this time, customizations happened on the file system via the CMF framework built on top of Zope 2. Then Zope 3 happened and folks began to customize templates on the file system with more modern web technology (AKA "pseudo-MVC-like environments"). Then Deliverance [2]_ happened and folks began to leave the complex stack alone in favor of using XSLT transforms to produce a hybrid output containing both clean, isolated HTML/CSS/JavaScript and Plone content (AKA "lipstick on a pig").

#. **Plone now has two distinct templating environments**: the application environment which still has plenty of templates to customize & the theming environment which also has templates to customize. This is both good and bad: it's good when everyone can easily figure out where to customize what they want to customize, and bad when this process breaks down.

#. **Diazo allows for some complex rules to be written** along with custom XSLT. That power allows folks to produce some truly unwieldy and wholly unmaintainable messes, for lack of a better description. I'm sad to say I've seen many of these in the wild, in just the few short years Diazo has existed.

Conclusion
~~~~~~~~~~

After all this thinking, I've reached the following conclusion(s):

1. **The concept of editing templates most web developers are familiar with is still valid in Plone.** But we must work harder to demonstrate where and how these customizations can occur. With great tools comes great power, but not without significant risk of injury (the so-called "power tool" analogy.)

#. **We should strive for the appearance of one templating environment.** The easiest way to do this is to have only one templating environment. Many electronic flames have been burned over the discussion of making Diazo that single environment. In the meantime let's disassemble, polish & reassemble all of our templating environments and put effort in to making the difference between them seemless. (`zope2_bootstrap <http://pypi.python.org/pypi/zope2_bootstrap>`_ anyone?)

#. **We should actively discourage complex rules and custom XSLT**. Of course, these knobs are nice to turn when you need them. But I don't want to read through complex rules and custom XSLT anymore than I want to see inline JavaScript or CSS. (AKA "This is why we can't have nice things.")

*And other CMS vendors should be watching, because Plone 5 is about to drop!*

(*You should probably* `hire me <http://aclark.net>`_ *or* `follow me on Twitter <http://twitter.com/aclark4life>`_ *or both*.)

.. [1] The fear all your hard work and customizations are trapped inside an unwieldy ZODB, with no easy way to persist or track them elsewhere.

.. [2] Early, pioneering implementation which inspired Diazo.
