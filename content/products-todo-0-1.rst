Products.todo 0.1
================================================================================

:date: 2008-11-13 08:07
:tags: Plone

I needed a project to jump start my return to Plone after spending months organizing `Plone Conference 2008`_, and I had the idea that I wanted to, very quickly, see a product's development cycle through from start to finish, including:

#. Generating boilerplate buildout and product code with paster.
#. Develop some simple functionality for Plone.
#. Releasing to pypi.

Repeat steps 2 and 3 as needed or desired. That product is Products.todo (`http://pypi.python.org/pypi/Products.todo/`_)

I also wanted to:

-  Include the buildout in the product so I could easily add buildbot (a la Tarek).
-  Write some tests for this code so I could practice TDD.
-  Release this product to new.plone.org, so we can finish the plone.org upgrade.

I'm off to a good start I think as, while it took me a couple days (more than I expected), the product is now on pypi. (Thanks to irc://irc.freenode.net#plone and the product-developers list for the help!)

Next steps:

-  Get some feedback on the code. While this is a simple product, it was not as simple as I would have hoped to implement, and there are more features I would like to add.
-  Edit my .pypirc and add new.plone.org and test a release.
-  Add buildbot.
-  Write some tests. I need some help here. How do you test a simple product like this? I understand that if you test the ability to add an item to a folder you are testing the framework not the product. So maybe I need to focus on testing just the features I add...
-  Enjoy doing this in the future when plone.org supports pypi ;-)

**Update (11/15/2008):**

-  New screenshot
-  0.2 version on PyPI
-  Thanks for the comments everyone!

.. _Plone Conference 2008: http://plone.org/2008
.. _`http://pypi.python.org/pypi/Products.todo/`: http://pypi.python.org/pypi/Products.todo/
