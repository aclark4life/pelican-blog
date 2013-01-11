Building Windows Installers In The Cloud
########################################

:date: 2012-08-01 22:19
:tags: Mozilla, Plone, Python

With pythonpackages.com, I want to solve real problems for people today. So here's a proof of concept for building Windows installers quickly and easily "in the cloud" (i.e. without a Windows machine local). This article is mostly about the back end, as the front end is `already documented`_. *TL;DR: We're moving from proof-of-concept phase to useful-service phase. If you find the demo interesting and want to help build something great, please consider purchasing one of `our current plans`_.*

Step 1: To The Clouds
=====================

For the purpose of the demo, I booted up a Windows server on Rackspace Cloud and started installing things. On the short list of things to install was:

-  Python 2.7 from python.org.
-  GitHub for Windows from github.com (mainly for git.)
-  pythonpackages.com from bitbucket.org (free private repos!)
-  Microsoft compiler (free version, make sure to use the same one used to compile Python.)
-  Redis for Windows (Hell froze over, you can find this in Microsoft's GitHub account: `https://github.com/MSOpenTech/Redis`_.)
-  Vim.exe (which I copy to vi.exe because I hate typing vim.)

Once I had all these things in place, I was able to:

-  Install pythonpackages.com (pip install -r requirements.txt.)
-  Compile and run Redis (Several projects bundled together in Visual
   Studio is apparently called a "solution", how quaint!)
-  Start the site.
-  Start testing.

Step 2: Fix all the bugs
========================

This step involved a lot of cursing:

-  Backslashes.
-  Lack of vi key bindings.
-  Other Windows-isms.

But I also praised my `CoRD Remote Desktop Client`_ because it worked awesome. Anyway, the bugs/issues I fixed (and didn't fix) were roughly:

-  Create new application on GitHub and configured keys accordingly.
-  Switch Stripe keys to testing.
-  Fix Python paths and other trivial changes, so the application can run \`python setup.py bdist\_wininst\`.
-  JavaScript is completely broken for some reason I've yet to determine (haven't looked yet, but guessing Windows path related).

Step 3: Profit!
===============

I have to admit: I was giddy when it started working, and I was able to create a Windows Installer for Pillow (Python Imaging Library fork). I was even happier when I ran the installer and it worked. That's it. Next I hope to `get some customers`_ so I can keep the Windows box running, and make it available to the public.

Big Picture
===========

In case you are interested, the `roadmap for beta Q3 is here`_. I will also mention that I recently used `Dia`_ (<3) to create this info-graphic, in hopes of better communicating what I'm trying to build. Check it out!

.. _already documented: http://docs.pythonpackages.com/en/latest/introduction.html
.. _our current plans: http://pythonpackages.com/plans
.. _`https://github.com/MSOpenTech/Redis`: https://github.com/MSOpenTech/Redis
.. _CoRD Remote Desktop Client: http://cord.sourceforge.net/
.. _get some customers: http://pythonpackages.com/plans
.. _roadmap for beta Q3 is here: http://docs.pythonpackages.com/en/latest/roadmap.html
.. _Dia: http://dia-installer.de/
