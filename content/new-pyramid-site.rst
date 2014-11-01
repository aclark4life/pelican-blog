New Pyramid Site
================

:date: 2013-04-22 12:00
:tags: Django, Mozilla, Plone, Python

.. image:: https://raw.github.com/ACLARKNET/aclarknet/master/screenshot.png
    :width: 98%
    :alt: alternate text

For the first time in 10 years, `aclark.net <http://aclark.net>`_ is not powered by Plone. Nothing against Plone: it's still one of the greatest loves of my life (inasmuch as you can love a software and community, as I do).

Why
---

This was not the result of a revolutionary plan, rather more of an evolution. It happened like this:

- As soon as Plone 4.3a1 was released (a year ago?) I deployed a new Plone site to aclark.net with it, featuring a **Diazo** (new Plone theming engine) theme.
- Around the same time I became obsessed with deploying to Heroku, and also gained an interest in **Python 3**.
- A few months ago, I got tired of paying $11/month to host my Plone site so I converted the site to **static HTML** and moved it to **GitHub pages**. But the result was flawed because maintenance involved editing duplicate copies of the website content (e.g. both clients.html and clients/foo.html contained the same text describing "foo").

So when it came time to do more than a few casual edits, I knew I had to find a new approach. That's when various elements of the Universe conspired to lead me in a new direction.

How
---

Pyramid
~~~~~~~

I spent a lot of time (~ 1 year) developing `pythonpackages.com <http://pythonpackages.com>`_ in Pyramid, but the result was a mess (code-wise). I'm in the process of rewriting and open sourcing it, but it's slow going. So what better way to get started than to do a small-ish site in Pyramid for fun?

about.me
~~~~~~~~

I also recently gave in and created an `about.me site <http://about.me/alex.clark>`_. I was impressed by their content editing features, and my ability to create a page that looked OK using them.

In my about.me profile, I used a picture of me and a picture of DC I took in early 2012. When it came time to redo aclark.net I felt like I really wanted to capture the simplicity of the about.me site, so I used the same photo in the background.

Bootstrap
~~~~~~~~~

Bootstrap is old news at this point, but I really enjoy using it and I particularly like that they have added more example templates. So I combined my background photo with one of `their example templates <http://twitter.github.io/bootstrap/getting-started.html#examples>`_ and a new site idea was born. As I'm not a particularly talented visual artist, my ability to produce something that looked OK (with code this time) was exciting.

What
----

Until I added a contact form, the site was entirely unremarkable. There are views and routes and templates, typical fare for a web framework. Here is the entire "main routine"::

    from pyramid.session import UnencryptedCookieSessionFactoryConfig
    from pyramid.config import Configurator
    from .redir import blog
    from .redir import blog_entry
    from .redir import blog_slash
    from .views import contact
    from .views import default
    import deform_bootstrap


    def main(global_config, **settings):
        """
        Oppan wsgi style! Configure and return WSGI application.
        """
        my_session_factory = UnencryptedCookieSessionFactoryConfig('itsaseekreet')
        config = Configurator(session_factory=my_session_factory)
        config.add_route('blog', '/blog')
        config.add_route('blog_entry', '/blog/{entry:.*}')
        config.add_route('blog_slash', '/blog/')
        config.add_route('contact', '/contact')
        config.add_route('clients', '/clients')
        config.add_route('projects', '/projects')
        config.add_route('services', '/services')
        config.add_route('team', '/team')
        config.add_route('testimonials', '/testimonials')
        config.add_route('root', '/')
        config.add_static_view(
            'static', 'aclarknet:static', cache_max_age=3600)
        config.add_view(blog, route_name='blog')
        config.add_view(blog_entry, route_name='blog_entry')
        config.add_view(blog_slash, route_name='blog_slash')
        config.add_view(
            default,
            renderer='aclarknet:templates/clients.mak',
            route_name='clients')
        config.add_view(
            contact,
            renderer='aclarknet:templates/contact.mak',
            route_name='contact')
        config.add_view(
            default,
            renderer='aclarknet:templates/projects.mak',
            route_name='projects')
        config.add_view(
            default,
            renderer='aclarknet:templates/root.mak',
            route_name='root')
        config.add_view(
            default,
            renderer='aclarknet:templates/services.mak',
            route_name='services')
        config.add_view(
            default,
            renderer='aclarknet:templates/testimonials.mak',
            route_name='testimonials')
        config.add_view(
            default,
            renderer='aclarknet:templates/team.mak',
            route_name='team')
        config.include(deform_bootstrap)
        return config.make_wsgi_app()

Contact form
~~~~~~~~~~~~

But then I wanted a contact form. Which lead me to wanting an elegant way to send mail via Heroku. Which lead me to discover `SendGrid <http://sendgrid.com/>`_. Which lead me create some primitive marketing features I am quite proud of and excited about.

I still ended up sending mail "the old way" via GMail. But now I send two mails: one to info@aclark.net to alert our staff about the lead (using GMail). And one to the lead acknowledging their submission (using SendGrid). SendGrid keeps a record of all the leads we've contacted, amongst other "fancy marketing features". Here's the relevant view code::

    import deform
    import smtplib

    from email.mime.text import MIMEText

    from .config import FORM_ERROR
    from .config import FORM_SUCCESS

    from .config import MIME_ONE_RECIPIENT
    from .config import MIME_ONE_SUBJECT
    from .config import MIME_TWO_MESSAGE
    from .config import MIME_TWO_SUBJECT

    from .config import GMAIL_HOSTNAME
    from .config import GMAIL_PASSWORD
    from .config import GMAIL_USERNAME

    from .config import SENDGRID_HOSTNAME
    from .config import SENDGRID_PASSWORD
    from .config import SENDGRID_USERNAME

    from .forms import ContactFormSchema


    def contact(request):
        """
        Create and render deform form containing colander schema. Provide
        sendgrid integration for marketing.
        """
        button = deform.Button('Send', css_class='span9 btn-block btn-large')
        schema = ContactFormSchema().bind(request=request)
        form = deform.Form(schema, buttons=(button, ))
        if 'Send' in request.POST:
            items = request.POST.items()
            try:
                appstruct = form.validate(items)
            except deform.ValidationFailure:
                return {
                    'form': form.render(),
                    'request': request,
                }
            # This is the form contents
            email = appstruct['email']
            message = appstruct['message']

            # This is the mail to info@aclark.net
            mime_document_one = MIMEText(message)
            mime_document_one['Subject'] = MIME_ONE_SUBJECT
            mime_document_one['To'] = MIME_ONE_RECIPIENT
            mime_document_one['From'] = email
            mime_document_one = mime_document_one.as_string()

            # This is the mail to the new lead
            mime_document_two = MIMEText(MIME_TWO_MESSAGE)
            mime_document_two['Subject'] = MIME_TWO_SUBJECT
            mime_document_two['To'] = email
            mime_document_two['From'] = MIME_ONE_RECIPIENT
            mime_document_two = mime_document_two.as_string()

            try:
                # This is the mail to info@aclark.net
                smtp_server = smtplib.SMTP(GMAIL_HOSTNAME)
                smtp_server.starttls()
                smtp_server.login(GMAIL_USERNAME, GMAIL_PASSWORD)
                smtp_server.sendmail(email, MIME_ONE_RECIPIENT, mime_document_one)
                smtp_server.quit()

                # This is the mail to the new lead
                smtp_server = smtplib.SMTP(SENDGRID_HOSTNAME)
                smtp_server.starttls()
                smtp_server.login(SENDGRID_USERNAME, SENDGRID_PASSWORD)
                smtp_server.sendmail(MIME_ONE_RECIPIENT, email, mime_document_two)
                smtp_server.quit()
                request.session.flash(FORM_SUCCESS)
            except:
                request.session.flash(FORM_ERROR, 'errors')
            return {
                'form': form.render(appstruct={}),
                'request': request,
            }
        return {
            'form': form.render(),
            'request': request,
        }


    def default(request):
        """
        This is the default view, to be used with most routes since we do not
        provide any content editing ability yet. Even then, maybe a default view
        would still be helpful.
        """
        return {}

Who cares
---------

The best thing about all of this being able to run the site **100% for free on Heroku**. Also:

- Python 3 compat!
- Free caching via CloudFlare
- Free ping service from Pingdom keeps the site from "going to sleep" (HT: natea).
- Updating the site fits my workflow. If I'm the content editor, I don't necessarily need or want to use Plone to edit my content. I can save Plone for my clients, and focus on **what makes them happy** with their CMS system.
