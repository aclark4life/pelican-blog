Matplotlib Plotting Cookbook Review
===================================

:date: 2014-05-19 14:00
:tags: Django, Mozilla, Plone, Python

*I was given a copy of* `Matplotlib Plotting Cookbook by Alexandre Devert <http://www.packtpub.com/matplotlib-plotting-cookbook/book>`_ *and asked to review it. Thanks PACKT!* *Here is my review.*

Preface
-------

But first, I'll mention I've worked on two projects recently that involved rendering matplotlib graphs directly to the browser i.e. via content-type: image/png. This is fun! It's particularly enjoyable when you are trying to avoid performing the task "the right way", which is arguably outputting JSON to some JavaScript graphing library e.g. `Highcharts <http://www.highcharts.com/>`_. The dependencies are heavy i.e. pip install numpy, etc. but not *that* heavy and once they are installed, **your web application can output graphs rivaling those produced by JavaScript, all written in Python** [1]_. Highly recommended!

Chapter 1
---------

I think the code examples in Chapter 1 alone are worth the price of admission. Here is a video of me walking through the Chapter 1 code examples:

.. raw:: html

    <iframe width="420" height="315" src="//www.youtube.com/embed/YOFHkszsdR8" frameborder="0" allowfullscreen></iframe>

You'll notice the typical fare here: bar, line and pie graphs along with some more complex boxplot, histogram, horizontal bar, scatter and triangle graphs, all in various colors. For reference, here are the excerpted commands called to produce these graphs:

.. raw:: html

    <script src="https://gist.github.com/aclark4life/0f9e61f2d62a67c31346.js"></script>

Chapter 2
---------

Chapter 2 is all about customization e.g. via matplotlibrc. Here is a video of me walking through the Chapter 2 code examples:

.. raw:: html

    <iframe width="420" height="315" src="//www.youtube.com/embed/BzGv1soDaRU" frameborder="0" allowfullscreen></iframe>

For reference, here is the sample matplotlibrc included with the matplotlib distribution (lib/python2.7/site-packages/matplotlib/mpl-data/matplotlibrc):

.. raw:: html

    <script src="https://gist.github.com/aclark4life/71c1edf815bd61aae8a9.js"></script>

As you can see, there are a lot of knobs you can turn here.

Chapter 3
---------

Chapter 3 is all about "annotations". Here is a video of me walking through the Chapter 3 code examples:

.. raw:: html

    <iframe width="420" height="315" src="//www.youtube.com/embed/994vecwODaI" frameborder="0" allowfullscreen></iframe>

"Annotations" includes related topics such as adding shapes and controlling tick spacing and labeling.

Chapter 4
---------

Chapter 4 is all about "working with figures". Here is a video of me walking through the Chapter 4 code examples:

.. raw:: html

    <iframe width="420" height="315" src="//www.youtube.com/embed/Q6PFBSxkOc4" frameborder="0" allowfullscreen></iframe>

"Working with figures" includes obvious topics like ``subplot`` and less obvious topics like setting the aspect ratio.

Chapter 5
---------

Chapter 5 is all about "working with file output". For reference, here are some of the images produced by the examples in this chapter (I wrote ``jpg`` files instead of ``png`` files due to a problem with my libpng: `RuntimeError: Could not create write struct <https://www.google.com/#q=RuntimeError%3A+Could+not+create+write+struct&safe=off>`_.)

.. image:: http://blog.aclark.net/images/sinc1.jpg
    :alt: alternate text

.. image:: http://blog.aclark.net/images/sinc3.jpg
    :alt: alternate text

Also covered in this chapter is `pdf output <http://blog.aclark.net/images/sinc.pdf>`_.

Chapter 6
---------

Chapter 6 is all about "working with maps".

.. raw:: html

    <iframe width="420" height="315" src="//www.youtube.com/embed/gKnR7IfNSsI" frameborder="0" allowfullscreen></iframe>

This chapter also introduces the `imshow command <http://matplotlib.org/1.3.1/users/image_tutorial.html>`_.

Chapter 7
---------

Chapter 7 is all about "working with 3D figures".

.. raw:: html

    <iframe width="420" height="315" src="//www.youtube.com/embed/7YFGHG62L5U" frameborder="0" allowfullscreen></iframe>

For reference, here are the excerpted commands called to produce these graphs:

.. raw:: html

    <script src="https://gist.github.com/aclark4life/6f7f3fd18ec4c7795028.js"></script>

Chapter 8
---------

Chapter 8 is all about working with the "user interface" interactively.

.. raw:: html

    <iframe width="420" height="315" src="//www.youtube.com/embed/k6984I_YGo4" frameborder="0" allowfullscreen></iframe>

Additionally, all of the popular graphical windowing environments are discussed: Tkinter, wxWidgets, GTK, Pyglet (three out of four of which I was able to install; GTK 2 vs GTK 3 `confused me and I ran out of time debugging it <https://www.google.com/#q=from+gi.repository+import+Gtk&safe=off>`_.

Conclusion
----------

Overall I enjoyed this book and would `recommend buying it <http://www.packtpub.com/matplotlib-plotting-cookbook/book>`_.

(*You should probably* `hire me <http://aclark.net>`_ *or* `follow me on Twitter <http://twitter.com/aclark4life>`_ *or both*. *And speaking of PACKT, you should definitely* `buy my book too <http://blog.aclark.net/2011/05/10/top-10-reasons-plone-33-site-admin-book-is-still-for-you/>`_.)

.. [1] Yes, I'm familiar with `Bokeh <http://bokeh.pydata.org/>`_.

