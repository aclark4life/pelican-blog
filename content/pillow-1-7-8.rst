Pillow 1-7-8
============

:date: 2012-11-02 11:00
:tags: Python

*Pillow is the "friendly" PIL fork. Initially just a packaging fork, now considering image code bug fixes and Python 3 support. To be friendly, we attempt to track changes against upstream tickets in PIL.*

Pillow 1.7.8 is out! Read about it here:

- http://pypi.python.org/pypi/Pillow/1.7.8

Features
--------

- It's PIL (Python Imaging Library)
- It installs on all modern systems [1]_
- Win32 eggs are provided (special thanks to Takayuki Shimizukawa)

Changes
-------

This release includes:

- Removed doctests.py that made tests of other packages fail. [thomasdesvenain]
- Fix opening psd files with RGBA layers when A mode is not of type 65535 but 3. Fixes issue https://github.com/python-imaging/Pillow/issues/3 [thomasdesvenain]

Install
-------

To install Pillow::

    $ easy_install Pillow

Or::

    $ pip install Pillow

Or::

    $ python setup.py install (inside the extracted zip)

Or::

    $ pip install zc.buildout
    $ buildout init

With ``buildout.cfg``::

    [buildout]
    parts = pillow

    [pillow]
    recipe = zc.recipe.egg

And::

    $ buildout

(Note: easy_install & pip each handle namespace packages differently, so you should choose one or the other, and not mix the two.) 

Report issues
-------------

If you find an issue, please report it here:

- https://github.com/python-imaging/Pillow/issues

Better yet: please fork, fix, and submit a pull request. Please also solicit for peer review once the pull request has been submitted.

Discussion
----------

You may discuss issues related to PIL, Pillow, and Python imaging on the image-sig list:

- http://mail.python.org/mailman/listinfo/image-sig

Enjoy using Pillow!

.. [1] If it doesn't, please report it: https://github.com/python-imaging/Pillow/issues
