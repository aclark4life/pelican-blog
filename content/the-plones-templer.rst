The Plones Templer
##################
:date: 2012-07-12 20:48
:tags: Plone, Python

(c.f. Knights Templar) I think we have a situation that could use the
help of the Plone and Python communities at large. It goes something
like this:

#. About 6 years ago, `Daniel Nouri started the ZopeSkel project`_ to
   provide a Zope project template to `PasteScript`_
#. Sometime between then and now, the Plone community latched on to the
   ZopeSkel project to include templates for its projects.
#. About 3 years ago, as part of the ZopeSkel project, `some folks at
   the BBQ`_ sprint built a more user friendly UI on top of PasteScript.
   And some refactoring of the project was planned or occurred, during
   which time the entire project was renamed to "Templer".

At present, if you install the latest ZopeSkel (3.0b3) you get:

::

    $ bin/paster create --list-templates  
    Available templates:
      archetype:         A Plone project that uses Archetypes content types
      basic_buildout:    A basic buildout skeleton
      basic_namespace:   A basic Python project with a namespace package
      basic_package:     A basic setuptools-enabled package
      nested_namespace:  A basic Python project with a nested namespace (2 dots in name)
      paste_deploy:      A web application deployed through paste.deploy
      plone_basic:       A package for Plone add-ons
      plone_nested:      A package for Plone add-ons with a nested namespace
      recipe:            A recipe project for zc.buildout
      zope2_basic:       A Zope project
      zope2_nested:      A nested-namespace Zope package

Looks nice, but some templates are missing. If you install the previous
stable version (2.21.2), you get this:

::

    $ bin/paster create --list-templates
    Available templates:
      archetype:          A Plone project that uses Archetypes content types
      basic_namespace:    A basic Python project with a namespace package
      basic_package:      A basic setuptools-enabled package
      basic_zope:         A Zope project
      kss_plugin:         A project for a KSS plugin
      nested_namespace:   A basic Python project with a nested namespace (2 dots in name)
      paste_deploy:       A web application deployed through paste.deploy
      plone:              A project for Plone add-ons
      plone2.5_buildout:  A buildout for Plone 2.5 projects
      plone2.5_theme:     A theme for Plone 2.5
      plone2_theme:       A theme for Plone 2.1
      plone3_buildout:    A buildout for Plone 3 installation
      plone3_portlet:     A Plone 3 portlet
      plone3_theme:       A theme for Plone 3
      plone4_buildout:    A buildout for Plone 4 developer installation
      plone_app:          A project for Plone add-ons with a nested namespace (2 dots in name)
      plone_hosting:      Plone hosting: buildout with ZEO and Plone versions below 3.2
      plone_pas:          A project for a Plone PAS plugin
      recipe:             A recipe project for zc.buildout
      silva_buildout:     A buildout for Silva projects

Looks a lot better. Additionally, with the previous release (2.21.2) you
can install zopeskel.dexterity, and "dexterity" will show up in the list
of available templates (but not so with 3.0b3). So what's left to finish
the move from ZopeSkel to Templer? I'm told by Chris Ewing (the current
project lead) that it's mostly a matter of missing imports in various
Python packages that provide templates to PasteScript. Let's. Finish.
This. This frustrates me because Paster is a nice system (that provides
pluggable commands, and code gen from templates). And ZopeSkel was a
nice system (that provided additional templates and a friendly UI). And
Templer will be a great system, but it's not there yet. So we need to
help Chris et. al. get it there ASAP. In addition to the code
refactoring, they have produced some `nice documentation available on
readthedocs.org`_. If you are interested in helping, please gather
around the #plone on irc.freenode.net to discuss options (I am aclark on
IRC).

.. _Daniel Nouri started the ZopeSkel project: http://danielnouri.org/blog/devel/zope/quickstart-with-pastescript.html
.. _PasteScript: http://pypi.python.org/pypi/PasteScript/1.7.5
.. _some folks at the BBQ: http://www.coactivate.org/projects/zopeskel-bbq-sprint/project-home
.. _nice documentation available on readthedocs.org: http://templer-manual.readthedocs.org/en/latest/index.html
