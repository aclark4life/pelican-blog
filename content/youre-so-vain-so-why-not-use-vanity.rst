You&#039;re so vain, so why not use Vanity?
###########################################
:date: 2011-06-16 12:01
:tags: Plone, Python
:category: Python

A few months ago I created a package called **Vanity**\ [0] that
provides easy access to package download statistics from **PyPI**. You
can find the source code here: `https://github.com/aclark4life/vanity`_.

I love this tool, and I use it all the time to gauge the value of a
package. Of course, downloads are only one criteria you can use to judge
the value of a package, and arguably not even a very good one.
**Vanity** itself is a good example of this phenomenon. I find it
incredibly useful, but in it's history it has only been downloaded *130*
times.

Other packages I have created with much less value have been downloaded
more times, e.g. **plonetheme.aclark\_twitter** which has been
downloaded  *674* times. But that package has also been around much
longer. So obviously another useful metric would be the *time period*
during which the downloads occurred.

.. raw:: html

   <p>

Anyway, here is how it works:

::

    $ easy_install vanity

Then:

::

    $ vanity <package>

For example:

::

    $ vanity vanity
    Package `vanity` has been downloaded 130 times!

Or:

::

    $ vanity plonetheme.aclark_twitter
    Package `plonetheme.aclark_twitter` has been downloaded 674 times!

Some of my other favorites:

::

    $ vanity Django[1]
    Package `Django` has been downloaded 302111 times!

::

    $ vanity zope.component
    Package `zope.component` has been downloaded 210541 times!

::

    $ vanity pyramid
    Package `pyramid` has been downloaded 26067 times!

Another thing to consider is if hitting **PyPI** each time is really
necessary. I'm told there is **PyPI** data living somewhere else, and in
future versions I would like to make vanity use that data by default.

.. raw:: html

   </p>

So, this post is simply to announce **Vanity** to a wider audience in
the event that some folks may find it useful. Otherwise, I will be happy
to continue to watch **Vanity** downloads crawl ever so slowly towards
200. :-)

Notes
=====

[0] By standing on the shoulders of some Plone giants, `David Glick,`_
in particular.

.. raw:: html

   </p>

[1] There is a `known issue`_ with regard to making Vanity case
insensitive.

 

 

 

.. _`https://github.com/aclark4life/vanity`: https://github.com/aclark4life/vanity
.. _David Glick,: http://davisagli.com/
.. _known issue: https://github.com/aclark4life/vanity/issues/1
