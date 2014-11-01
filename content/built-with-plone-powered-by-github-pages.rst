Built with Plone, Powered by GitHub Pages
=========================================

:date: 2013-02-23 12:00
:tags: Plone

Is Plone the next great static website generator? Probably not, but it definitely could be

I am always looking for ways to improve, streamline and otherwise hack my e-life. And this post is about all of the above.
https://raw.github.com/ACLARKNET/blog/gh-pages/images/httrack.png
Plone in the cloud

Plone is still too "heavy" to easily run "in the cloud" (except via http://ploud.com, HT), but it's getting there. In particular, I find this effort by David Bain very inspiring:

    https://github.com/pigeonflight/stack-python-plone

And based on my experiments and research on Heroku:

    https://github.com/aclark4life/zope2-heroku

The only "real" remaining issue seems to be packaging; we need this PLIP to happen sooner, rather than later:

    https://dev.plone.org/ticket/13283

Cheating

In the meantime, one way you can cheat is to export the contents of your Plone site with httrack then host the results for free on GitHub Pages (i.e. "the cloud")

This process if far from perfect [1], but in a pinch it can work. And it recently worked very well for me so I thought I'd share. See:

    http://aclark.net
    https://github.com/ACLARKNET/aclarknet.github.com

These links are my website, and GitHub Pages repository respectively. The website was created with Plone (https://github.com/ACLARKNET/new_style) then exported via httrack, then uploaded to GitHub Pages (to the gh-pages branch of any repo except <{org,user}>>.github.com repos).
[1] httrack got "stuck" on my @@search links, and I've got a lot of duplicate content now. Fortunately I don't mind editing lots and lots of text files :-).
Conclusion

In doing this, I was able to turn off my $11/month "website and IRC server" which makes the CFO happy. And in a year or so with Plone 5, hopefully I'll be able to return to the cloud and edit content "live" again.

What do you think about Plone as a static site generator and/or Plone in the cloud? Let me know in the comments below.
