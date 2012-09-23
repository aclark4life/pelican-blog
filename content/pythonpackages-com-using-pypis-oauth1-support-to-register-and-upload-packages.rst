pythonpackages.com: Using PyPI&#039;s OAuth1 support to register and upload packages
####################################################################################
:date: 2012-08-07 05:16
:tags: Plone, Python

***TL;DR** PyPI has OAuth1 support; pythonpackages.com uses it to send
your GitHub repos to PyPI.* Thanks in very large part to `Richard
Jones`_, the Python Package Index now has support for registering and
uploading packages via OAuth1. And using his `sample code`_ I was able
to take advantage of it on pythonpackages.com. The result is a fairly
**elegant approach to releasing packages** sans dirty hacks (I had been
asking users for their username and password, then storing them in an
encrypted session cookies so I could send them to PyPI.) Here's how it
works now.

Sign In With GitHub
===================

GitHub provides an easy way to let folks sign in to pythonpackages.com
with their APIv3. I was able to code the OAuth dance using only the
requests library (HT Kenneth Reitz). This was working as of late 2011.
`|image0|`_ `|image1|`_

Select a package
================

Once you are signed in, you can select a package. Selected packages can
perform various actions, one of which is **Tag and Release**.
`|image2|`_ As soon as you select Tag and Release, you are required to
authenticate with PyPI.

[STRIKEOUT:Enter your PyPI credentials]
=======================================

In order to get the beta out the door, a dirty hack was added to allow
users to enter their PyPI credentials. Credentials were saved in an
encrypted session cookie, then written out to .pypirc before calling
\`python setup.py upload\`. Really terrible. This was shipped in early
July 2012 and is thankfully no longer necessary (though it is `still
necessary to push the initial commit to GitHub.`_)

Authorize pythonpackages.com
============================

Now authorization can happen elegantly via OAuth1. First, sign in to
PyPI. Then authorize pythonpackages.com to act on your behalf. Lastly,
profit (register and upload your package). `|image3|`_ `|image4|`_
`|image5|`_

Register and upload your package
================================

At this point you are free to tag and release. `|image6|`_ `|image7|`_  
I am really excited about this. I began fantasizing about it almost a
year ago and after several false starts (pypissh, openid, avoidance) it
is now a reality. If you have a minute, please `give it a try`_.

.. _Richard Jones: https://twitter.com/r1chardj0n3s
.. _sample code: https://gist.github.com/0d46c48b230e61e18479
.. _|image8|: http://aclark4life.files.wordpress.com/2012/08/screen-shot-2012-08-07-at-12-26-20-am.png
.. _|image9|: http://aclark4life.files.wordpress.com/2012/08/screen-shot-2012-08-07-at-12-21-20-am.png
.. _|image10|: http://aclark4life.files.wordpress.com/2012/08/azqtp6icuaile2p_large.png
.. _still necessary to push the initial commit to GitHub.: http://docs.pythonpackages.com/en/latest/security.html#github-credentials
.. _|image11|: http://aclark4life.files.wordpress.com/2012/08/screen-shot-2012-08-07-at-12-48-04-am.png
.. _|image12|: http://aclark4life.files.wordpress.com/2012/08/screen-shot-2012-08-07-at-12-51-18-am.png
.. _|image13|: http://aclark4life.files.wordpress.com/2012/08/screen-shot-2012-08-07-at-12-51-51-am.png
.. _|image14|: http://aclark4life.files.wordpress.com/2012/08/azqtp6icuaile2p_large1.png
.. _|image15|: http://aclark4life.files.wordpress.com/2012/08/screen-shot-2012-08-07-at-12-57-13-am.png
.. _give it a try: https://pythonpackages.com/signup

.. |image0| image:: http://aclark4life.files.wordpress.com/2012/08/screen-shot-2012-08-07-at-12-26-20-am.png?w=300
.. |image1| image:: http://aclark4life.files.wordpress.com/2012/08/screen-shot-2012-08-07-at-12-21-20-am.png?w=300
.. |image2| image:: http://aclark4life.files.wordpress.com/2012/08/azqtp6icuaile2p_large.png?w=300
.. |image3| image:: http://aclark4life.files.wordpress.com/2012/08/screen-shot-2012-08-07-at-12-48-04-am.png?w=300
.. |image4| image:: http://aclark4life.files.wordpress.com/2012/08/screen-shot-2012-08-07-at-12-51-18-am.png?w=300
.. |image5| image:: http://aclark4life.files.wordpress.com/2012/08/screen-shot-2012-08-07-at-12-51-51-am.png?w=300
.. |image6| image:: http://aclark4life.files.wordpress.com/2012/08/azqtp6icuaile2p_large1.png?w=300
.. |image7| image:: http://aclark4life.files.wordpress.com/2012/08/screen-shot-2012-08-07-at-12-57-13-am.png?w=300
.. |image8| image:: http://aclark4life.files.wordpress.com/2012/08/screen-shot-2012-08-07-at-12-26-20-am.png?w=300
.. |image9| image:: http://aclark4life.files.wordpress.com/2012/08/screen-shot-2012-08-07-at-12-21-20-am.png?w=300
.. |image10| image:: http://aclark4life.files.wordpress.com/2012/08/azqtp6icuaile2p_large.png?w=300
.. |image11| image:: http://aclark4life.files.wordpress.com/2012/08/screen-shot-2012-08-07-at-12-48-04-am.png?w=300
.. |image12| image:: http://aclark4life.files.wordpress.com/2012/08/screen-shot-2012-08-07-at-12-51-18-am.png?w=300
.. |image13| image:: http://aclark4life.files.wordpress.com/2012/08/screen-shot-2012-08-07-at-12-51-51-am.png?w=300
.. |image14| image:: http://aclark4life.files.wordpress.com/2012/08/azqtp6icuaile2p_large1.png?w=300
.. |image15| image:: http://aclark4life.files.wordpress.com/2012/08/screen-shot-2012-08-07-at-12-57-13-am.png?w=300
