.. pyEmdat documentation master file, created by
   sphinx-quickstart on Mon Dec  7 22:44:10 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

pyEmdat
=======

pyEmdat is a library for analysis of the EMDAT natural disasters dataset. It allows to:

* Load and clean EMDAT data
* Summarize disaster statistics by country (single time period & annual time series)
* Summarize disaster statistics by hazard type (single time period & annual time series)
* Combine with population and GNI data (via World Development Indicators API)
* Create choropleth maps.

Contents
-------------
.. toctree::
   :maxdepth: 2
   :caption: API reference:

   emdat_df
   utils

Possible extensions
-------------------

* more functions to clean and summarize the dataset.
* converting historical damage data from nominal to real terms (eg. constant 2010 USD).
* additional data structures to load & clean Desinventar or other disaster datasets.

Dependencies
------------

* ``pandas``, ``wbdata`` (required)
* ``geopandas`` (recommended)
