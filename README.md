# pyEmdat - efficient analysis of natural disaster data

pyEmdat is a library for analysis of the EM-DAT natural disasters dataset. It allows to:

* Load and clean EMDAT data

* Summarize disaster statistics by country (single time period & annual time series)

* Summarize disaster statistics by hazard type (single time period & annual time series)

* Combine with population and GNI data (via World Development Indicators API)

## Background: EM-DAT data
EM-DAT is a global database of natural disaster events and impacts maintained by the Centre for Research on the Epidemiology of Disasters (CRED) at Université catholique de Louvain. It is used widely to inform policy-making on disaster risk management: for example, it helps policymakers identify the disaster types that are most common in a given country and that have had significant historical impacts on human populations.

Researchers can access EM-DAT through CRED's website: http://public.emdat.be. The data can be downloaded by researchers in Excel format (having created an account and agreed to applicable conditions). pyEmdat makes analysis easier as researchers were rewriting the required functionality each time or using Excel.

## Getting started
First, download EM-DAT data which comes in Excel format. Abide by all terms and conditions of CRED including downloading only the data you need.
Second, create an ``emdat`` object
```python
from emdat_df import emdat
ED = emdat('home/data/my_EMDAT_download.xlsx')
```
Third, use `emdat`'s built-in methods to filter, group and aggregate the data.
Fourth, use the built-in `utils` to compare natural disaster impacts with population and GNI data from World Development Indicators.

## Examples
See example notebook for usage.

## Quick examples

Load EM-DAT data as above, then:

```python
df = ED.disaster_count_timeseries(1960, 2000, countries = 'all', disastertype = ['Storm','Flood', 'Earthquake','Volcanic activity','Landslide'])
df.plot(title = 'World: Number of events by year');
```

Output:

![world number of events](/docs/world_events.png)

```python
df = ED.country_stats_timeseries(1980, 2020, ['Georgia','Armenia','Azerbaijan'],'all','total_damages')
df.plot.area(title = "South Caucasus: Total damages 1980 - present (all hazards, current USD '000)");
```

Output:

![damage South Caucasus](/docs/damage_caucasus.png)

## Documentation
Documentation for pyEmdat is available at: https://pyemdat.readthedocs.io/en/latest/

## Functionality to add
* Merge with country polygons to make choropleth maps
* Damage stats in real 2010 USD
* Annual average loss for selected countries/hazards/period (real 2010 USD)
* Possible additional data structure for Desinventar data
