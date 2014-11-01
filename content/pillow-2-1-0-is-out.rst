Pillow 2-1-0 is out!
====================

:date: 2013-07-02
:tags: Django, Plone, Python

*Pillow is a popular fork of PIL by Alex Clark and Contributors. PIL is the Python Imaging Library by Fredrik Lundh and Contributors*

.. image:: https://raw.github.com/ACLARKNET/blog/gh-pages/images/pillow-2.1.0.png
    :alt: alternate text
    :width: 75%

`Pillow 2.1.0 is out! <https://pypi.python.org/pypi/Pillow/2.1.0>`_ With this release, the Pillow team has *finally* removed support for "import _imaging", thus completing the move of PIL modules into the PIL namespace [1]_. Many thanks to Eric Soroos (AKA wiredfool) who completed the majority of this work. Also a big thanks to Christopher Gohlke and `Arfrever <https://github.com/Arfrever>`_ both of whom rallied around a push to get the 2.1.0 release out on schedule. And I want to thank everyone else who reported an issue and/or sent a pull request to help make this release the best it could be.

Quarterly release cycle
-----------------------

After the March 15, 2013 release of Pillow 2.0.0 we decided to adopt a quarterly release cycle. So every three months, as long as the patches keep coming you will see a new Pillow release.

Look ma no official funding
---------------------------

Pillow 2.0.0 was an enormous effort, made possible by a generous grant from the Python Software Foundation. But things have stablized quite a bit since then. So much so, that with help from many others I was able to squeeze this release into my normal schedule. However you are always welcome to financially help support Pillow, especially if you are using it in a commercial environment. Committers are encouraged to add their name here if they'd like to receive donations:

- https://github.com/python-imaging/Pillow/blob/master/README.rst#support

And I have personally steered my gittip profile entirely towards Pillow production.

.. raw:: html

    <script data-gittip-username="aclark4life"
    src="https://www.gittip.com/assets/widgets/0002.js">
    </script>

Go get it now
-------------

Pillow 2.1.0 source and binaries are available on PyPI. Please use, enjoy, and `report issues <https://github.com/python-imaging/Pillow/issues?state=open>`_.

.. [1] Which began with the first release of Pillow 1.0 on 2010-07-31 in which support for "import Image" was removed.
