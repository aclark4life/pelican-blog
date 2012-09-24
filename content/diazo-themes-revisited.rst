
Diazo themes revisited
======================
:date: 2012-09-24 12:15
:tags: Plone

With Diazo theming on the rise (going in to 4.3 core) I'd like to take a look at the Diazo theming ecosystem again. For that matter, since I know that some folks will never commit to Diazo, I'd like to take a look at the entire Plone theming ecosystem.

What are themes?
----------------

Themes control the way the site looks. For the scope of this post, at least, I don't care about "views", "viewlets", "portlets", "tiles", etc. In fact, I'm not sure I ever want to mix "templating" (for lack of a better word) with theming. There is a bit of discussion going on right now amongst the core developers regarding how to make it easier for themers to associate there template code with application code. And while I fully support this discussion, at present the bottom line is:

- "Old style"[1]_ theming is still a valid way to control the look and feel of a Plone system.
- "New style" (Diazo) theming is a great way to isolote the complexity of the stack and get HTML/CSS/JavaScript folks going quickly (especially in 4.3a1 with the new theme editor!)

Where are themes?
-----------------

In short: all over the place. Why is that? Because we are in the middle of several fluctuating "best practice" approaches that have fluctuated over the past half decade or so:

- Plone developers should release their Plone add-ons [2]_ to PyPI!
- Plone developers should release their Plone add-ons to plone.org (in addition to PyPI)!
- Plone developers should release their Diazo themes as zip archives (i.e. no Python package)!

Hence, the need for this post to clarify the status quo.

What should I do?
-----------------

Everyone should form their own opinion based on the information in this post and act accordingly or however they see fit. If we can all agree on an approach, great! If not, here's what I'm doing.

What am I doing?
~~~~~~~~~~~~~~~~

While I have a large interest in seeing plone.org work well (and am also in the middle of helping to cat herd a plone.com marketing site effort), I have given up on plone.org as a reliable, consistent source for add-ons (in favor of PyPI). This abandonment is perhaps only temporary, but in any event for now: if it's on PyPI, it's good enough for me. Also to close the loop on Diazo zip themes, while I fully support this approach I don't use it myself much.

What is the point?
~~~~~~~~~~~~~~~~~~

All of this brings me to the actual point of this post which is to take a quick look at the Plone themeing landscape in order to spur more Diazo theme development (or old style theming, if that is your thing). Quickly, using pip to search PyPI by package namespace I see:

**88 plonetheme themes**::

    plonetheme.Bangalore      - An installable theme for Plone 3
    plonetheme.GreenEarthTheme3_0 - An installable theme for Plone 3
    plonetheme.ReOrg          - Theme that reorganizes screen real-estate abd gives plone a fresh look
    plonetheme.aclark_twitter - Complete silliness: make your Plone site look like Alex Clark's Twitter profile.
    plonetheme.andreas01      - An installable theme for Plone 3.0.
    plonetheme.andreas02      - 
    plonetheme.aqueouslight   - An installable Diazo theme for Plone 4.1
    plonetheme.bananaleaf     - An installable Diazo theme for Plone 4.1
    plonetheme.basic          - An easily customizable theme for Plone 4
    plonetheme.blueblog       - An installable theme for Plone 3.0
    plonetheme.bluegray       - An installable theme for Plone
    plonetheme.bootstrap      - bootstrap css integration
    plonetheme.broadcaster    - An installable theme for Plone 3.0
    plonetheme.bronzecube     - An installable theme for Plone 3
    plonetheme.burned         - An installable Diazo theme for Plone 4.1
    plonetheme.classic        - The classic Plone 3 default theme.
    plonetheme.cleantheme     - An installable theme for Plone 3.0
    plonetheme.codapress      - An installable Diazo theme for Plone 4.1
    plonetheme.colorcontext   - Total CSS rebuild and color themed sections
    plonetheme.colorfulworld  - An installable theme for Plone 4
    plonetheme.coolblue       - An installable Diazo theme for Plone 4.1
    plonetheme.corporatemale  - An elastic layout presentation suitable for a corporate business.
    plonetheme.criticas       - An installable theme for Plone 3.0
    plonetheme.cultureCab     - An installable theme for Plone 3
    plonetheme.darkened       - An installable Diazo theme for Plone 4.1
    plonetheme.delicious2     - An installable theme for Plone 3.0
    plonetheme.discovery      - An installable Diazo theme for Plone 4.1
    plonetheme.drupal         - Get all the power of Drupal for Plone ;)
    plonetheme.earthlingtwo   - An installable Diazo theme for Plone 4.1
    plonetheme.elemental      - Elemental Plone 4 Theme
    plonetheme.equipoteih     - An installable theme for Plone 3.0
    plonetheme.essay          - 
    plonetheme.evergreen      - An installable Diazo theme for Plone 4.1
    plonetheme.ewb_case       - A Plone 4 theme for EWB Case
    plonetheme.flowerbuds     - UNKNOWN
    plonetheme.freshpick      - An installable Diazo theme for Plone 4.1
    plonetheme.fui            - A Plone 3.0 theme for FUI
    plonetheme.gemstone       - Arcsin's Gemstone web design for Plone4
    plonetheme.gov            - An installable theme for Plone 4
    plonetheme.greencommunity - An installable theme for Plone 3.0.
    plonetheme.grungeera      - An installable Diazo theme for Plone 4.1
    plonetheme.hamnavoe       - An installable theme for Plone 3.0
    plonetheme.html5_hotpink  - Diazo theme for Plone
    plonetheme.inbusiness     - An installable theme for Plone 3.0
    plonetheme.intk           - An installable theme for Plone 3
    plonetheme.intkBase       - An installable theme for Plone 4
    plonetheme.jsjamba        - An installable theme for Plone 4
    plonetheme.keepitsimple   - An installable theme for Plone 4, fluid 3-column theme, minimalistic and light colored design
    plonetheme.laboral        - An installable theme for Plone 4
    plonetheme.labs           - An installable theme for Plone
    plonetheme.leavesdew      - An installable Diazo theme for Plone 4.1
    plonetheme.level2         - An installable theme for Plone 3.0
    plonetheme.lithium        - An installable theme for Plone 3.0
    plonetheme.mimbo          - An installable theme for Plone 3.0 based on the Mimbo theme by Darren Hoyt
    plonetheme.minimalist     - An installable theme for Plone 3.0
    plonetheme.mvob           - An installable Plone4 theme
    plonetheme.nautica05      - An installable theme for Plone 3.x
    plonetheme.netsightintranet - A clean, intranet theme for Plone 3.0
    plonetheme.nonzero        - A theme for Plone 3 based on the Nonzero design by NodeThirtyThree
    plonetheme.notredame      - Theme for Plone 3 with color scheme based on new Plone Logo
    plonetheme.overlappedtabs - A theme for plone 3.x with overlapping tabs
    plonetheme.p2             - An installable theme for Plone 3.0
    plonetheme.peerstheme     - An installable theme for Plone 3.0
    plonetheme.ploneorg       - Plone.org theme
    plonetheme.pollination    - Pollination Theme
    plonetheme.porseleinplaats - An installable theme for Plone 3
    plonetheme.portaltwodotoh - An elastic lounded corners.
    plonetheme.pyar           - A PyAr theme for Plone 3.x
    plonetheme.python         - 
    plonetheme.rcom           - An installable theme for Plone 3.0.
    plonetheme.redmusic       - An installable Diazo theme for Plone 4.1
    plonetheme.relic          - An installable theme for Plone 3.0.
    plonetheme.responsive1140 - A responsive theme for Plone
    plonetheme.responsivetheme - An installable theme for Plone 4 that uses a fluid grid system
    plonetheme.sait2009       - SAIT-2009 installable Plone theme
    plonetheme.simplicity     - An installable theme for Plone 3.0
    plonetheme.solemnity      - An installable theme for Plone 3.0 based on the solemnity theme by Six Shooter Media.
    plonetheme.stylized       - An installable theme for Plone 3.0 based on the stylized theme by NodeThirtyThree.
    plonetheme.subordinate    - An installable theme for Plone 3.0
    plonetheme.sunburst       - The default theme for Plone 4.
    plonetheme.terrafirma     - An installable theme for Plone 3.0
    plonetheme.tidyblog       - An installable theme for Plone 3.0
    plonetheme.transition     - An installable Diazo theme for Plone 4.1
    plonetheme.twinapex       - Twinapex Theme is a theming product for Plone to give your site a professional corporate look
    plonetheme.unilluminated  - An installable Diazo theme for Plone 4.1
    plonetheme.wmoWonen       - An installable theme for Plone 4
    plonetheme.woodexperience - An installable Diazo theme for Plone 4.1
    plonetheme.xtheme         - An installable theme for Plone

**1 diazotheme theme**::

    diazotheme.bootstrap      - Plone theme based on Twitter's Bootstrap CSS

**5 Products themes**::

    Products.Andreas09Theme   - An example theme for Plone 3.0
    Products.HSCustom         - The HSCustom theme was originally created for my band's website.
    Products.naked_plone      - An installable theme for Plone 3.0 that does little but override default public stylesheets with empty ones.
    Products.NuPlone          - A new theme for Plone 3.0
    Products.PloneTableless   - Plone Tableless provides a completly tableless version of the Plone Default theme

**60 other themes (WTF?!)**::

    alterootheme.busycity     - Free City Plone 3.0 Theme
    alterootheme.intensesimplicity - A Plone 3.0 Theme based on a free template by David Uliana
    alterootheme.lazydays     - A Theme for Plone 3.0 based on OpenWebDesign.org Lazy Days theme
    atrealtheme.algol         - An installable theme for Plone 3.0
    atrealtheme.gienah        - An installable theme for Plone 3.0
    beyondskins.ploneday.site - Installable Plone 3 theme for World Plone Day
    beyondskins.ploneday.site2009 - Installable Plone 3 theme developed to promote World Plone Day 2009 (April 22nd)
    beyondskins.ploneday.site2010 - World Plone Day 2010 theme.
    beyondskins.ploneday.site2011 - World Plone Day 2011 theme.
    beyondskins.pyconbrasil2008 - Plone Theme developed by Simples Consultoria
    beyondskins.pythonbrasil.site - This product is a installable Plone 3 Theme developed by Simples Consultoria for use in Python Brasil [7] Conference web site.
    collective.fastview       - View and viewlet helper modules for Plone theme and five.grok developers
    collective.jqueryuithememanager - JQueryUI theme manager for Plone
    collective.lesscss        - This package allow theme developers to add LESS stylesheets into a Plone site.
    collective.phantasy       - dynamic theme for Plone
    collective.responsivetheme - A responsive theme based on sunburst for Plone 4
    collective.shinythings    - Jazz up your Plone theme
    collective.threecolorstheme - A Phantasy theme variation for Plone, with 3 dynamic colors
    cooking.theme             - This is plone theme created from css/html ready design.
    dgsanco.plone3theme       - Plone3 Theme for DG Sanco
    freearch.theme            - Free Arch Theme for Plone
    gameprog.theme            - An installable theme for Plone 3.0
    gomobile.templates        - Project templates creating Web and Mobile themes for Plone
    heddex.cityportal         - Installable theme for Plone
    heddex.greenfield         - An installable theme for Plone 4
    heddex.tranquility        - An installable visual theme for Plone 3
    ilrt.migrationtool        - A site migration tool for Plone that uses the site's theme egg version releases
    iscorpio.themes.redmaple  - iscorpio readmaple Plone 3 theme
    ityou.bluetheme           - An installable theme for Plone 4
    jalon.theme               - An installable theme for Plone 3
    jalonedit.theme           - JalonEdit Theme for PLONE 4
    medialog.kuliadentheme    - An installable theme for Plone 3.0
    medialog.roundskin        - An installable theme for Plone 3
    medialog.subskins         - An installable theme and theming tool for Plone 4
    medialog.subskinsiii      - An installable theme for Plone 3.0
    plone.app.themeeditor     - Theme Editor for Plone, Customize your theme resources
    plone.theme               - Tools for managing themes in CMF and Plone sites
    quintagroup.sunrain.policy - extension for SunRain Plone theme
    quintagroup.theme.estatelite - Free Diazo Theme for Plone 4.1
    quintagroup.theme.lite    - Free Diazo Theme for Plone 4.1
    quintagroup.theme.schools - Free Diazo theme for Plone 4.2
    quintagroup.theme.sunrain - Free Diazo Theme for Plone 4.2
    quintagroup.theme.techlight - Free diazo theme for Plone 4.1
    quintagroup.theme.whiteblack - Free Diazo Theme for Plone 4.1
    quintagroup.themetemplate - Quintagroup theme template for Plone 3 with nested namespace
    raptus.theme.plonebartop  - move the plone-bar on the top
    raptus.theme.ploneformgen - set standard theme for ploneformgen
    redomino.css3theme        - A responsive (and mobile) theme for Plone 4 (based on sunburst)
    sc.paster.theme           - Produto de tema para o portal Plone (skin).
    semicinternet.theme.cambrils - A free Plone theme from SEMIC Internet for Plone 4
    soniatheme                - An installable theme for Plone 3.0
    themetweaker.themeswitcher - A product for switching themes in Plone.
    uofl.dztheme.simplesite   - A Diazo theme for Plone 4 and UofL Simple Left-Nav Sites
    uvsq.theme                - An installable theme for Plone 3
    v2.theme                  - An installable theme for Plone 4
    webcouturier.city.theme   - Plone visual theme
    webcouturier.icompany.theme - Plone theme in blue/green colors
    xdvtheme.inventions       - A xdvtheme for Plone
    xdvtheme.sparkling        - An xdv Theme for Plone
    zettwerk.ui               - Adding jquery.ui's themeroller to plone 4 for easy theme customization.

That last one is a surprise, and that's a total of **154 themes for Plone on PyPI** (assuming I didn't miss any which I probably did). If we had the man power, all of these themes could be made to work with the latest Plone and work with either old style or new style technology. So if we can't do that (which is a hugely ambitious goal) let's at least try to come close!

Do you like this post, and/or appreciate my open source work? Help build the commons by gittiping me: https://www.gittip.com/aclark4life/.

.. raw:: html

    <iframe style="border: 0; margin: 0; padding: 0;"
        src="https://www.gittip.com/aclark4life/widget.html"
        width="48pt" height="20pt"></iframe>

.. [1] It's getting harder to define what "old style" theming is. For this blog entry, old style theming is some form of customizing the main_template in Plone (I'm ignoring the fact that macros called by main_template are customizable, for now). If we could (consistently, in a core supported way) get newer ways to do that (e.g. browser views instead of CMF skin layers) then "old style" would become "newer style". It wouldn't become "new style" because Diazo technology is "newer" than browser view technology. Get it? I think my point is this: in addition to seeing Diazo help with isolating the complexity of the stack, I'd like to see the underlying technology modernized. Give me something that looks and feels like "old style" theming (i.e. putting templates in CMF skin layers) but that is built on modern technology (i.e. the ZCA).

.. [2] <rant> Have I mentioned today yet that I hate the term "product"? when it's used to refer to a Plone add-on? It's 2012 people. Zope 2 products died last decade. :-p :-) </rant>


