Pillow 3-0-0 is out
===================

:date: Sat Oct  3 21:51:26 EDT 2015
:tags: Plone, Python

The `Pillow Team <https://github.com/python-pillow/Pillow/graphs/contributors>`_  is excited to announce the release of Pillow 3.0.0. While "3 is just a number after 2", there are some **significant changes in this release all users should be aware of**: 

- `LibJpeg and Zlib are Required by Default <http://pillow.readthedocs.org/en/3.0.x/releasenotes/3.0.0.html#libjpeg-and-zlib-are-required-by-default>`_

- `Deprecated Methods <http://pillow.readthedocs.org/en/3.0.x/releasenotes/3.0.0.html#deprecated-methods>`_

I'm particularly happy to see libjpeg & zlib required; this will avoid many-a-broken-installation in the future. **PIL is of little practical value when installed without JPEG support**, yet this has been the default for over 20 years. No more! Thanks to wiredfool for `spearheading this change <https://github.com/python-pillow/Pillow/issues/1412>`_.

For more goodness, please see the release notes & changelog:

- http://pillow.readthedocs.org/en/3.0.x/releasenotes/3.0.0.html
- https://github.com/python-pillow/Pillow/blob/3.0.x/CHANGES.rst#300-2015-10-01

Lastly, we're approaching 10 million downloads:

::

    $ vanity -q pillow
    Pillow has been downloaded 9,906,841 times!

An exciting milestone! 

Thanks to all the developers & users of PIL & Pillow. Enjoy the 3.0.0 release, and as always `report'em if you got'em and we'll fix'em <https://github.com/python-pillow/Pillow/issues>`_.

.. raw:: html

    <a href="https://gratipay.com/aclark4life/">
      <img alt="Support via Gratipay" src="https://cdn.rawgit.com/gratipay/gratipay-badge/2.3.0/dist/gratipay.png"/>
    </a>
