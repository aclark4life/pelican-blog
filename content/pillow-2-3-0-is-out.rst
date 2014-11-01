Pillow 2-3-0 is out!
====================

:date: 2014-01-01 18:30
:tags: Django, Mozilla, Plone, Python

**Pillow is the "friendly" PIL fork by Alex Clark and Contributors. PIL is the Python Imaging Library by Fredrik Lundh and Contributors**

Since Pillow 2.0, the Pillow Team has adopted a quarterly release cycle; as such, Pillow 2.3.0 has just been released. Here's what's new in this release:

.. image:: /images/one-does-not-simply-make-a-release.jpg
    :alt: alternate text

2.3.0 (2014-01-01)
------------------

- Stop leaking filename parameter passed to getfont
  [jpharvey]

- Report availability of LIBTIFF during setup and selftest
  [cgohlke]

- Fix msvc build error C1189: "No Target Architecture"
  [cgohlke]

- Fix memory leak in font_getsize
  [wiredfool]

- Correctly prioritize include and library paths
  [ohanar]

- Image.point fixes for numpy.array and docs
  [wiredfool]

- Save the transparency header by default for PNGs
  [wiredfool]

- Support for PNG tRNS header when converting from RGB->RGBA
  [wiredfool]

- PyQT5 Support
  [wiredfool]

- Updates for saving color tiffs w/compression using libtiff
  [wiredfool]

- 2gigapix image fixes and redux
  [wiredfool]

- Save arbitrary tags in Tiff image files
  [wiredfool]

- Quote filenames and title before using on command line
  [tmccombs]

- Fixed Viewer.show to return properly
  [tmccombs]

- Documentation fixes
  [wiredfool]

- Fixed memory leak saving images as webp when webpmux is available
  [cezarsa]

- Fix compiling with FreeType 2.5.1
  [stromnov]

- Adds directories for NetBSD.
  [deepy]

- Support RGBA TIFF with missing ExtraSamples tag
  [cgohlke]

- Lossless WEBP Support
  [wiredfool]

- Take compression as an option in the save call for tiffs
  [wiredfool]

- Add support for saving lossless WebP. Just pass 'lossless=True' to save()
  [liftoff]

- LCMS support upgraded from version 1 to version 2, fixes #343
  [wiredfool]

- Added more raw decoder 16 bit pixel formats
  [svanheulen]

- Document remaining Image* modules listed in PIL handbook
  [irksep]

- Document ImageEnhance, ImageFile, ImageFilter, ImageFont, ImageGrab, ImageMath, and ImageOps
  [irksep]

- Port and update docs for Image, ImageChops, ImageColor, and ImageDraw
  [irksep]

- Move or copy content from README.rst to docs/
  [irksep]

- Respect CFLAGS/LDFLAGS when searching for headers/libs
  [iElectric]

- Port PIL Handbook tutorial and appendices
  [irksep]

- Alpha Premultiplication support for transform and resize
  [wiredfool]

- Fixes to make Pypy 2.1.0 work on Ubuntu 12.04/64
  [wiredfool]

Thanks to everyone who contributed fixes to 2.3.0, especially Eric Soroos AKA "wiredfool" who is officially now "Pillow Man #2" [1]_.

Handbook
--------

Additionally, we've forked the PIL handbook and have included it with our documentation here: http://pillow.readthedocs.org. Special thanks to Stephen Johnson AKA "irksep" for working on this.

Distributions
-------------

Lastly, I'm very grateful to Christopher Gohlke for producing Windows Egg, Exe, and Wheel distributions to accompany each source release. I suspect Christopher will produce his 2.3.0 distributions any second now at which point I will upload them to PyPI via `twine <https://pypi.python.org/pypi/twine>`_.

Enjoy Pillow 2.3.0! And please report any issues you find here: https://github.com/python-imaging/Pillow/issues

.. [1] In case I'm hit by a bus, Eric Soroos has the keys. 
