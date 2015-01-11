New Django Website
==================

:tags: Plone, Python
:date: Sat Jan 10 18:14:36 EST 2015

*After a series of Django gigs recently, I had the urge to redevelop our company website in Django; I am very happy with the results.*

.. image:: /images/aclarknet-django.png
    :alt: Website front page

Same theme, different backend
-----------------------------

The Pyramid version of aclark.net was almost two years old and needed an overhaul. Django appeared attractive because:

- I know Django, but I don't know enough Django. Like with Pyramid and Plone before, much Django was learned during the process of developing this site over the course of one month.
- There was no "content" with the previous (Pyramid) site. The idea of putting my "content" in Django models appealed to me.
- The new `Django project <https://djangoproject.com>`_ website is awesome! An awesome website makes me want to build another awesome website with an awesome web framework. Awesome.

I hate code generators
----------------------

I typically hate using code generators, full stop. But somehow Django's ``startproject`` and ``startapp`` don't make me want to vomit. So I used them in an organic [1]_ way, to make some `obnoxiously long package names <https://github.com/ACLARKNET/aclarknet-django/tree/master/aclarknet/aclarknet/aclarknet>`_, and I *miraculously* don't hate the results! This can only mean:

- I am more tolerant of boilerplate code when learning a new framework, and/or:
- The process of creating the boilerplate code and the resulting boilerplate are so elegant/minimalistic that my insatiable desire for elegance/minimalism is at least partially satisified.

No Postgres? No problem
-----------------------

The idea of having to develop locally with Postgresql (or some other "real" database) feels "heavy" to me. With sqlite, I don't have to worry about database setup until I'm ready to worry about database setup [2]_. 

I even pushed to Heroku with the sqlite database checked in, until I was ready to deploy Postgres. And I still use sqlite locally.

Bootstrap all the things
------------------------

Sure Bootstrap is ubiquitious now, but it remains attractive nonetheless. One of the first tasks I performed was add ``django-bootstrapped`` to my ``INSTALLED_APPS`` [3]_.

And because it's 2015, I Bower-installed Bootstrap and Fontawesome for my theme development.

Make like a tree and file
-------------------------

Lately I've gotten into the habit of using good-ol' Make to automate various tasks [4]_. This project was no exception::

    dump:
        curl -o latest.dump `heroku pgbackups:url`
    push:
        git push
        git push heroku master
    sync:
        heroku run python aclarknet/manage.py syncdb
    publish:
        git commit -a -m "Update"

Add-ons, Apps, Eggs, Distributions, Packages, Products, Wheels
--------------------------------------------------------------

I am literally annoyed by the figurative abomination that is Python packaging terminology. It makes sense though, because:

- Python-the-language includes terminology applied to itself.
- Python-the-community debates the terminology to apply to the language.
- Software written in Python defines its own terminology, unrelated to Python-the-language but may be overlapping.
- Software communities debate terminology to apply to their software.
- There are hundreds of software communities built on top of Python software, so there is bound to be some confusion, discrepancies, overlap, etc.

All of that was so I could tell you I pip-installed the following::

    Django
    Pillow
    django-admin-bootstrapped
    django-cumulus
    dj-database-url
    dj-static
    gunicorn
    psycopg2
    -e aclarknet

.. [1] ``django-admin startproject aclarknet; cd aclarknet/aclarknet; django-admin startapp aclarknet``

.. [2] Granted, the perceived heaviness is much worse than the *actual* burden of "real" database setup which is admittedly fairly trivial: ``brew install postgres``.

.. [3] The Django admin without Bootstrap reminds me of the ZMI without Bootstrap, which `I also don't like <https://pypi.python.org/pypi/zope2_bootstrap>`_.

.. [4] Embarrassingly, I create the tabs with ``s/    /\t/`` because my tabstop is set to 4 spaces.
