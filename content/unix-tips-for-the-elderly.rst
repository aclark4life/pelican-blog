UNIX Tips for the Elderly
================================================================================

:date: 2008-03-06 09:31
:tags: Plone

With apologies to the Plone community for the off-topic post, I'd like to mention this so I won't forget it again (and, in case I do some nice Plonista somewhere wil remind me ;-).

I often want to do ***something*** to a bunch of files on the filesystem, e.g.

::

    find Music/ | xargs -J % echo 'Do something to ' %

The problem is that sometimes the filenames have spaces in them which will cause:

::

    $ find Music/ | xargs -J % 'Do something to ' %
    xargs: unterminated quote

Useless. The best fix I've managed to come up with (which I couldn't recall, hence the blog post)  is to replace the beginning and end of the line with quotes to make the shell happy, e.g.

::

    $ find Music/ | sed -e 's/^/"/' -e 's/$/"/'
    "Music//iTunes/iTunes Music/Yael Naïm/Yael Naïm/03 New Soul.m4a"

So I can do things like:

::

    $ find Music/ | sed 's/^/"/' | sed 's/$/"/' | xargs -J % ls -d %
    Music//iTunes/iTunes Music/Yael Naïm/Yael Naïm/03 New Soul.m4a

or

::

    $ find Music/ | sed 's/^/"/' | sed 's/$/"/' | xargs -J % file %
    Music//iTunes/iTunes Music/Yael Naïm/Yael Naïm/03 New Soul.m4a:
      ISO Media, MPEG v4 system, iTunes AAC-LC

... and afterwards go back to whatever I was supposed to be working on in the first place. There, I feel better now! Thanks for listening,

 

:-)

 

P.S. If anyone knows a better way to do this, please add it in the comments.
