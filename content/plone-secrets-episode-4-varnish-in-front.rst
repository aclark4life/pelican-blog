Plone secrets: Episode 4 - Varnish in front
###########################################
:date: 2011-11-09 12:50
:tags: Plone

*This just in from the production department: use Varnish. (And please
forgive the heavily meme-laden approach to describing these techniques
:-).)*

Cache ALL the hosts
-------------------

`|image0|`_\ Our ability to use Varnish in production is no secret by
now, or at least it shouldn't be. What is often less clear is exactly
how to use it. One way I like[1], is to run Varnish on your public IP
port 80 and make Apache listen on your private IP port 80. Then proxy
from Varnish to Apache and enjoy easy caching goodness on all your
virtual hosts in Apache.

Configuration
-------------

This should require less than five minutes of down time to implement.
First, configure the appropriate settings. (Well, first install Apache
and Varnish if you haven't already: \`aptitude install varnish apache2\`
on Ubuntu Linux[0].)

Varnish
~~~~~~~

To modify the listen IP address and port, we typically edit a file like
*/etc/default/varnish* (in Ubuntu). However you do it, configure the
equivalent of the following on your system:

::

    DAEMON_OPTS="-a 174.143.252.11:80 
                 -T localhost:6082 
                 -f /etc/varnish/default.vcl 
                 -s malloc,256m"

This environment variable is then passed to *varnishd* on the command
line. Next, pass traffic to Apache like so (in
*/etc/varnish/default.vcl* on Ubuntu):

::

    backend default {
     .host = "127.0.0.1";
     .port = "80";
     }

Now on to Apache.

.. raw:: html

   </p>

***Please note that the syntax above is for Varnish 3.x and the syntax
has (annoyingly) changed from 2.x to 3.x.***

Apache
~~~~~~

The Apache part is a bit simpler. You just need to change the listen
port (on Ubuntu this is done in */etc/apache2/ports.conf*), typically
from something like:

::

    Listen *:80

to:

::

    Listen 127.0.0.1:80

Restart ALL the services
------------------------

Now restart both services. If all goes well you shouldn't notice any
difference, except better performance, and when you make a website
change and need to clear the cache[2]. For this, I rely on telnetting to
the varnish port and issuing the \`ban.url\` command (formerly
\`url.purge\` in 2.x):

::

    $ telnet localhost 6082
    Trying 127.0.0.1...
    Connected to localhost.
    Escape character is '^]'.
    200 205     
    -----------------------------
    Varnish Cache CLI 1.0
    -----------------------------
    Linux,2.6.35.4-rscloud,x86_64,-smalloc,-smalloc,-hcritbitType 'help' for command list.
    Type 'quit' to close CLI session.ban.url /
    200 0

Cache ALL the disks
-------------------

This site has Varnish and Apache configured as described in this
article. It also has disk caching in Apache enabled, thanks to Elizabeth
Leddy's article:

-  `http://plonechix.blogspot.com/2011/08/10-minute-caching-with-apache.html`_

As a result, it's **PEPPY AS THE DICKENS™** on a 512MB "slice" (Cloud
server) from Rackspace Cloud. And now you know yet another "Plone
secret". Now go make your Plone sites faster, and let me know how it
goes in the comments section below.

Notes
-----

[0] Using the latest distribution, "oneric".

.. raw:: html

   </p>

[1] I first saw this technique at NASA when NASA Science was powered by
Plone; I found it odd at the time but years later it makes perfect
sense.

[2] Ideally you'd configure this in p.a.caching, but I've not been able
to stomach this yet.

 

.. _|image1|: http://memegenerator.net/cache/instances/400x/10/11036/11301169.jpg
.. _`http://plonechix.blogspot.com/2011/08/10-minute-caching-with-apache.html`: http://plonechix.blogspot.com/2011/08/10-minute-caching-with-apache.html

.. |image0| image:: http://aclark4life.files.wordpress.com/2011/11/11301169.jpg
.. |image1| image:: http://aclark4life.files.wordpress.com/2011/11/11301169.jpg
