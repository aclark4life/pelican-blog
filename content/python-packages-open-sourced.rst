Python Packages Open Sourced
============================

:date: 2013-10-13 0:00
:tags: Plone, Python

Today I am open sourcing the code that ran pythonpackages.com from late 2011 to late 2012. You can find it here:

    https://github.com/pythonpackages/vanity_app

Why I Waited
------------

I waited a long time before doing this because:

- It's embarrassing. I originally wanted to have pythonpackages.com rewritten with some tests before doing this. But that never happened.
- Some of it was private. The original repository had things like the database checked in to it which had users' names in it. There were also various and sundry account credentials and API keys that needed to be removed. It took some time and motivation to get all that done.
- I needed historical perspective which does not occur without the passage of time. The packaging landscape has totally changed for the better since I last worked on pythonpackages.com, and I'm now ready to put the past behind me and focus on the future.

Why Now
-------

- I managed to find some time thanks to the U.S. Government <cough> (Speaking of that: this would be a great time to hire me for any tasks you need done. Email: aclark@aclark.net)
- Folks have been asking about it. I originally planned to re-launch by Q2 2013, but that nevered happened. I'm now planning to have something working by the end of the year and I'm actively working on the site again as of right now.
- I know what to focus on. The original pythonpackages.com tried to do way too much, but the most useful thing it did was automate the release of packages from GitHub to PyPI through a GitHub service: https://github.com/github/github-services/blob/master/lib/services/pythonpackages.rb. I'm going to focus on getting that working again without all the spaghetti code wrapped around it. I believe a lot of useful services can be built around this feature.

Enjoy
-----

I hope you enjoy reading the source and if you end up using it for something please drop me a line: aclark@aclark.net.
