Pillow 2.2.1 Released
=====================

:date: 2013-10-03 08:00
:tags: Django, Python, Plone

*Pillow is the "friendly" PIL fork. PIL is the Python Imaging Library.*

.. Note:: An earlier version of this entry was published yesterday with the wrong date. Apologies for any annoyance or confusion.

The Pillow 2.2.1 source distribution is `now available on PyPI <https://pypi.python.org/pypi/Pillow/2.2.1>`_, featuring over 30 documented bug fixes and enhancements since 2.1.0 was released 3 months ago.

Changelog
---------

- Fix `#254 <https://github.com/python-imaging/Pillow/issues/254>`_: Bug in image transformations resulting from uninitialized memory [nikmolnar]
- Fix for encoding of b_whitespace, similar to closed issue `#272 <https://github.com/python-imaging/Pillow/issues/272>`_ [mhogg]
- Fix `#273 <https://github.com/python-imaging/Pillow/issues/273>`_: Add numpy array interface support for 16 and 32 bit integer modes [cgohlke]
- Partial fix for `#290 <https://github.com/python-imaging/Pillow/issues/290>`_: Add preliminary support for TIFF tags. [wiredfool]
- Fix `#251 <https://github.com/python-imaging/Pillow/issues/251>`_ and `#326 <https://github.com/python-imaging/Pillow/issues/326>`_: circumvent classification of pngtest_bad.png as malware [cgohlke]
- Add typedef uint64_t for MSVC. [cgohlke]
- Fix `#329 <https://github.com/python-imaging/Pillow/issues/329>`_: setup.py: better support for C_INCLUDE_PATH, LD_RUN_PATH, etc. [nu774]
- Fix `#328 <https://github.com/python-imaging/Pillow/issues/328>`_: _imagingcms.c: include windef.h to fix build issue on MSVC [nu774]
- Automatically discover homebrew include/ and lib/ paths on OSX [donspaulding]
- Fix bytes which should be bytearray [manisandro]
- Add respective paths for C_INCLUDE_PATH, LD_RUN_PATH (rpath) to build if specified as environment variables. [seanupton]
- Fix `#312 <https://github.com/python-imaging/Pillow/issues/312>`_ + gif optimize improvement [d-schmidt]
- Be more tolerant of tag read failures [ericbuehl]
- Fix `#318 <https://github.com/python-imaging/Pillow/issues/318>`_: Catch truncated zTXt errors. [vytisb]
- Fix IOError when saving progressive JPEGs. [e98cuenc]
- Add RGBA support to ImageColor [yoavweiss]
- Fix `#304 <https://github.com/python-imaging/Pillow/issues/304>`_: test for str, not "utf-8". [mjpieters]
- Fix missing import os in _util.py. [mnowotka]
- Added missing exif tags. [freyes]
- Fail on all import errors, fixes `#298 <https://github.com/python-imaging/Pillow/issues/298>`_. [macfreek, wiredfool]
- Fixed Windows fallback (wasn't using correct file in Windows fonts). [lmollea]
- Moved ImageFile and ImageFileIO comments to docstrings. [freyes]
- Restore compatibility with ISO C. [cgohlke]
- Use correct format character for C int type. [cgohlke]
- Allocate enough memory to hold pointers in encode.c. [cgohlke]
- Fix `#279 <https://github.com/python-imaging/Pillow/issues/279>`_, fillorder double shuffling bug when FillOrder ==2 and decoding using libtiff. [wiredfool]
- Moved Image module comments to docstrings. [freyes]
- Add 16-bit TIFF support, fixes `#274 <https://github.com/python-imaging/Pillow/issues/274>`_. [wiredfool]
- Ignore high ascii characters in string.whitespace, fixes `#272 <https://github.com/python-imaging/Pillow/issues/272>`_. [wiredfool]
- Added clean/build to tox to make it behave like travis. [freyes]
- Adding support for metadata in webp images. [heynemann]

Distributions
-------------

In addition to the `source distribution <https://pypi.python.org/pypi?name=Pillow&version=2.2.1&:action=files>`_, there are also Python Eggs and Windows Installers available (for 32 and 64 bit) and for the first time ever: Python Wheels! (New built-package format supported by pip.)


Support
-------

`The Pillow Team <https://github.com/python-imaging?tab=members>`_ has really settled in to the groove of making Pillow releases every three months, and I am very proud to be a part it! Special thanks to Eric Soroos and Christopher Gohlke for their invaluable help with Pillow 2.2.1.

If you use Pillow professionally, please consider `supporting its development <https://github.com/python-imaging/Pillow#financial>`_.
