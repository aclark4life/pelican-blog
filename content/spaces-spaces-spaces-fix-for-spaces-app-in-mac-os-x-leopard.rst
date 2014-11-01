Spaces.. Spaces.. Spaces.. fix for Spaces.app in Mac OS X Leopard
================================================================================

:date: 2008-01-01 19:50
:tags: Plone

Like many `Plone`_ developers, I primarily develop on Mac OS X. Also, like many Plone developers I salivate over, and immediately install any updates to Mac OS X that are released, including Leopard.  Overall, I have been very happy with Leopard, but there is one thing that drives me (and plenty of other people) nuts: the automatic window switching functionality in Spaces. For the unfamiliar, a common feature of UNIX desktops is the ability to easily switch between many different desktops containing many different windows. This feature is commonly referred to as a "desktop pager" or "virtual desktop", but Apple calls it Spaces.

Spaces is a great application, they nearly got it right on the first try. I suspect many of the questionable features were included for the sake of soliciting new would-be power users, and/or to maintain user-friendliness, but some features conflict directly with the ability to "power use". For example, if I'm running a Terminal in Space 1, and I switch to (an empty) Space 2 to open another Terminal, opening the new Terminal (e.g. via Quicksilver, or Spotlight) automatically returns me to Space 1. I now have two terminals in Space 1, which is not what I want. I then have to drag this Terminal to Space 2 which is easy, but annoying. A much better approach would be to allow users to force-open a new application window in the current Space.

`Spaces.. Spaces.. Spaces..`_ \*almost\* makes this happen (via some Dock + code-injection magic). With Spaces.. Spaces.. Spaces.., I can now switch to a new Space and open a new Terminal window, without being automatically taken to another Space running another Terminal. The only catch is the Terminal application has to be "in focus", else the old "wrong" behavior still applies. In other words, switch to a new window, then click on the Terminal icon in the Dock, then open a new Terminal window. Not a bad work-around for my purposes, this allows me to easily open as many Terminals on as many Spaces as I see fit without being "redirected" (read: interrupted).

There are a few downsides: 1. You have to run Spaces.. Spaces.. Spaces..  as root, not convenient for starting on boot (unless applications can be run as services somehow? Or something? :-) 2. I'd like the ability to force-launch a new window for any currently running application in the current Space without having to bring that application into focus.  Spaces.. Spaces.. Spaces.. does not currently provide this functionality. 3. It is for Intel-based Macs only.

I \*really\* hope Apple addresses this issue in a future release, but in the meantime many thanks to the Spaces.. Spaces.. Spaces.. developer!!!  If you are similarly bothered by this behavior in Spaces, I recommend you give Spaces.. Spaces.. Spaces.. a try.

.. _Plone: http://plone.org
.. _Spaces.. Spaces.. Spaces..: http://www.scsc.no/products/spaces-spaces-spaces/
