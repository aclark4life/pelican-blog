Review of Veda Williams&#039; Plone 3 Theming
#############################################
:date: 2009-09-22 16:17
:tags: Plone

First things first, I can't overstate enough how much I personally appreciate Veda's efforts to bring the (currently-and-unfortunately, but-not-for-long) complex world of Plone theming to the masses. It's an acquired taste, but once you get the hang of it you can use your powerful skills to create some very impressive sites – and make the world a better place like Veda and the crew at `Groundwire`_ are doing (formerly ONE/Northwest).

Furthermore, If you are interested in Plone and how Plone theming works, this book is almost certainly for you. It gives you an over abundance of present day theming knowledge, and also covers aspects of the Zope 3 component architecture, where Plone has been, and where it is going to be in the not-so-distant-future.

Since `PACKT`_ are well known for giving back to the communities that produce the software that is the subject of their books, purchasing a copy of this book will directly benefit Plone, so I encourage you to do so.

With all that out of the way, I'd like to focus on a chapter by chapter review (`like`_ `everyone`_ `else`_ `does`_) of Plone 3 Theming. Like I said, I really liked this book so please don't take any of my (hopefully constructive) criticism negatively. I hope my comments will help the readers of this book, as well as Veda, if she dares to attempt a 2nd edition one day!

**STANDARD DISCLAIMERS APPLY**: I'm a "paid" reviewer (in that I received a free copy of the book) and also, I know Veda personally.

Chapter 1
---------

This chapter gives an overview of Plone, which as a total-Plone-fanboy, I very much appreciated. I particularly enjoyed the "community lore".  "what is Plone", and "books about Plone" sections. The author also includes a "Plone vs. Drupal" comparison and an "evolution" section that covers Plone theming-framework changes version by version, which I didn't care for as much [1].

Chapter 2
---------

This chapter lists many tools for graphic design, web browsing, web development (with browser add-ons), and text editing. All useful information. I particularly enjoyed the recommendation for the browser add-on `YSlow`_ which I'd heard of, but don't use regularly.  Recommendations for the traditional UNIX® text editors vi and emacs were missing, but folks that use these editor already know which one they prefer (\*wink\* – vi), and those that don't aren't likely to start using them now.

Chapter 3
---------

Here we get into the now-venerable `zc.buildout`_ and how it is used by Plone. I think many folks will appreciate the terminology section, featuring definitions of Zope, Python, and various Python package terminology. I would have liked to have seen the `PyPI features of plone.org mentioned`_, but I'll settle for a shameless plug of it here.  Similarly, no mention of git or mercurial in a section about version control (Subversion only), but I suppose (again) those familiar with these technologies already know which one they prefer.

Lastly, I liked the variety of approaches described in the "download Plone" section, from using platform installers to using the unified installer to satisfying all the Plone dependencies by hand. All good information.

Chapter 4
---------

Using `ZopeSkel`_ to create a theme package, then adding that package to your buildout as a "develop egg" are the main topics covered here. (A side note: I'm very much looking forward to the upcoming release of ZopeSkel 2.14!  `http://www.coactivate.org/projects/zopeskel-bbq-sprint/blog/2009/10/13/zopeskel-bbq-sprint-days-two-three-and-four/`_ )

Chapter 5
---------

I like this chapter because it covers a variety of the TTW (through the web) changes that we are consistently reminded we are not supposed to make, but we all know that everyone makes them. The truth is, there is absolutely nothing wrong with TTW changes if you take them for what they are worth. It's fine to turn a knob or two TTW, just be aware that at some point you may be turning that knob again TTW, if you don't turn a similar knob on the file system ;-)

Chapter 6-7
-----------

Here we get into various Zope 3 concepts: ZCML, browser layers, resources, viewlets and more! If there is such a thing, this would be the "unfortunate" part of the modern Plone theming story. Plone themers, for better or worse, must be familiar these concepts in order to be successful. One pet peave I have, that I will mention here because it seems appropriate, is the bundling of GenericSetup in a discussion about Zope 3 concepts. While GenericSetup may use Zope 3 technology under the hood (I assume it does, like most modern Zope 2 code) as a concept it has absolutely nothing to do with Zope 3 (in other words it is not part of the "component architecture") It just happened to be introduced to Plone around the same time various other Zope 3 technology was introduced (via Five), hence people tend to include it in the "things they hate about Zope 3 in Plone" category. Perhaps GenericSetup should have been added either before or after the Zope 3 stuff to make it more palatable, but that train has sailed and now we must deal with the consequences.

Chapter 8
---------

This chapter about TAL (template attribute language) is great stuff. TAL is one of those beautiful technologies that pays for itself once you learn it (unlike various web form frameworks, for example ;-). If like me you can't get enough of TAL from Veda's book, check out the section on it in the Zope 2 book: `http://docs.zope.org/zope2/zope2book/ZPT.html`_

Chapter 9-11
------------

Here we get to watch Veda design, build, and deploy a theme. This is the focal point of the book, and is worth the price of admission alone. I almost wish the entire book was about this theme, with the other relevant bits sprinkled in as needed. But in any event, these three chapters are what most readers will be most interested in.

Chapter 12
----------

This is a great little chapter about various add-ons that themers may find interesting. My favorite add-on mentioned in this chapter is Products.FSDump. Very, very useful tool for getting various bits out of your ZODB and on to your file system (e.g. the contents of the portal\_skins/custom folder). I'm really hoping that a 1.0 release will see the light of day one of these days. I notice Veda didn't mention it, but there is now an egg-based version of this popular add-on: `http://pypi.python.org/pypi/Products.FSDump/FSDump-0.9.4`_ Just add Products.FSDump to your instance section's eggs= parameter and off you go.

Chapter 13
----------

Here, a gratuitous chapter on multimedia wherein various useful multi-media add-ons are mentioned. I say gratuitous because I think there is a misperception that you need these add-ons to accomplish what you want. Plone should do a much better job convincing people that while it is a complex application, a Plone site is also just a website. So if you know how to do it elsewhere (e.g. on a "regular" website) it should be easy to do it in Plone (we are not quite there yet). Anyway, some great add-ons are mentioned here of course, but one noticeable absence: `http://plone.org/products/collective-fancyzoomview`_ (which is used by PloneSoftwareCenter on plone.org).

Chapter 14
----------

An 'Amen!' for this chapter that covers deploying and contributing themes, especially on the contributing part. As I mentioned earlier, I would have liked to have seen the `PyPI features of plone.org mentioned`_ in this book, and in this chapter in particular. While it is arguably still hard to create Plone themes, it is encouragingly not hard to share them! Also, an incredibly useful tool for releasing themes (and any package) to both plone.org/products and pypi.python.org at the same time (i.e in a single command) is `http://pypi.python.org/pypi/jarn.mkrelease/2.0.2.`_

Chapter 15
----------

This chapter (by Alexander Limi) introduces people to "new style" theming with xdv. While I enjoy this subject tremendously, I think it's going to take a while before it is fully digested by integrators.  Hopefully, Alex's chapter will help. I'm also told that Laurence Rowe has been making some improvements to collective.xdv recently, and I see there is a new version here: `http://pypi.python.org/pypi/collective.xdv`_ (I think this version handles 404s).

Bottom line: this is great stuff but potentially confusing in that you have an add-on, collective.xdv, that applies an XSLT transform "on the fly" (in memory) to your Plone site, but the recommended deployment strategy is to use NGINX or Apache with Laurence's patches applied. I've spent some time doing this (I expect to re-launch this site with xdv soon, and of course plone.org uses it) and it is non-trivial to say the least. What we have now is a situation where folks are starting to use collective.xdv and thinking that \*it\* is the new way to theme, when in fact it is only part of the story.

One last pet peeve I will mention is that both "theming" and "skinning" were used to describe the subject of the book.  I would have preferred just "theming" (since that is what we are calling it now ;-).

In conclusion, great job Veda! Thank you very much for your efforts. I look forward to reviewing a second edition. To every one else, I invite you to purchase your copy of this book and get your Plone 3 theming ON: `http://www.packtpub.com/plone-3-theming-create-flexible-powerful-professional-templates`_

[1] Quite frankly, I think Plone is in a category all its own (as the most successful Python-based CMS of all time), and while there are certainly comparisons to be made, and lessons to be learned from the competition, I think we should let the readers decide for themselves how Plone stacks up to the competition.

.. _Groundwire: http://groundwire.org
.. _PACKT: http://packtpub.com
.. _like: http://vincentfretin.ecreall.com/articles/review-plone-3-theming
.. _everyone: http://seeknuance.com/2009/08/25/a-review-of-plone-3-theming/
.. _else: http://www.littled.net/new/2009/09/27/review-of-plone-3-theming-by-veda-williams/
.. _does: http://reinout.vanrees.org/weblog/2009/10/25/plone-3-theming.html
.. _YSlow: http://developer.yahoo.com/yslow/
.. _zc.buildout: http://pypi.python.org/pypi/zc.buildout/1.4.1
.. _PyPI features of plone.org mentioned: is-anyone-using-plone.orgs-new-pypi-functionality
.. _ZopeSkel: http://pypi.python.org/pypi/ZopeSkel/2.13
.. _`http://www.coactivate.org/projects/zopeskel-bbq-sprint/blog/2009/10/13/zopeskel-bbq-sprint-days-two-three-and-four/`: http://www.coactivate.org/projects/zopeskel-bbq-sprint/blog/2009/10/13/zopeskel-bbq-sprint-days-two-three-and-four/
.. _`http://docs.zope.org/zope2/zope2book/ZPT.html`: http://docs.zope.org/zope2/zope2book/ZPT.html
.. _`http://pypi.python.org/pypi/Products.FSDump/FSDump-0.9.4`: http://pypi.python.org/pypi/Products.FSDump/FSDump-0.9.4
.. _`http://plone.org/products/collective-fancyzoomview`: http://plone.org/products/collective-fancyzoomview
.. _`http://pypi.python.org/pypi/jarn.mkrelease/2.0.2.`: http://pypi.python.org/pypi/jarn.mkrelease/2.0.2
.. _`http://pypi.python.org/pypi/collective.xdv`: http://pypi.python.org/pypi/collective.xdv
.. _`http://www.packtpub.com/plone-3-theming-create-flexible-powerful-professional-templates`: http://www.packtpub.com/plone-3-theming-create-flexible-powerful-professional-templates/mid/220709943ki3?utm_source=aclark.net&utm_medium=affiliate&utm_content=blog&utm_campaign=mdb_001376
