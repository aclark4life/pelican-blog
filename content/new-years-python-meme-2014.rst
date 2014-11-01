New Year's Python Meme 2014
===========================

:date: 2013-12-30 14:30
:tags: Django, Mozilla, Plone, Python

**Tarek Ziadé's New Year's Python Meme**

What’s the coolest Python application, framework or library you discovered this year?
-------------------------------------------------------------------------------------------------

This year we have a tie between two must-have packaging-related utilities:

- `check-manifest <https://pypi.python.org/pypi/check-manifest>`_
- `pyroma <https://pypi.python.org/pypi/pyroma>`_

Both of these utilities help you make better Python packages, and I regularly use them in my packages via a Makefile like this::

    test:
        check-manifest
        flake8 *.py
        pyroma
        python setup.py sdist
        python setup.py test
        viewdoc

Good times! And better packages.

What new programming technique did you learn this year?
-------------------------------------------------------------------------------------------------

I didn't program much in 2013 but when I did, I tried to write tests too. Check out the following projects to see how I did:

- `Plock <https://github.com/plock/plock>`_
- `PythonPackages <https://github.com/pythonpackages/pythonpackages>`_

Which open source project did you contribute to the most this year? What did you do?
-------------------------------------------------------------------------------------------------

`Pillow <https://github.com/python-imaging/Pillow>`_. Fork author and project lead. Aside from a working PIL, the most exciting thing about Pillow for me is my `Gittip funding <https://www.gittip.com/aclark4life/>`_ and working with the `Pillow Team <https://github.com/python-imaging?tab=members>`_ which includes most notably Eric Soroos and Christopher Gohlke.

Which Python blogs, websites, or mailing lists did you read the most this year?
-------------------------------------------------------------------------------------------------

This year I cut back to reading *only* the following feeds, consumed via Feedly:

- `Planet Plone <http://planet.plone.org>`_
- `Planet Python <http://planet.python.org>`_
- `gmane.comp.web.zope.plone.devel <http://dir.gmane.org/gmane.comp.web.zope.plone.devel>`_
- `gmane.comp.web.zope.plone.user <http://dir.gmane.org/gmane.comp.web.zope.plone.user>`_

What are the top three things you want to learn next year?
-------------------------------------------------------------------------------------------------

- `JavaScript <https://github.com/aclark4life/javascript_goodparts>`_
- `JavaScript <https://github.com/aclark4life/javascript_goodparts>`_
- `JavaScript <https://github.com/aclark4life/javascript_goodparts>`_

What is the top software, application or library you wish someone would write next year?
-------------------------------------------------------------------------------------------------

I wish there was some "Python to JavaScript bridge software". It's not the complexities of JavaScript that keep me from learning it, it's that I don't have any reason to obsess over it. Plone gave me that opportunity with Python, but not JavaScript (yet). Once that happens, I'm sure I'll be as proficient in JavaScript as I am currently in Python (which is enough to get by).

Want to participate? Copy/paste/answer the questions below then tweet your entry with the #2014pythonmeme hash tag::

    New Year's Python Meme
    ======================

    What’s the coolest Python application, framework or library you discovered this year?
    ----------------------------------------------------------------------------------------
    What new programming technique did you learn this year?
    ----------------------------------------------------------------------------------------
    Which open source project did you contribute to the most this year? What did you do?
    ----------------------------------------------------------------------------------------
    Which Python blogs, websites, or mailing lists did you read the most this year?
    ----------------------------------------------------------------------------------------
    What are the top three things you want to learn next year?
    ----------------------------------------------------------------------------------------
    What is the top software, application or library you wish someone would write next year?
    ----------------------------------------------------------------------------------------
