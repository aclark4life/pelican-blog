New vanity release
##################
:date: 2012-01-30 09:52
:category: Plone, Python

With all the Python `stats`_ `goodness`_ going on recently, I got
inspired to make a new `vanity`_ release. This release features the
ability to display per package download statistics via the \`-v\` or
\`--verbose\` command line argument.

Here are some of my favorite results.

Vanity
------

::

    $ vanity vanity -v
         vanity-1.0.zip     2011-04-14      352
       vanity-1.1.0.zip     2011-10-26      139
       vanity-1.1.1.zip     2011-10-28      114
       vanity-1.1.2.zip     2011-10-28      145
    vanity-1.2.0.tar.gz     2012-01-30        0
    -------------------------------------------
    Package `vanity` has been downloaded 750 times!

Django
------

::

    $ vanity django -v
    Django-1.1.3.tar.gz     2010-12-23    2,618
    Django-1.1.4.tar.gz     2011-02-09    4,476
      Django-1.2.tar.gz     2010-05-17   15,876
    Django-1.2.1.tar.gz     2010-05-24   65,120
    Django-1.2.2.tar.gz     2010-09-09    2,467
    Django-1.2.3.tar.gz     2010-09-11   73,984
    Django-1.2.4.tar.gz     2010-12-23   49,904
    Django-1.2.5.tar.gz     2011-02-09   63,977
    Django-1.2.6.tar.gz     2011-09-10      427
    Django-1.2.7.tar.gz     2011-09-11    6,825
      Django-1.3.tar.gz     2011-03-23  238,504
    Django-1.3.1.tar.gz     2011-09-10  176,054
    -------------------------------------------
    Package `Django` has been downloaded 700,232 times!

Plone
-----

::

    $ vanity plone -v
         Plone-3.2.zip     2008-12-31    1,690
       Plone-3.2.1.zip     2009-02-04    2,466
       Plone-3.2.2.zip     2009-03-03    4,893
       Plone-3.2.3.zip     2009-06-20    2,731
       Plone-3.2a1.zip     2008-10-10      976
      Plone-3.2rc1.zip     2008-12-15      758
         Plone-3.3.zip     2009-08-19    4,611
       Plone-3.3.1.zip     2009-09-09    4,148
    Plone-3.3.2.tar.gz     2009-11-03    3,043
       Plone-3.3.3.zip     2009-12-08    1,733
       Plone-3.3.4.zip     2010-01-14    4,906
       Plone-3.3.5.zip     2010-03-03   12,131
    Plone-3.3.6.tar.gz     2011-07-19      787
       Plone-3.3b1.zip     2009-03-12      940
      Plone-3.3rc1.zip     2009-03-30      743
      Plone-3.3rc2.zip     2009-04-05    1,822
      Plone-3.3rc3.zip     2009-05-23    2,036
      Plone-3.3rc4.zip     2009-07-07    2,163
      Plone-3.3rc5.zip     2009-08-01    1,211
         Plone-4.0.zip     2010-08-30    3,659
       Plone-4.0.1.zip     2010-10-04    4,224
       Plone-4.0.2.zip     2010-11-22    4,022
       Plone-4.0.3.zip     2011-01-21    3,339
       Plone-4.0.4.zip     2011-03-01    2,711
       Plone-4.0.5.zip     2011-04-09    3,152
       Plone-4.0.6.zip     2011-05-22    1,469
       Plone-4.0.7.zip     2011-06-06    2,192
       Plone-4.0.8.zip     2011-07-17      509
       Plone-4.0.9.zip     2011-07-29      958
      Plone-4.0.10.zip     2011-10-12      495
       Plone-4.0a1.zip     2009-11-19      946
       Plone-4.0a2.zip     2009-12-04      921
       Plone-4.0a3.zip     2009-12-21    1,272
       Plone-4.0a4.zip     2010-02-01    1,121
       Plone-4.0a5.zip     2010-02-19      850
       Plone-4.0b1.zip     2010-03-09    1,308
       Plone-4.0b2.zip     2010-04-10    1,028
       Plone-4.0b3.zip     2010-05-04    1,722
       Plone-4.0b4.zip     2010-06-13    1,642
    Plone-4.0b5.tar.gz     2010-07-08    1,995
      Plone-4.0rc1.zip     2010-08-06    1,598
         Plone-4.1.zip     2011-07-17    4,479
    Plone-4.1.1.tar.gz     2011-09-21      429
    Plone-4.1.2.tar.gz     2011-10-08    2,187
    Plone-4.1.3.tar.gz     2011-11-29    1,883
       Plone-4.1a1.zip     2011-01-21      699
       Plone-4.1a2.zip     2011-02-11      451
       Plone-4.1a3.zip     2011-02-15      680
       Plone-4.1b1.zip     2011-03-08      958
       Plone-4.1b2.zip     2011-04-09    1,040
      Plone-4.1rc2.zip     2011-05-22      797
      Plone-4.1rc3.zip     2011-06-06    1,329
       Plone-4.2a1.zip     2011-08-10      521
       Plone-4.2a2.zip     2011-09-16      884
    Plone-4.2b1.tar.gz     2011-12-06      619
    ------------------------------------------
    Package `Plone` has been downloaded 111,877 times!

Pyramid
-------

::

    $ vanity pyramid -v
       pyramid-1.0.tar.gz     2011-01-31   24,055
     pyramid-1.0.1.tar.gz     2011-08-13      460
     pyramid-1.0.2.tar.gz     2011-12-15      185
     pyramid-1.0a1.tar.gz     2010-11-05    1,128
     pyramid-1.0a2.tar.gz     2010-11-09      952
     pyramid-1.0a3.tar.gz     2010-11-16      803
     pyramid-1.0a4.tar.gz     2010-11-21    1,732
     pyramid-1.0a5.tar.gz     2010-12-15      639
     pyramid-1.0a6.tar.gz     2010-12-16      834
     pyramid-1.0a7.tar.gz     2010-12-20      912
     pyramid-1.0a8.tar.gz     2010-12-27    1,233
     pyramid-1.0a9.tar.gz     2011-01-08    1,313
    pyramid-1.0a10.tar.gz     2011-01-18      960
     pyramid-1.0b1.tar.gz     2011-01-22      871
     pyramid-1.0b2.tar.gz     2011-01-25    1,003
     pyramid-1.0b3.tar.gz     2011-01-28      816
       pyramid-1.1.tar.gz     2011-07-22    5,674
     pyramid-1.1.1.tar.gz     2011-08-13    1,057
     pyramid-1.1.2.tar.gz     2011-08-17    1,560
     pyramid-1.1.3.tar.gz     2011-12-15      160
     pyramid-1.1a1.tar.gz     2011-06-20    1,146
     pyramid-1.1a2.tar.gz     2011-06-23    1,003
     pyramid-1.1a3.tar.gz     2011-06-26    1,252
     pyramid-1.1a4.tar.gz     2011-07-01    1,517
     pyramid-1.1b1.tar.gz     2011-07-10      981
     pyramid-1.1b2.tar.gz     2011-07-13      844
     pyramid-1.1b3.tar.gz     2011-07-15      742
     pyramid-1.1b4.tar.gz     2011-07-18    1,094
       pyramid-1.2.tar.gz     2011-09-13    6,450
     pyramid-1.2.1.tar.gz     2011-09-28   10,357
     pyramid-1.2.2.tar.gz     2011-11-20      322
     pyramid-1.2.3.tar.gz     2011-11-21    3,078
     pyramid-1.2.4.tar.gz     2011-12-06    1,193
     pyramid-1.2.5.tar.gz     2011-12-15      555
     pyramid-1.2.6.tar.gz     2012-01-05      514
     pyramid-1.2.7.tar.gz     2012-01-20      472
     pyramid-1.2a1.tar.gz     2011-08-24      907
     pyramid-1.2a2.tar.gz     2011-08-27      696
     pyramid-1.2a3.tar.gz     2011-08-29    3,268
     pyramid-1.2a4.tar.gz     2011-09-02      593
     pyramid-1.2a5.tar.gz     2011-09-04      840
     pyramid-1.2a6.tar.gz     2011-09-07      602
     pyramid-1.2b1.tar.gz     2011-09-08      493
     pyramid-1.2b2.tar.gz     2011-09-08      700
     pyramid-1.2b3.tar.gz     2011-09-11      674
     pyramid-1.3a1.tar.gz     2011-12-09    1,264
     pyramid-1.3a2.tar.gz     2011-12-14    1,641
     pyramid-1.3a3.tar.gz     2011-12-21    2,716
     pyramid-1.3a4.tar.gz     2012-01-05      675
     pyramid-1.3a5.tar.gz     2012-01-09    2,369
     pyramid-1.3a6.tar.gz     2012-01-20    1,917
    ---------------------------------------------
    Package `pyramid` has been downloaded 97,222 times!

Enjoy the new release.

.. raw:: html

   </p>

.. _stats: http://crate.io/
.. _goodness: http://python3wos.appspot.com/
.. _vanity: http://pythonpackages.com/info/vanity
