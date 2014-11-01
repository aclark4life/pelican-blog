Placeful Theming
================================================================================

:date: 2008-06-02 07:02
:tags: Plone

I had to do a bit of placeful theming lately and I thought I would share the techniques I used (thanks davisagli, jonbaldievieso, vedawms). Let's say you have a Plone 3 site, and for some location /foo/bar/baz, you want 'baz' and everything below it to look different. I made this change through the web because I was in a hurry, but the same can be done in filesystem code.

The steps are:

1. Override getSectionFromURL (navigate to portal\_skins/plone\_scripts/getSectionFromURL and customize)
--------------------------------------------------------------------------------------------------------

Normally, this bit of code returns the section id for whatever section you are in. So if your site has three top level folders A, B, C, getSectionURL returns section-A when you are inside of A, section-B when you are inside of B, and so on. However, when you are inside of a sub-section, e.g. /A/news-items-folder, it \*still\* returns the section id, in this case section-A. The override makes getSectionURL return the sub-section, e.g. /A/news-items-folder, or /foo/bar/baz.

::

    # Courtesy of jonb at onenw.org# getSectionFromURLcontentPath = context.portal_url.getRelativeContentPath(context)if not contentPath:    return Noneelse:    s = ''    sectionId = ''    for pathItem in contentPath:        sectionId += pathItem + '-'        s += 'section-' + sectionId[:-1] + ' '    return s[:-1]

2. Override plone.logo (navigate to /portal\_view\_customizations/zope.interface.interface-plone.logo and customize)
--------------------------------------------------------------------------------------------------------------------

For some reason (good or not, I don't know) Plone includes an image tag in the html code it uses to generate the Plone logo. This means that it will always output something like:

::

    img src="logo.jpg"

which is a problem if you want to placefully replace the logo because there is no easy way to do it (perhaps you could use some trick to return a different image file with the same file name).

Plone ships with:

::

    <a metal:define-macro="portal_logo"   id="portal-logo"   accesskey="1"   tal:attributes="href view/navigation_root_url"   i18n:domain="plone">    <img src="logo.jpg" alt=""         tal:replace="structure view/logo_tag" /></a>

Replace that with:

::

    <div metal:define-macro="portal_logo" id="portal-logo">    <a accesskey="1"       tal:attributes="href view/navigation_root_url"       i18n:domain="plone"></a></div>

3. Add CSS (Navigate to /portal\_skins/plone\_styles/ploneCustom.css and customize)
-----------------------------------------------------------------------------------

Next, add in some CSS to make use of the previous two changes:

::

    body.section-foo-bar-baz {    background-image: url(gradient.png);}.section-foo-bar-baz #portal-globalnav li a {    border: 0px;    background: #0066CC;    color: white;    font-size: 110%;    font-face: bold;}.section-foo-bar-baz #portal-globalnav {    background: #0066CC;    padding: 0.25em;}.section-foo-bar-baz #portal-breadcrumbs,.section-foo-bar-baz #portal-personaltools {    background: white;}.section-foo-bar-baz #portal-top {     background: white;}.section-foo-bar-baz #portal-logo {     margin: 1em;    background-image: url(ama_logo.gif);    background-repeat: no-repeat;}.section-foo-bar-baz #visual-portal-wrapper {     background: white;    margin: auto;    width: 883px;    position: relative;}.section-foo-bar-baz body {     background-image: url(gradient.png);    background-repeat: repeat;}#portal-logo {     margin: 1em;    background-image: url(logo.jpg);    background-repeat: no-repeat;}#portal-logo a {     display: block;    width: 650px;    height: 80px;}

I hope this helps someone get started with placeful theming.

