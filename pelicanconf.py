#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Alex Clark"
SITENAME = u"Alex Clark"
SITEURL = 'http://blog.aclark.net'

#TIMEZONE = 'America/New York'

DEFAULT_LANG = 'en'

# Blogroll
#LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
#          ('Python.org', 'http://python.org'),
#          ('Jinja2', 'http://jinja.pocoo.org'),
#          ('You can modify those links in your config file', '#'),)
# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

SOCIAL = (
    ('atom feed (Mozilla)', 'http://blog.aclark.net/Mozilla.atom.xml'),
    ('atom feed (Plone)', 'http://blog.aclark.net/Plone.atom.xml'),
    ('atom feed (Python)', 'http://blog.aclark.net/Python.atom.xml'),
    ('ACLARK.NET, LLC', 'http://aclark.net'),
    ('GitHub', 'http://github.com/aclark4life'),
    ('PythonPackages', 'http://pythonpackages.com'),
    ('Twitter', 'http://twitter.com/aclark4life'),
)

DEFAULT_PAGINATION = 10

# Default category AKA header configuration
DEFAULT_CATEGORY = "Blog"

# Generate feeds for tags instead of categories
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
TAG_FEED_ATOM = 'feeds/%s.atom.xml'
TAG_FEED_RSS = None
