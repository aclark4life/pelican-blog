Building Windows Installers In The Cloud
########################################
:date: 2012-08-01 22:19
:category: Mozilla, Plone, Python

With pythonpackages.com, I want to solve real problems for people today.
So here's a proof of concept for building Windows installers quickly and
easily "in the cloud" (i.e. without a Windows machine local). This
article is mostly about the back end, as the front end is `already
documented`_. *TL;DR: We're moving from proof-of-concept phase to
useful-service phase. If you find the demo interesting and want to help
build something great, please consider purchasing one of `our current
plans`_.*

Step 1: To The Clouds
=====================

For the purpose of the demo, I booted up a Windows server on Rackspace
Cloud and started installing things. `|image0|`_ On the short list of
things to install was:

-  Python 2.7 from python.org.
-  GitHub for Windows from github.com (mainly for git.)
-  pythonpackages.com from bitbucket.org (free private repos!)
-  Microsoft compiler (free version, make sure to use the same one used
   to compile Python.)
-  Redis for Windows (Hell froze over, you can find this in Microsoft's
   GitHub account: `https://github.com/MSOpenTech/Redis`_.)
-  Vim.exe (which I copy to vi.exe because I hate typing vim.)

Once I had all these things in place, I was able to:

-  Install pythonpackages.com (pip install -r requirements.txt.)
-  Compile and run Redis (Several projects bundled together in Visual
   Studio is apparently called a "solution", how quaint!)
-  Start the site.
-  Start testing.

`|image1|`_

Step 2: Fix all the bugs
========================

This step involved a lot of cursing:

-  Backslashes.
-  Lack of vi key bindings.
-  Other Windows-isms.

But I also praised my `CoRD Remote Desktop Client`_ because it worked
awesome. Anyway, the bugs/issues I fixed (and didn't fix) were roughly:

-  Create new application on GitHub and configured keys accordingly.
-  Switch Stripe keys to testing.
-  Fix Python paths and other trivial changes, so the application can
   run \`python setup.py bdist\_wininst\`.
-  JavaScript is completely broken for some reason I've yet to determine
   (haven't looked yet, but guessing Windows path related).

Step 3: Profit!
===============

I have to admit: I was giddy when it started working, and I was able to
create a Windows Installer for Pillow (Python Imaging Library fork).
[caption id="attachment\_5143" align="aligncenter"
width="300"]\ `|image2|`_ (We know there are security implications here.
We are currently addressing them as best as we can.)[/caption]
`|image3|`_ I was even happier when I ran the installer and it worked.
`|image4|`_ `|image5|`_ That's it. Next I hope to `get some customers`_
so I can keep the Windows box running, and make it available to the
public.

Big Picture
===========

In case you are interested, the `roadmap for beta Q3 is here`_. I will
also mention that I recently used `Dia`_ (<3) to create this
info-graphic, in hopes of better communicating what I'm trying to build.
Check it out! `|image6|`_

.. raw:: html

   </p>

.. _already documented: http://docs.pythonpackages.com/en/latest/introduction.html
.. _our current plans: http://pythonpackages.com/plans
.. _|image7|: http://aclark4life.files.wordpress.com/2012/08/screen-shot-2012-08-01-at-3-41-28-pm.png
.. _`https://github.com/MSOpenTech/Redis`: https://github.com/MSOpenTech/Redis
.. _|image8|: http://aclark4life.files.wordpress.com/2012/08/50-56-240-204-screen-capture.png
.. _CoRD Remote Desktop Client: http://cord.sourceforge.net/
.. _|image9|: http://aclark4life.files.wordpress.com/2012/08/screen-shot-2012-08-01-at-4-39-53-pm.png
.. _|image10|: http://aclark4life.files.wordpress.com/2012/08/buddy-screen-capture.png
.. _|image11|: http://aclark4life.files.wordpress.com/2012/08/buddy-screen-capture-2.png
.. _|image12|: http://aclark4life.files.wordpress.com/2012/08/buddy-screen-capture-3.png
.. _get some customers: http://pythonpackages.com/plans
.. _roadmap for beta Q3 is here: http://docs.pythonpackages.com/en/latest/roadmap.html
.. _Dia: http://dia-installer.de/
.. _|image13|: http://aclark4life.files.wordpress.com/2012/08/pythonpackages-diagram.png

.. |image0| image:: http://aclark4life.files.wordpress.com/2012/08/screen-shot-2012-08-01-at-3-41-28-pm.png?w=300
.. |image1| image:: http://aclark4life.files.wordpress.com/2012/08/50-56-240-204-screen-capture.png?w=300
.. |image2| image:: http://aclark4life.files.wordpress.com/2012/08/screen-shot-2012-08-01-at-4-39-53-pm.png?w=300
.. |image3| image:: http://aclark4life.files.wordpress.com/2012/08/buddy-screen-capture.png?w=300
.. |image4| image:: http://aclark4life.files.wordpress.com/2012/08/buddy-screen-capture-2.png?w=300
.. |image5| image:: http://aclark4life.files.wordpress.com/2012/08/buddy-screen-capture-3.png?w=300
.. |image6| image:: http://aclark4life.files.wordpress.com/2012/08/pythonpackages-diagram.png?w=300
.. |image7| image:: http://aclark4life.files.wordpress.com/2012/08/screen-shot-2012-08-01-at-3-41-28-pm.png?w=300
.. |image8| image:: http://aclark4life.files.wordpress.com/2012/08/50-56-240-204-screen-capture.png?w=300
.. |image9| image:: http://aclark4life.files.wordpress.com/2012/08/screen-shot-2012-08-01-at-4-39-53-pm.png?w=300
.. |image10| image:: http://aclark4life.files.wordpress.com/2012/08/buddy-screen-capture.png?w=300
.. |image11| image:: http://aclark4life.files.wordpress.com/2012/08/buddy-screen-capture-2.png?w=300
.. |image12| image:: http://aclark4life.files.wordpress.com/2012/08/buddy-screen-capture-3.png?w=300
.. |image13| image:: http://aclark4life.files.wordpress.com/2012/08/pythonpackages-diagram.png?w=300
