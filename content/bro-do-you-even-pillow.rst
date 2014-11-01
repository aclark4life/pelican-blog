Bro, do you even Pillow?
========================

:date: 2014-04-07 20:00
:tags: Django, Plone, Python

.. image:: /images/bro-do-you-even-pillow.jpg
    :alt: alternate text

`Pillow <https://github.com/python-imaging/Pillow>`_ is a fork of the Python Imaging Library. Here is an update on the status of the project.

2.4.0 released
--------------

Pillow 2.4.0 is out! Here are the highlights:

- Indexed Transparency handled for conversions between L, RGB, and P modes. Fixes #510 [wiredfool]
- Conversions enabled from RGBA->P, Fixes #544 [wiredfool]
- Improved icns support [al45tair]
- Fix libtiff leaking open files, fixes #580 [wiredfool]
- Fixes for Jpeg encoding in Python 3, fixes #577 [wiredfool]
- Added support for JPEG 2000 [al45tair]
- Add more detailed error messages to Image.py [larsmans]
- Avoid conflicting _expand functions in PIL & MINGW, fixes #538 [aclark]
- Merge from Philippe Lagadec’s OleFileIO_PL fork [vadmium]
- Fix ImageColor.getcolor [homm]
- Make ICO files work with the ImageFile.Parser interface, fixes #522 [wiredfool]
- Handle 32bit compiled python on 64bit architecture [choppsv1]
- Fix support for characters >128 using .pcf or .pil fonts in Py3k. Fixes #505 [wiredfool]
- Skip CFFI test earlier if it's not installed [wiredfool]
- Fixed opening and saving odd sized .pcx files, fixes #523 [wiredfool]
- Fixed palette handling when converting from mode P->RGB->P [d_schmidt]
- Fixed saving mode P image as a PNG with transparency = palette color 0 [d-schmidt]
- Improve heuristic used when saving progressive and optimized JPEGs with high quality values [e98cuenc]
- Fixed DOS with invalid palette size or invalid image size in BMP file [wiredfool]
- Added support for BMP version 4 and 5 [eddwardo, wiredfool]
- Fix segfault in getfont when passed a memory resident font [wiredfool]
- Fix crash on Saving a PNG when icc-profile is None [brutasse]
- Cffi+Python implementation of the PixelAccess object [wiredfool]
- PixelAccess returns unsigned ints for I16 mode [wiredfool]
- Minor patch on booleans + Travis [sciunto]
- Look in multiarch paths in GNU platforms [pinotree]
- Add arch support for pcc64, s390, s390x, armv7l, aarch64 [manisandro]
- Add arch support for ppc [wiredfool]
- Correctly quote file names for WindowsViewer command [cgohlke]
- Prefer homebrew freetype over X11 freetype (but still allow both) [dmckeone]

OS X 10.9.2 issues
------------------

This happened:

- https://github.com/python-imaging/Pillow/issues/527

Security issues
---------------

This happened:

- https://github.com/python-imaging/Pillow/pull/548

Logo
----

Pillow has a logo thanks to Alastair Houghton:

- https://github.com/python-imaging/Pillow/issues/575

Keep using and supporting Pillow!
