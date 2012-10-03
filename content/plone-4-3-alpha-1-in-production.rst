Plone 4-3 Alpha 1 In Production
===============================
:tags: Plone
:date: 2012-10-03 13:00

I love upgrading Plone. Given the choice between an afternoon in the sun and upgrading Plone… OK I'd probably pick the sun, but it'd be close.

Always upgrading?
-----------------

I would love to see the trend of continuous integration make it's way all the way to deployment, so that one day our Plone sites are getting new code as soon as it's released. Until then, it's nice to know that Plone's upgrade procedure is fairly predictable and stable, if not entirely straightforward [1]_.

How do I upgrade?
-----------------

Unfortunately we *still* get asked this question in IRC. The TLDR (short) explanation is as follows. Got an old Plone? Here's what you should do:

- Don't touch it! Leave it alone. It's probably doing something important.

- Install the latest Plone somewhere that is not the location of your current site. Maybe not even on the same machine.

- Copy the production Data.fs file (usually in var/ somewhere) and any blobs you may have (Plone 4 or greater) to the new installation.

- Restart Plone in the foreground (bin/instance fg). If it starts, great! If it doesn't, look for missing add-ons and add their newest-Plone counterparts (this is usually where all the real work happens). Can't find the latest version? Try contacting the author. Stuck? Try Plone support (http://plone.org/support) or hire a consultant (e.g. http://aclark.net). Otherwise, continue.

- Once your add-ons are in place, start the site in the foreground and give the ZMI a poke (stay out of Plone). Look for broken objects. If you find some, repeat the previous step. Otherwise, continue. 

- Once the ZMI looks good, trigger the migration with the Dry Run checkbox selected. See what you get. If it completes, do it for real. If it doesn't, open a ticket on http://dev.plone.org so we can track the kinds of issues that folks are encountering in the wild. At this point if you are stuck, try to get help from the support forums (http://plone.org/support) or hire a consultant (e.g. http://aclark.net). Otherwise, you are almost done!

- Run the upgrade for real i.e. with the Dry Run checkbox unselected. When it finishes (it could take a while depending on the size of your site) check Plone. If everything looks OK, rejoice! If not, don't worry. Check: ``Site Setup -> ZMI -> portal_skins -> custom``. If there is anything inside the custom folder, rename the custom folder to ``custom_X_X`` where ``X_X`` equals the previous Plone version e.g. ``custom_3_3``. Or, rename it to whatever you like. Or delete it if you don't care about any in-database customizations that have been made. You probably should care, but maybe you don't. Now check Plone again. If everything looks OK, you are done! If not… well you really should be done by now. So if not, please email me: aclark@aclark.net and I will try to help.

That's still a lot to swallow for a summary. The key point is this: **test the upgrade away from the production site. Don't put yourself in an unpleasant situation you can easily avoid**. Once everything works as expected, make a copy of your Data.fs and perform the upgrade on the production site (by editing the buildout.cfg if you know how, or just make the new Plone installation the production site. Need help? Please feel free to email me: aclark@aclark.net to discuss professional assistance.)

How did I upgrade?
------------------

Anyway, the point of this blog entry is to cover the recent upgrade of http://aclark.net to Plone 4.3a1, and the bliss that ensued. Plone 4.3 has lots of goodness in it, most notably the new theme editor from Martin Aspeli. Whilst I haven't fully explored its possibilites, I definitely liked seeing it in place; it's an impressive piece of work and I suspect will be very useful to lots of folks. So here is a brief summary of my upgrade steps, which took about 2-3 days.

Create a new empty repo
~~~~~~~~~~~~~~~~~~~~~~~

I started with a public repo in my personal GitHub account, then forked it to my organization for showcasing:

- https://github.com/ACLARKNET/new_style

Add the buildout
~~~~~~~~~~~~~~~~

Yes, we are still married to Buildout for even the simplest deployments :-/. So in order to make this easy for myself and others, I maintain buildouts for every version of Plone under the http://pythonpackages.com umbrella. I typically start like this from within the checked out repo:

.. code-block:: sh

    $ virtualenv .
    $ bin/pip install zc.buildout
    $ bin/buildout init

I then ``extend`` the desired base configuration (``4.3.x-dev`` in this case) and add additional customizations as needed.

.. code-block:: ini

    [buildout]
    extends = http://pythonpackages.com/buildout/plone/4.3.x-dev

    [plone]
    eggs += 
        z3c.jbot
        ZODB3
    scripts = ZODB3
    resources = ${buildout:directory}/resources
    zcml-additional =
    # XXX Can this be done with p.r.zope2instance yet?
        <configure
            xmlns:browser="http://namespaces.zope.org/browser"
            >
            <include package="z3c.jbot" file="meta.zcml" />
            <browser:jbot directory="${buildout:directory}/templates" />
        </configure>

    [versions]
    Cheetah = 2.2.1
    Pillow = 1.7.7
    Products.DocFinderTab = 1.0.5
    Products.FSDump = 0.9.5
    collective.recipe.supervisor = 0.17
    gdata = 2.0.17
    meld3 = 0.6.9
    plone.app.debugtoolbar = 1.0a2
    supervisor = 3.0b1
    z3c.jbot = 0.7.1
    zope2-bootstrap = 0.0.7

Develop the Diazo theme
~~~~~~~~~~~~~~~~~~~~~~~

With Diazo, Python packaging is optional. And the ``resources`` parameter available from ``plone.recipe.zope2instance`` makes it easy to start theming without a Python package. I started with a bootstrap template:

.. code-block:: html

    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <title>Bootstrap, from Twitter</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="">
        <meta name="author" content="">

        <!-- Le styles -->
        <link href="/++theme++static/css/bootstrap.css" rel="stylesheet">
        <link href="/++theme++static/css/new_style.css" rel="stylesheet">
        <link href='http://fonts.googleapis.com/css?family=Oswald' rel='stylesheet' type='text/css'>
        <style type="text/css">
          body {
            padding-top: 60px;
            padding-bottom: 40px;
          }
        </style>

        <!-- Le HTML5 shim, for IE6-8 support of HTML5 elements -->
        <!--[if lt IE 9]>
          <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
        <![endif]-->

        <!-- Le fav and touch icons -->
        <link rel="shortcut icon" href="/++theme++static/img/favicon.ico">
        <link rel="apple-touch-icon-precomposed" sizes="144x144" href="/++theme++static/ico/apple-touch-icon-144-precomposed.png">
        <link rel="apple-touch-icon-precomposed" sizes="114x114" href="/++theme++static/ico/apple-touch-icon-114-precomposed.png">
        <link rel="apple-touch-icon-precomposed" sizes="72x72" href="/++theme++static/ico/apple-touch-icon-72-precomposed.png">
        <link rel="apple-touch-icon-precomposed" href="/++theme++static/ico/apple-touch-icon-57-precomposed.png">
        <script type="text/javascript">

          var _gaq = _gaq || [];
          _gaq.push(['_setAccount', 'UA-35125830-1']);
          _gaq.push(['_trackPageview']);

          (function() {
            var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
            ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
            var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
          })();

        </script>
      </head>

      <body>

        <div class="navbar navbar-inverse navbar-fixed-top">
          <div class="navbar-inner">
            <div class="container">
              <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
              </a>
              <a class="brand" href="#">Project name</a>
              <div class="nav-collapse collapse">
                <ul class="nav">
                  <li class="active"><a href="#">Home</a></li>
                  <li><a href="#about">About</a></li>
                  <li><a href="#contact">Contact</a></li>
                  <li class="dropdown">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown">Dropdown <b class="caret"></b></a>
                    <ul class="dropdown-menu">
                      <li><a href="#">Action</a></li>
                      <li><a href="#">Another action</a></li>
                      <li><a href="#">Something else here</a></li>
                      <li class="divider"></li>
                      <li class="nav-header">Nav header</li>
                      <li><a href="#">Separated link</a></li>
                      <li><a href="#">One more separated link</a></li>
                    </ul>
                  </li>
                </ul>
              </div><!--/.nav-collapse -->
            </div>
          </div>
        </div>

        <div class="container">

          <!-- Main hero unit for a primary marketing message or call to action -->
          <div class="hero-unit">
            <h1>Hello, world!</h1>
            <p>This is a template for a simple marketing or informational website. It includes a large callout called the hero unit and three supporting pieces of content. Use it as a starting point to create something more unique.</p>
            <p><a class="btn btn-primary btn-large">Learn more &raquo;</a></p>
          </div>

          <!-- Example row of columns -->
          <div class="row">
            <div class="span6 col1">
              <h2>Heading</h2>
              <p>Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed odio dui. </p>
              <p><a class="btn" href="#">View details &raquo;</a></p>
            </div>
            <div class="span6 col2">
              <h2>Heading</h2>
              <p>Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed odio dui. </p>
              <p><a class="btn" href="#">View details &raquo;</a></p>
           </div>

          <hr>

          <footer>
            <p>&copy; Company 2012</p>
          </footer>

        </div> <!-- /container -->

        <!-- Le javascript
        ================================================== -->
        <!-- Placed at the end of the document so the pages load faster -->
        <script src="/++theme++static/js/jquery.js"></script>
        <script src="/++theme++static/js/bootstrap.min.js"></script>
        <script src="http://platform.twitter.com/widgets.js" type="text/javascript"></script>
        <script type="text/javascript">
            $(document).ready(function() { 
                $('a.lightbox').lightBox();
                $(".client").collapse()
                $('.carousel').carousel({
                    interval: 10000,
                }
                )
            });
        </script>
      </body>
    </html>

Then added some Diazo rules:

.. code-block:: xml

    <rules
        xmlns="http://namespaces.plone.org/diazo"
        xmlns:css="http://namespaces.plone.org/diazo/css"
        xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

        <append css:content="#category" css:theme=".hero-unit" />
        <before content='/html/head/title' theme='/html/head/title' />
        <theme href="index.html" />
        <replace css:content=".nav" css:theme=".nav" />
        <replace css:content="#content" css:theme-children=".hero-unit" />
        <replace css:content="#portal-column-one" css:theme-children=".col1" />
        <replace css:content="#portal-column-two" css:theme-children=".col2" />
        <replace css:content="footer" css:theme="footer" />
        <replace css:content="#portal-logo" css:theme=".brand" />

    </rules>

Then styled to fit with CSS:

.. code-block:: css

    #about {
        padding-top: 9px;    
    }
    .alex {
        border-bottom: 1px solid #FAFAFA;
    }
    body {
        background: url("/++theme++static/img/aclark-net-background.png") repeat-x;
        background-color: black;
    }
    .brand {
        color: #FAFAFA !important;
        font-family: Georgia;
    }
    .brand .alpha {
        font-size: 360%;
        font-style: italic;
    }
    .brand .name {
        font-size: 50px;
    }
    .carousel-inner {
        border-bottom: 1px solid #CCC;
        padding-bottom: 2em;
    }
    #content {
        color: #FAFAFA;
    }
    .description {
        font-size: 125%;
        margin: 1em 0 1em 0;
    }
    .documentDescription {
        font-size: 125%;
        margin: 1em 0 1em 0;
    }
    dt {
        margin: 1em 0 1em 0;
    }
    #facebook {
        padding-top: 1px;    
    }
    footer {
        border-top: 1px solid #999999;
        color: #999999;
        margin-top: 600px;
        width: 100%;
        padding-top: 1em;
    }
    footer li {
        list-style-type: none;
    }
    .hero-unit {
        background: black;
    }
    hr {
        border: none;
        background-color: #CCC;
        color: #CCC;
        height: 1px;
    }
    .image-left {
        float: left;
        margin: 0 1em 0 0;
    }
    .navbar-inner {
        background: #AA001F !important; 
        height: 50px;
    }
    .portletHeader {
        font-size: 125%;
    }
    #portal-column-one {
        color: #FAFAFA;
    }
    #portal-column-two {
        color: #FAFAFA;
    }
    .team-member {
        border-bottom: 1px solid #FAFAFA;
    }
    .service {
        padding: 30px 0 30px 0;
    }
    #twitter {
        padding-top: 15px;
    }


Add content
-----------

I then cut/pasted all my content from the old site to the new site. This is a lot of work, but I like mimicking the experience of someone non-tech-savvy using Plone for the first time.

What's left? 
------------

I am very happy with this upgrade, but of course it's not perfect.

Use Sunburst theme for content editing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you are Diazo-savvy, you may notice I completely ignore styling the content editing interface. Instead I rely on the unthemed [2]_ site for content editing.


.. image:: https://raw.github.com/ACLARKNET/aclarknet.github.com/master/images/edit-ui.png

Use Diazo theme for public facing view
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Of course, visitors to http://aclark.net see the Diazo theme.

.. image:: https://raw.github.com/ACLARKNET/aclarknet.github.com/master/images/diazo-theme.png

I'm hoping that the Plone team can unify the content editing experience again in Plone 5, possibly via simplifying the "old style" templates such that it's easier to map them to custom Diazo themes.

Hightlights
-----------

Lastly, I'll cover some of the remaining highlights.

It works!
~~~~~~~~~

Plone 4.3a1 is remarkably stable. The TinyMCE UI is a bit rough, and the sitemap is broken [3]_, but it works.

The ``All content`` view is awesome
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://raw.github.com/ACLARKNET/aclarknet.github.com/master/images/all-content.png

Contributed by Laurence Rowe for Plone 4, I use the ``All content`` view in two places:

- http://aclark.net/services
- http://aclark.net/team

I love the ability to easily aggregate the contents of pages within a folder.

My deployment is awesome
~~~~~~~~~~~~~~~~~~~~~~~~

I'm really happy with the following trick I used this time around:

- Content is stored in Data.fs (of course) which I've checked into a private repo on bitbucket, and save nightly with an automated commit and push. I'm able to present the site buildout and theme to the public but keep the Data.fs private via git submodules.

Prior to this, the entire site was stored in a private repo on bitbucket. And finally:

- If you load the site, you'll notice the images (configured as static resources) are a bit laggy. I'm a big fan of of CloudFlare and current user via pythonpackages.com, so I'll probably be configuring aclark.net to use it soon too. Once that is done, the site should be lightning fast instead of just really fast.

Like this article and/or my open source work in general? Please `consider supporting me on gittip`_.

.. [1] Some ideas for improving upgrades: 1.) optionally rename portal_skins/custom during the upgrade process. 2.) Include suggestions in the form copy to stage the upgrade away from the current production site. 3.) Report on availability of add-ons compatible with latest version of Plone.

.. [2] Unthemed meaning un-diazo-themed. The content UI is themed with the Sunburst theme "the old way".

.. [3] https://dev.plone.org/ticket/13178

.. _`consider supporting me on gittip`: http://gittip.com/aclark4life
