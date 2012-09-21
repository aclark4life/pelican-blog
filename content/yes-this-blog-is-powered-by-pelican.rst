Yes, this blog is now powered by Pelican
########################################
:date: 2012-11-21 09:30
:tags: Mozilla, Plone, Python

As an open source "Plone guy", I'm always prepared to defend and explain my choice to **not** use Plone for blogging. A couple years ago, I started using Wordpress in order to learn its feature set. I enjoyed my time with it, but after moving to wordpress.com for "trouble free" hosting, I found I couldn't control my category feeds the way I wanted; the honeymoon was over.

This was a giant let down, because I was hoping to avoid putting any time in to my blogging infrastructure. For weeks I did nothing. I poked at various options: Pelican, Plone, Tumblr, others. Eventually, I found my way back to Pelican and now I'm happy again.

.. image:: http://blog.aclark.net/images/pelican.png

Pelican is a static blog generator, as you may have heard. So **one big advantage** is:

- You can host it for free, or close to free on any number of free or cheap static website hosting services! (I'm using GitHub Pages)

Other advantages
----------------

- It does feeds right (I need 3 "full body" feeds for: Mozilla, Plone, Python) [1]_.

- It's fun to configure (edit pelicanconf.py or publishconf.py).

- The "cool kids" use it: e.g. Tarek Ziadé, Kenneth Reitz, Daniel Greenfeld, many others.

- It grows with you: this is huge. You can start using it and feel comfortable right away, but there is always more to learn. This is how all software should be. Unfortunately, it's tough to get it right (I think this is formally called UX).

Some disadvantages
------------------

- Don't like typing in the terminal? Pelican is not for you.

- No "nested" entries e.g. 2012/09/21/entry.html. I don't know if there is a formal name for this feature, but I miss it (if for no other reason than "cool URLS never change" i.e. I've broken links with this move.)

- The pelican-import has some bugs, so I'm doing a lot of manual cleanup (I don't mind this though.)

- Tags are categories and categories are tags (or something). I had to convert all my categories to tags, and then turn on tag feeds and turn off category feeds. Category feeds are on by default and tag feeds are off by default. Also ATOM is on and RSS is off, if that is of interest to you. (Since this is really just configuration change and not a disadvantage per sé, it probably belongs more in the next section where I discuss my setup.)

If you are curious about my setup, here are the details.

Setup
-----

Getting started with Pelican was easy, basically::

    $ virtualenv .
    $ bin/pip install pelican BeautifulSoup Markdown 
    $ bin/pelican-quickstart

At this point, after I answer the quickstart questions I::

    $ source bin/activate
    $ make html

Now the content is ready to host (which for me just involves a git push).

Tweaks
------

A few things were tricky. 

- I wanted to host my articles at the top level of the repo for serving on GitHub Pages, so I modified the Makefile to make it so [2]_. 

- Categories control what links are available in the header, so I disabled them all but one called "Blog". Not ideal, but it works.

- The "social" links, and my disqus and analytics API keys were all a pleasure to configure.

Workflow
--------

Now I write articles in restructured text and publish like so::

    $ make publish; git commit -a -m "Publish"; git push

All the details are here if you'd like to take a look:

- https://github.com/ACLARKNET/aclarknet.github.com/commits/master

Comments from more knowledgable Pelican users welcome. Like this article? Tip me on Gittip!

.. raw:: html

    <iframe style="border: 0; margin: 0; padding: 0;"
        src="https://www.gittip.com/aclark4life/widget.html"
        width="48pt" height="20pt"></iframe>

.. [1] This is actually my first "test" post with Pelican so I will get a chance to see how the feeds perform. But they looked good in testing.

.. [2] I think I broke "make html", actually. Primarily I just needed to make it not "clean" the entire repo.
