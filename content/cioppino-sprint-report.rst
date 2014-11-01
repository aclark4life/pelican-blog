Cioppino Sprint Report
================================================================================

:date: 2011-02-16 09:04
:tags: Plone

The `Cioppino Sprint`_ was recently held in Bodega Bay, CA. It was a `beautiful location`_ for a gathering of awesome Plone folks; and much was accomplished. Unfortunately on the second morning of the sprint, we were all deeply saddened to hear about the passing of Dorneles Treméa.

.. image:: https://raw.github.com/ACLARKNET/blog/gh-pages/images/bodega.jpg
    :alt: alternate text

The passing of Dorneles Treméa
------------------------------

I didn't know Dorneles very well, but he was certainly someone I idolized during my initial Plone fascination days (e.g. "Who are all these cool people with such cool names!"). And after digging through my old emails, I now remember we had several pleasant exchanges over the years.

Memories
~~~~~~~~

In particular, I have this memory of Dorneles and Alan Runyan sitting together at the Plone Conference 2008 sprint, smiling and working on their laptops. Before his death, it was just a random image that would occasionally pop into my head. Now, it's something I'll remember him by.

We also corresponded briefly about his `ExternalStorage`_ add-on for Plone, around the time we upgraded plone.org from Plone 2.5 to Plone 3.0 (circa 2008), as well as traded emails about his invitation to attend Plone Conference 2008 in DC (for his visa application).  

The funniest thing he ever said to me was when I was making the rounds asking for donations for Plone Conference 2008. He replied,

    "Are you aware that you're talking with a 3rd world citizen?"

I'm not sure if I offended him, or what. But it struck me funny at the time (and he went on to joke about how donations usually flow in the other direction, ending with his tongue stuck out i.e. ":-p") :-). It also reminded me of one the things I love most about Plone: the opportunity (I may never get otherwise) to correspond/collaborate with cool, passionate people all over the world.

To me, Dorneles was one of the living embodiments of the *coolness* and *worldliness* of the Plone project.

Wishes
~~~~~~

My condolences and best wishes to his family, I hope you know how much he meant to so many folks in the Plone and Python communities. And just how many lives he touched with his work. And goodbye Dorneles; though I knew you very little, I will miss you very much. May your legacy live on, long in to the future.

Incidentally, if you would like to give money to help support Dorneles' family in the aftermath of this tragedy, you can do so here: `http://associacao.python.org.br/doacoes-familia-dorneles`_.

Anyway, the sprint (or at least my part of it) was awesome! Amidst the very sad and shocking news of Dorneles' passing, we all kept busy with our work.

Sprint report
-------------

It's a bit overwhelming to try and capture everything that happened (and I was only there for two days!); hopefully this report will be useful. The focus of this sprint was evaluator approachability (i.e. making Plone look good to prospective new users).

Day 1 and Day 2 
~~~~~~~~~~~~~~~~

Steve McMahon (SteveM) was our host. Alex Limi (limi) provided general direction regarding strategies to improve plone.net, documentation, and end user support. But most importantly, he pointed out that the first stop for any prospective new user is the website, so it's important that it look good.

David Glick (davisagli) and Elizabeth Leddy (eleddy) wasted no time in diving in to the 150 or so open tickets in the (now defunct) `plone.org issue tracker`_.

I (aclark) quickly fell into the role of the "deployment witch" (a role I enjoy), and suggested people simply push the **ACLARK** button (née Staples Easy Button) whenever they needed their code deployed to plone.org.

We closed a good number of tickets this way.

Additionally:

-  Ross Patterson (zenwryly) grabbed a hold of the `PloneOrg add-on`_ (the add-on that powers plone.org) and added tests (among other things).
-  Tyler Randles (hennaheto) and Trish Ang (feeeeesh) fixed a number of CSS annoyances, which were `committed by SteveM`_ (while Tyler & Trish pondered core commit access). My favorite of which is the now-blissfully-aligned username and password fields of the login\_form:
-  zenwryly fixed the `team section`_ of plone.org.
-  davisagli completed the last remaining task to fix `PloneSoftwareCenter`_ permissions on plone.org (the sharing tab finally works now!)
-  limi `fixed a CSS sprite issue`_ on plone.org (involving https, I think).
-  SteveM tackled `SSL certificate issues`_ on plone.org.
-  aclark took a stab at plone.net by converting the old style add-on Product that powers it to a `new style Egg package`_. zenwryly then `took that ball and ran with it`_, added tests and otherwise prepared for the future (i.e. Plone 4 compat).
-  Jon Stahl (remotely) added a `"follow" section`_ to plone.org.
-  hennaheto and feeeeesh produced this amazing (but `possibly non-compliant`_) sprint logo

Day 3, Day 4 and Day 5 
~~~~~~~~~~~~~~~~~~~~~~~

Unfortunately, I had to leave on Friday morning but these are some of the things that happened after I left. Most importantly, Tom Kapanka (spanktar) arrived Thursday night and Bill Deegan arrived on Friday. And then:

-  zenwryly updated PloneServicesCenter to Plone 4.
-  limi and zenwryly replaced images of "showcased sites" in PloneServicesCenter with a web screenshot service to eliminate the need for storing images. (This move is still in progress, and various folks are working on issues with the web screenshot service. Please be patient!)
-  zenwryly and limi moved content from plone.net to plone.org.
-  aclark (remotely) pulled the DNS trigger on plone.net (re-configured A records for plone.net, to resolve to the same IP as plone.org)
-  eleddy and spanktar created and released `cioppino.twothumbs`_ to facilitate "thumb style" (up/down) ratings in PloneSoftwareCenter.
-  davisagli made it so Plone can start without PIL (via fixes to PlonePAS and plone.app.blob). And these fixes even made it in to Plone 4.1a3! To be clear, Plone still requires PIL to render images but it will start if it's missing.
-  davisagli and eleddy refactored the PloneOrg buildout
-  Bill and limi moved the remaining old Plone installers from Sourceforge to `dist.plone.org`_.

Post-sprint sprinting
~~~~~~~~~~~~~~~~~~~~~

One of the great things about a sprint is that it really focuses
attendees on accomplishing their tasks, long after they have left the
event. To that end:

-  aclark triaged the remaining tickets in the plone.org tracker, and did a final tally of closed ticket rankings: davisagli (55), aclark (32), eleddy (28), limi (7). davisagli wins! :-)
-  aclark got inspired to begin uploading the half dozen or so missing videos from various Plone Conference 2008 talks (which were finally sent to him by the video company circa last year). Look for these to `land on plone.org`_ soon.
-  eleddy continued to develop the “two thumbs” feature.
-  eleddy and aclark deployed the "two thumbs" feature to plone.org.  (This feature may not work as expected yet, eleddy is resolving issues.) Check it out:
-  limi continued to improve the documentation/ and support/ sections of plone.org. Here are some screenshots of how the new sections will look once they launch:

That's it! Just so you don't worry the sprinters worked too hard, you can rest assured everyone was in good hands with zenwryly and his travelling-bar.

*If you enjoyed reading this report and/or appreciate all the fun-but-hard work that goes in to attending a sprint, please consider* `donating to my travel fund`_. *Only three days left, and I'm still a few dollars short!*

.. _Cioppino Sprint: http://coactivate.org/projects/snow-sprint-west-2011/project-home
.. _beautiful location: http://twitpic.com/3y21yk
.. _ExternalStorage: http://pypi.python.org/pypi/Products.ExternalStorage
.. _`http://associacao.python.org.br/doacoes-familia-dorneles`: http://associacao.python.org.br/doacoes-familia-dorneles
.. _plone.org issue tracker: http://dev.plone.org/plone.org
.. _PloneOrg add-on: http://dev.plone.org/plone/browser/plone.org/Products.PloneOrg/trunk
.. _committed by SteveM: http://dev.plone.org/plone/changeset/47345/
.. _team section: http://plone.org/team
.. _PloneSoftwareCenter: http://dev.plone.org/collective/browser/Products.PloneSoftwareCenter/trunk
.. _fixed a CSS sprite issue: http://dev.plone.org/plone/changeset/47428/
.. _SSL certificate issues: http://dev.plone.org/plone/changeset/47507/
.. _new style Egg package: http://dev.plone.org/collective/browser/Products.PloneServicesCenter/trunk
.. _took that ball and ran with it: http://rpatterson.net/blog/cioppino-sprint
.. _"follow" section: http://plone.org/follow
.. _possibly non-compliant: http://plone.org/foundation/logo/logoguidelines.pdf/view
.. _cioppino.twothumbs: http://pypi.python.org/pypi/cioppino.twothumbs/1
.. _dist.plone.org: http://dist.plone.org/archive/
.. _land on plone.org: http://plone.org/2008
.. _donating to my travel fund: http://blog.aclark.net/2011/01/21/help-alex-clark-help-plone/
