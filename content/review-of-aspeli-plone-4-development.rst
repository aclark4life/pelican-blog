
Review of Aspeli's Professional Plone 4 Development
===================================================

:date: 2012-10-20 19:15
:tags: Plone

*I owe PACKT a review of this book, so here it is.*

First: I liked it. Second: I appreciate Aspeli writing it. Third: Like many others, I couldn't wait for it to come out. Fourth: I know that it was a **TON OF WORK** and **PROBABLY NOT WORTH THE MONEY** to write it. So why write a Plone book? A few reasons (other than money):

- It's good for you
- It's good for the community
- It's good for Plone

So if you care about Plone: please go buy both an electronic and paper version of this book **RIGHT NOW** [0]_. While you are at it, please pick up a copy of **Plone 3.3 Site Administration**. It's quite good, and I hear the author is a **swell guy** and would most certainly appreciate your generosity [1]_ [2]_.

What I like
-----------

First let me cover what I **ABSOLUTELY LOVE** about this book.

buildout:eggs
~~~~~~~~~~~~~

.. image:: https://raw.github.com/ACLARKNET/aclarknet.github.com/master/images/buildout.png

Aspeli correctly addresses one of my biggest pet peeves (concerns) about what I believe to be an **ANTI-PATTERN** in almost every Plone buildout: buildout:eggs (referring to the eggs parameter of the buildout section; it does not exist, other than as a convenient variable setting).

If you know me, you know I've spoken about this before and whilst I've moved on from harping on it I will say this: with most software that uses ini-style configuration files when you set a parameter you expect something to happen. But since Buildout is more complicated than the average software that uses ini-style configuration, that expectation is not always met.

Add-ons
~~~~~~~

.. image:: https://raw.github.com/ACLARKNET/aclarknet.github.com/master/images/addons.png

Did you see? You might have missed it. No mention of **Products** WHAT-SO-EVER. "Product" was a term that Zope2 used for Python libraries that enhanced the functionality of Zope2, and it stuck. Now, it should die in favor of something everyone else in the world understands: add-on. Well played, Aspeli. Well played.

The Review
----------

I will now talk about each chapter briefly. This will be TL;DR-style, but I hope you'll get a nice idea for why this book is so great. If you have any questions, please don't hesitate to ask them in the comments.

Chapter 1: Plone in Context
~~~~~~~~~~~~~~~~~~~~~~~~~~~

In which we learn what, why & when Plone is, plus a bit more. My favorite sub-section is: Plone-the-application and Plone-the-framework, in which Aspeli describes the phenomenon of Plone the application being used by some folks as a generic Python web framework. Plone's strengh and indeed its raison d'etre (reason to exist) is to provide a fully-featured CMS web application suitable for immediate use, or use immediately after a few simple customizations. So if you try to use it as a web framework, you may not get exactly what you expect (because it was not designed to be used that way).

Chapter 2: Introduction to the Case Study
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In which we learn how a professional may execute a typical website project with Plone. This is a nice little chapter with some great details about the fictional project that will be executed throughout the remainder of the book: requirements, mockups, and information architecture are the highlights here; as well as the necessary CMS details like users, groups, and content types.

Chapter 3: The Development Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In which we learn about how to setup an environment in which you can customize Plone to suit your needs. TL;DR: fairly typical Python development environment [3]_ with additional Plone details covered: Buildout recipes, development libraries, and more.

Chapter 4: Basics of Customization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In which we learn about the technical architecture of Plone: ZODB, GenericSetup, Zope2 CMF, Zope Component Architecture, and more (!). And the best way to implement your requirements within that architecture.

Chapter 5: Developing a Site Strategy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In which we learn about how to bundle your customizations into a Python package for general use.

Chapter 6: Security and Workflow
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In which we learn about how Plone implements generic web application features and how you can customize that implementation.

Chapter 7: Using Add-ons
~~~~~~~~~~~~~~~~~~~~~~~~

In which we learn about how to add additional Python libraries to Plone to provide additional features.

Chapter 8: Creating a Custom Theme
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In which we learn about Plone's new theming engine: Diazo.

Chapter 9: Nine Core Concepts of Zope Programming
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In which learn a bit more about the technical architecture of Plone. If you love this chapter (as many do), you might also enjoy: http://developer.plone.org/reference_manuals/old/zope_secrets/index.html.

Chapter 10: Custom Content Types
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In which we learn about Plone's new content type framework: Dexterity.

Chapter 11: Standalone Views and Forms
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In which we learn about a topic that would be first, if Plone were a generic website framework: how to build forms.

Chapter 12: Relational Databases
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In which we learn about how to integrate a relational database into your CMS application. Since Plone relies heavily on the ZODB, none is included by default.

Chapter 13: Users and their Permissions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In which we learn about another topic that would be covered first if Plone were a generic website framework: authentication and authorization.

Chapter 14: Dynamic User Interfaces with jQuery
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In which we learn about using jQuery in Plone.

Chapter 15: Summary and Potential Enhancements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In which we learn about next steps. You've just built and delivered a CMS application for your client. What will they ask you for next? And how will you implement it.

Conclusion
----------

I hope you have enjoyed this review; and I hope you'll consider purchasing a copy of Aspeli's book for your next Plone project.

*Like this article? Consider a* `gittip`_. *You may also want to follow me on* `twitter`_.

.. _`Gittip`: http://gittip.com/aclark4life
.. _`Twitter`: http://twitter.com/aclark4life

.. [0] Disclaimer: I was given a copy of both versions in exchange for this review.

.. [1] Seriously though, whilst PACKT literally forces you to include a software version number in your title, **Plone 3.3 Site Administration** is still relevant to today's Plone. I expect it will be relevant through at least Plone 5.

.. [2] The financial details of (at least) my contract for writing a book with PACKT **CLEARLY FAVORED PACKT**. That said, I think they are a great organization and I am proud to be a PACKT author. But according to my statements, I still need to earn about $1K more in royalties before I have paid back my advance. Notice what I just said there: **earn in royalties** i.e. I have to sell enough books in order to get PACKT to pay out enough money to meet the terms of the contract. I won't pretend to have any idea why PACKT does what it does with its contracts, except to say that I assume they expect to make money. I'll also assume everything is on the up and up. But unfortunately sometimes the "up and up" can look like this: http://www.techdirt.com/articles/20121018/01054720744/hollywood-accounting-how-19-million-movie-makes-150-million-still-isnt-profitable.shtml.

.. [3] ``$ pip install Plone`` support may be available soon which may blow the lid off the Python popularity shack (raise the level of interest from generic Python developers interested in Python CMS applications).
