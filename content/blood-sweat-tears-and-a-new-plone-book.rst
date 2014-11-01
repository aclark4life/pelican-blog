Blood, sweat, tears… and a new Plone book!
================================================================================

:date: 2010-03-30 18:15
:tags: Plone

Well, no blood yet. But certainly sweat and tears! If `Plone Conference
2006`_ was my inspiration for `Plone Conference 2008`_, then
`Professional Plone Development`_ was my inspiration for this book:
`Plone 3.3 Site Administration`_.

For the past 14 months or so, I have been writing a book aimed at end users of Plone; folks that have little knowledge of how to do much more than add content. It is intended to make them feel more comfortable performing various site administrator tasks. Topics like theming, maintenance, and optimization are covered.

But wait, there's more!

#1
--

This book aims to "lower the Plone bar for users of Python". What do I mean by that? Basically this: I love Python almost as much as I love Plone. It lets me translate my thoughts directly into code. I fantasize that with little more than a Python interpreter, one can forge a working Plone site within minutes. But it is not just a fantasy, it is (more or less) the status quo. (Maybe even `MacGyver`_ used Python?)

So, this book begins at the beginning: by making sure folks are comfortable installing and using Python on there operating system of choice (or using the pre-installed Python). If you read *Professional Plone Development*, you may recall Martin Aspeli saying at the beginning of Chapter 3:

    We will assume that Python 2.4 gets invoked when you run python on the command line.

This book does not make that assumption and tries to cover everything you may need to know after installing your operating system up to that point.

In **Chapter 1**, we cover installing and running Python on three popular operating systems: Mac OS X 10.6 (my main squeeze), Windows 7, and Ubuntu 9.10 (Debian is my main production server squeeze). Other operating systems are welcome; your mileage may vary.

#2
--

This book is largely a response to the whole "Oh no! I have to use Buildout to install Plone and its add-ons!" sentiment that has been prevalent since Buildout was first introduced to Plone several years ago. I don't know if Buildout was the "right" way to go, but I do know that I love using it and I would like to help others feel the same way.

The bottom line is this: Plone made a conscious decision to "become more Pythonic" by using eggs. With that choice came more complexity from potential conflicts between eggs. Buildout is one solution to that problem. Unfortunately, it introduces other problems like cryptic error messages and a certain **too-many-moving-parts**-ness.

An aside…
---------

Let me correct myself: I am fairly certain Buildout was the right way to go at the time. What I am not sure about is where to go from here. It would be nice to get back to a place where folks could just drop packages in to a directory (I don't literally mean going back to old-style products, but perhaps we could provide that type of functionality again somehow). But I don't have an answer for that. In the meantime, let's make everyone more comfortable with using Buildout.

About the rest of the book…
---------------------------

The book teaches you to find your way around Buildout and Plone. Whether you choose to follow along and build your site from scratch using only Buildout (and a paper clip) or if you use one of the Buildout-based installers (like the Unified Installer), this book aims to make you more competent and comfortable performing a variety of Buildout-related tasks.

In **Chapters 2-7**, we present various buildout configuration files that correspond to specific tasks that are related to various subjects, e.g. theming, maintenance, and optimization. The reader is expected to "know how to write a buildout.cfg file" by the end. No one that reads the book is allowed in the #plone IRC channel afterward to ask about buildout (you can answer buildout questions though). Kidding… I kid…

In the final **Chapter 8**, we cover new technologies like XDV and repoze.zope2 which may become more mainstream once you decide to start using them (although the latter seems more like a toy to keep us busy until the real fix arrives: `full WSGI support in Zope 2`_).

When will it arrive?
--------------------

PACKT originally announced the book will arrive in March and I have been working non-stop since mid-March to make sure it gets out the door as quickly as possible; I expect it to be available **Real Soon Now™**. I apologize to those of you who have pre-ordered and are now waiting for it!

So get ready! I plan to have over 200 pages of draft material submitted by the end of this month. I will continue to work with PACKT to address any concerns that arise during editing. They have promised to try to ship the book by May, so we will see how it goes. I encourage you to `pre-order now`_ as that will go a long way to inspire them to work just that much harder to get it done and out to you, ASAP!

Can I write a book?
-------------------

Probably. For those curious about the process (as I very much was), here is a bit about how it went for me:

#. A few years ago, Martin Aspeli had the idea for Practical Plone 3 and put out a call to writers that I responded to; I ended up contributing 2 chapters. This taught me that it was indeed a lot of work, and I got exposed to the editing process.
#. A couple years ago, PACKT approached me (and several others) about the idea for Plone Site Administration and I thought I had a good story to tell based on my experiences, so I wrote a detailed outline and they accepted it.
#. Though I had written for Practical Plone 3, I struggled to find my voice. At the same time I had a tremendous amount of consulting work to do to make a living. I sneaked in time to write drafts and eventually found my voice. To be honest, the most productive work has been done in the last 3 months.

Perhaps the biggest lesson I learned was this: stop thinking and start writing. I tend to over analyze things and spent a lot of time thinking about "how it would go" rather than just writing it. Writing is the key.  Think less, write more (at which point your thoughts tends to flow more naturally anyway).

Should I write a book?
----------------------

Possibly. I am sensitive to the phenomenon of "Plone book diarrhea" and I do think that there can be such a thing as too many Plone books. But I don't think we are there yet. To me, the more books published about Plone (by PACKT or any publisher) the better. I like to see what each individual author brings to the story, even if the stories they are telling tend to overlap sometimes. So for me the answer to that question both before and after writing my book is **yes**. I know I am a better writer having written it, and I certainly know more about Python, Zope, and Plone and many other technologies.

In either case, you should definitely take my class.
----------------------------------------------------

If you are interested in learning more about Python and tools like Distribute, Pip, Buildout, etc. and you want to feel more comfortable managing your Plone site, you will not want to miss the `one day class I am teaching at Plone Symposium East 2010`_!

The book will hopefully be out by then, but the class will go on either way.

Hope to see you there, and I hope you enjoy the book.

P.S. Looking for Plone experts? Hire ACLARK.NET, LLC.
-----------------------------------------------------

Thank you, everyone, for the responses to `my previous blog entry`_. I have had some great conversations with some very interesting folks and I appreciate everyone's interest. However, I wanted to encourage everyone once more to `get in touch.`_ And also, to feel free to reach whenever you come across this blog entry and are in need of Plone help. We are always looking for a challenge.

.. _Plone Conference 2006: http://plone.org/events/conferences/seattle-2006
.. _Plone Conference 2008: http://plone.org/2008
.. _Professional Plone Development: https://www.packtpub.com/Professional-Plone-web-applications-CMS/book
.. _Plone 3.3 Site Administration: https://www.packtpub.com/plone-3-3-site-administration/book
.. _MacGyver: http://en.wikipedia.org/wiki/MacGyver
.. _full WSGI support in Zope 2: http://article.gmane.org/gmane.comp.web.zope.plone.devel/23887
.. _pre-order now: https://www.packtpub.com/plone-3-3-site-administration/book
.. _one day class I am teaching at Plone Symposium East 2010: http://plone-site-admin.eventbrite.com
.. _my previous blog entry: http://blog.aclark.net/?p=170
.. _get in touch.: mailto:aclark@aclark.net?subject="Hire%20Alex%20Clark"
.. _contact: http://aclark.net/contact-info
