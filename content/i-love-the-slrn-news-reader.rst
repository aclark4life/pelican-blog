I love the slrn news reader
###########################

:date: 2007-10-17 09:26
:tags: Plone

I've been meaning to write this blog entry about ***slrn*** ever since I started using it some time last year. Finally, here it is. But this is not the blog entry I had originally intended to write. There were some grandiose ideas about where I first heard of it; the blog entry that inspired me to try it; how I was frustrated with the alternatives; none of these are present here in any detail. That is because I'm frustrated with the length of time it takes to write a "quality" blog entry, when all I want to do is get the information out. (But that is a separate blog entry :-))

To that end, here are a few things I'd like you to know about ***slrn***:

#. It rocks, for those that enjoy terminal applications as I do (e.g.  mutt, w3m, etc.) And by "rocks" I mean, it allows you to do in a terminal what most people do in a graphical application. Further, it allows you to do it the way you want (for the most part) and by that I mean, it allows you to bind keys to actions.
#. It's a bit confusing to get started, that is what I'd like to help with here. There is a `default config file that you'll want to copy to ~/.slrnrc`_, and
#. there are some additional configuration parameters I use that were hard to track down. Those are:

::

    set confirm_actions 14visible_headers "From:,Subject:,Newsgroups:,Followup-To:,Reply-To:,Date:"set query_read_group_cutoff 0set uncollapse_threads 1set netiquette_warnings 0

Most of these are self-explanatory, but if you are looking at "set confirm\_actions 14" and thinking "wtf?" you are not alone :-) I'll leave it as an exercise to the reader to explore. See: `http://slrn.sourceforge.net/manual/slrn-manual.html`_ for more information. I hope this post helps someone get started using ***slrn**!*

*Next, in Part II, I will cover **slrnpull**; the program I use (distributed with slrn) to download news. I never "read it live" and I will explain why ;-)*

.. _default config file that you'll want to copy to ~/.slrnrc: http://slrn.sourceforge.net/downloads/slrn.rc
.. _`http://slrn.sourceforge.net/manual/slrn-manual.html`: http://slrn.sourceforge.net/manual/slrn-manual.html
