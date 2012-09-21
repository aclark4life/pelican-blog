Spaces fixed!
#############
:date: 2008-03-06 09:31
:tags: Plone

For those of you using Spaces in Mac OS X, I'd like to follow up my
`previous post`_ with some exciting news regarding Spaces in Mac OS X
10.5.2. It's "fixed"! Thousands of former FVWM users can now rejoice as
they enjoy sane desktop pager functionality. As you know, I've been
tracking the development of the "Spaces... Spaces... Spaces..." hack
(read: waiting for it to support 10.5.2) and I just noticed that the
issue has actually been resolved by Apple, yay! See this post on
macosxhints.com for more information:
`http://www.macosxhints.com/article.php?story=2008021122525348`_

.. raw:: html

   <p>

The short of it is, to alter the annoying spaces-follows-application
behavior, do this:

::

      % defaults write com.apple.dock workspaces-auto-swoosh -bool NO

::

      % sudo killall Dock

Now Plonistas everywhere (including Tomster) can give Spaces another
try!

.. raw:: html

   </p>

And now, with my sincerest thanks to Apple, I leave you to go work in
another Space...

.. _previous post: spaces-spaces-spaces-fix
.. _`http://www.macosxhints.com/article.php?story=2008021122525348`: http://www.macosxhints.com/article.php?story=2008021122525348
