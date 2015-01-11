New Django Website
==================

:tags: Plone, Python
:date: Sun Jan 11 09:48:24 EST 2015

*After a series of Django gigs in 2014, I had the urge to redevelop our company website in Django; I am very happy with the results. This overview is roughly in order of development from start to finish*.

.. image:: /images/aclarknet-django.png
    :alt: Website front page

Same theme, different backend
-----------------------------

The Pyramid version of aclark.net was almost two years old and needed an overhaul. Django appeared attractive because:

- I know Django, but I don't know enough Django. Like with Pyramid and Plone before, I learned a lot of Django while developing this site over the last few weeks.
- There was no "content" with the previous (Pyramid) site. The idea of putting my "content" in Django models was appealing to me.
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

Sure Bootstrap is ubiquitious now, but it remains attractive nonetheless. One of the first tasks I performed was add ``django-admin-bootstrapped`` to my ``INSTALLED_APPS`` [3]_.

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

I am *literally* annoyed by the *figurative* abomination that is Python packaging terminology. The proliferation of terms is understandable though because of the many layers of *technology*, each with its own *terminology*, that may or may not overlap:

- The Python language
- Various packaging frameworks
- Software written in Python

And all of that was so I could tell you I pip-installed the following::

    Django
    Pillow
    django-admin-bootstrapped
    django-cumulus
    dj-database-url
    dj-static
    gunicorn
    psycopg2
    -e aclarknet

Buildout, Conda, easy_install, pip
----------------------------------

On a related subject, why do I have a `setup.py <https://github.com/ACLARKNET/aclarknet-django/blob/master/aclarknet/setup.py>`_? I get the feeling that Django projects in the wild sometimes use one, and sometimes don't. And the Django documentation `doesn't even mention setup.py <https://docs.djangoproject.com/search/?q=setup.py&release=11>`_. So why do I have one?

In short, because I wanted my project and app in the ``sys.path``. I have a similar feeling that when Django projects/apps/etc don't have setup.py files, they are manipulating sys.path manually to include themselves.

.. [1] ``django-admin startproject aclarknet; cd aclarknet/aclarknet; django-admin startapp aclarknet``

.. [2] Granted, the perceived heaviness is much worse than the *actual* burden of "real" database setup which is admittedly fairly trivial: ``brew install postgres``.

.. [3] The Django admin without Bootstrap reminds me of the ZMI without Bootstrap, which `I also don't like <https://pypi.python.org/pypi/zope2_bootstrap>`_.

.. [4] Embarrassingly, I create the tabs with ``s/    /\t/`` because my tabstop is set to 4 spaces. Maybe I should be change my tabstop setting each time instead?
