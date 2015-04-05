Pillow 2015 Report
==================

:date: Sun Apr  5 18:50:50 EDT 2015
:tags: Plone, Python

.. image:: /images/pillow-2015-report.png
    :alt: Most interesting man

*Pillow is the friendly PIL fork by Alex Clark and Contributors. PIL is the Python Imaging Library by Fredrik Lundh and Contributors.*

The state of the Pillow
-----------------------

Pillow Fighter #2 Eric Soroos had some time constraints recently so I managed the Pillow 2.8 release. While preparing the release I also reviewed and updated the entire project, including:

- Issues
- Pull Requests
- Documentation
- Website

July of 2015 will mark Pillow's 5th anniversary and as of 2015, PIL is 20 years old. In early 2015, the state of the Pillow is good. Here are some statistics:

- Over 5.5 million PyPI downloads.

  - About 36 distributions uploaded with each release, including Windows Eggs/Exes/Wheels, OS X Wheels and source distributions.

- 4 core developers AKA Pillow Fighters, including the recently added Alexander Karpinsky (AKA 'homm').
- 100 total committers.
- 66 open issues (431 closed).
- 12 open pull requests (672 closed).

Issues
------

All issues were pruned, including:

- Applying labels and milestones
- Changing state when appropriate
- Asking for status updates

At this time, most if not all issues have at least one label e.g. `"bug" <https://github.com/python-pillow/Pillow/labels/Bug>`_ and many have milestones configured e.g. "2.9.0". The most meaningful milestones designate either "this release" or "next release" or "future". The most meaningful labels designate "needs code review or tests" or "bug or enhancement" or "question".

Pull Requests
-------------

All mergable pull requests were merged just prior to the 2.8.0 release. Of the remaining open pull requests, most `need code review <https://github.com/python-pillow/Pillow/labels/Needs%20Code%20Review>`_ and the rest are experimental or in progress.

Documentation
-------------

Pillow's documentation is now sizeable, a large part of which was forked from the PIL handbook and some of which is created automatically by Sphinx. The remainder is new and was the focus of recent updates [1]_, [2]_, [3]_:

- https://github.com/python-pillow/Pillow/blob/master/README.rst
- https://github.com/python-pillow/Pillow/blob/master/CONTRIBUTING.md
- https://github.com/python-pillow/Pillow/blob/master/RELEASING.md
- http://pillow.readthedocs.org/installation.html

Website
-------

Finally, the website received some much needed attention. We're currently using a theme provided by GitHub Pages, and minimal effort is invested to maintain it, but we may be `interested in building a new one <https://github.com/python-pillow/Pillow/issues/1180>`_.

Notes
-----

.. [1] https://github.com/python-pillow/Pillow/pull/1175
.. [2] https://github.com/python-pillow/Pillow/pull/1179
.. [3] https://github.com/python-pillow/Pillow/pull/1181

.. raw:: html

    <br />
    <script data-gratipay-username="aclark4life" src="//grtp.co/v1.js"></script>
