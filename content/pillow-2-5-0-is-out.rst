Pillow 2-5-0 is out!
====================

:date: 2014-07-05 11:15
:tags: Django, Mozilla, Plone, Python

**Pillow is the "friendly" PIL fork by Alex Clark and Contributors. PIL is the Python Imaging Library by Fredrik Lundh and Contributors**

Since Pillow 2.0 the Pillow Team has adopted a quarterly release cycle; as such, Pillow 2.5.0 is out! Here's what's new in this release:

2.5.0 (2014-07-01)
------------------

- Imagedraw rewrite
  [terseus, wiredfool]

- Add support for multithreaded test execution
  [wiredfool]

- Prevent shell injection #748
  [mbrown1413, wiredfool]
  
- Support for Resolution in BMP files #734
  [gcq]
  
- Fix error in setup.py for Python 3
  [matthew-brett]

- Pyroma fix and add Python 3.4 to setup metadata #742
  [wirefool]

- Top level flake8 fixes #741
  [aclark]

- Remove obsolete Animated Raster Graphics (ARG) support
  [hugovk]

- Fix test_imagedraw failures #727
  [cgohlke]

- Fix AttributeError: class Image has no attribute 'DEBUG' #726
  [cgohlke]

- Fix msvc warning: 'inline' : macro redefinition #725
  [cgohlke]

- Cleanup #654
  [dvska, hugovk, wiredfool]

- 16-bit monochrome support for JPEG2000
  [videan42]

- Fixed ImagePalette.save
  [brightpisces]

- Support JPEG qtables
  [csinchok]

- Add binary morphology addon
  [dov, wiredfool]

- Decompression bomb protection
  [hugovk]

- Put images in a single directory
  [hugovk]

- Support OpenJpeg 2.1
  [al45tair]

- Remove unistd.h #include for all platforms
  [wiredfool]

- Use unittest for tests
  [hugovk]

- ImageCms fixes
  [hugovk]

- Added more ImageDraw tests
  [hugovk]

- Added tests for Spider files
  [hugovk]

- Use libtiff to write any compressed tiff files
  [wiredfool]

- Support for pickling Image objects
  [hugovk]

- Fixed resolution handling for EPS thumbnails
  [eliempje]

- Fixed rendering of some binary EPS files (Issue #302)
  [eliempje]

- Rename variables not to use built-in function names
  [hugovk]

- Ignore junk JPEG markers
  [hugovk]

- Change default interpolation for Image.thumbnail to Image.ANTIALIAS
  [hugovk]

- Add tests and fixes for saving PDFs
  [hugovk]

- Remove transparency resource after P->RGBA conversion
  [hugovk]

- Clean up preprocessor cruft for Windows
  [CounterPillow]

- Adjust Homebrew freetype detection logic
  [jacknagel]

- Added Image.close, context manager support.
  [wiredfool]

- Added support for 16 bit PGM files.
  [wiredfool]

- Updated OleFileIO to version 0.30 from upstream
  [hugovk]

- Added support for additional TIFF floating point format
  [Hijackal]

- Have the tempfile use a suffix with a dot
  [wiredfool]

- Fix variable name used for transparency manipulations
  [nijel]


Acknowledgements
----------------

With every release, there are notable contributions I must acknowledge:

- Thanks to Stephen Johnson for contributing http://pillow.readthedocs.org, we continue to rely on & extend this resource.

- Thanks to Christopher Gohlke for producing Windows Egg, Exe, and Wheel distributions.

- Thanks to Matthew Brett for producing OS X Wheels (for the first time ever!)

- Thanks to Eric Soroos for his contributions and serving as "Pillow Man #2" (2nd in command).

- Welcome to Hugo VK who has joined the Pillow Team & contributed significantly to this release.

- Thanks to all the remaining unnamed contributors! We appreciate every commit.

Enjoy Pillow 2.5.0 & please report issues here: https://github.com/python-imaging/Pillow/issues
