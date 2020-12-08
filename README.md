# pyEmdat - efficient analysis of natural disaster data

pyEmdat is a library for analysis of the EM-DAT natural disasters dataset. It allows to:

* Load and clean EMDAT data

* Summarize disaster statistics by country (single time period & annual time series)

* Summarize disaster statistics by hazard type (single time period & annual time series)

* Combine with population and GNI data (via World Development Indicators API)

* Create choropleth maps.

## Documentation
Documentation for pyEmdat is available at: https://pyemdat.readthedocs.io/en/latest/

## Background: EM-DAT data
EM-DAT is a global database of natural disaster events and impacts maintained by the Centre for Research on the Epidemiology of Disasters (CRED) at Université catholique de Louvain. It is used widely to inform policy-making on disaster risk management: for example, it helps policymakers identify the disaster types that are most common in a given country and that have had significant historical impacts on human populations.

Researchers can access EM-DAT through CRED's website: http://public.emdat.be. The data can be downloaded by researchers (having created an account and agreed to applicable conditions). It comes in Excel format. pyEmdat provides a data structure and functions to efficiently load, clean and analyze EM-DAT data.

## Getting started
First, download EM-DAT data which comes in Excel format. Abide by all terms and conditions of CRED including downloading only the data you need.
Second, create an ``emdat`` object
```
from emdat_df import emdat
ED = emdat('home/data/my_EMDAT_download.xlsx')
```
Third, use `emdat`'s built-in methods to filter, group and aggregate the data.
Fourth, use the built-in `utils` to compare natural disaster impacts with population and GNI data from World Development Indicators.

## Examples
See example notebooks for usage.

## Quick example

```python
result = ED.disaster_stats_entire_period(1980, 2020, countries = 'Pakistan', disastertype = 'all', stats = ['total_damages'])
result.head().plot(kind = 'pie', y='total_damages', figsize =[4,4])
plt.title('Pakistan: total USD damages by hazard type (1980-2020)');
```

![damage pie chart](https://github.com/GFDRR/pyEmdat/raw/master/docs/damage_pie.png)

![damage pie chart](/docs/damage_pie.png)
