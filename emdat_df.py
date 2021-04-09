import pandas as pd
import wbdata
from utils import rebase_CPI

class emdat():
    '''A class used to load, clean and manipulate EMDAT data. 

    Args:
        filename (str) : the path to the Excel file to load.

    Attributes:
        data (pd.DataFrame) : returns the EMDAT data in df format.
        countries (list) : returns the unique set of countries contained in the data.
        hazard_types (list) : returns the unique set of hazard types contained in the data.
        n_events (int) : returns the number of individual events contained in the data.
    '''

    def __init__(self,filename):

        cols_dict = {"Year":"year",
        "Country":"country",
        "Dis No":"dis_no",
             "Total Deaths":"deaths",
             "Disaster Group":"disaster_group",
             "Disaster Type":"disaster_type",
             "Disaster Subgroup":"disaster_subgroup",
             "Disaster Subtype":"disaster_subtype",
             "Location":"location",
             "Latitude":"lat",
             "Longitude":"lon",
             "Event Name":"event_name",
             "No Injured":"injured",
             "No Affected":"affected",
             "No Homeless":"homeless",
             "Total Affected":"total_affected",
             "Reconstruction Costs ('000 US$)":"reconstruction_costs",
             "Insured Damages ('000 US$)":"insured_damages",
             "Total Damages ('000 US$)":"total_damages"}

        self.data = pd.read_excel(filename, header = 6).rename(columns = cols_dict)
        self.countries = self.data.country.unique()
        self.disaster_types = self.data.disaster_type.unique()
        self.n_events = self.data.dis_no.nunique()
        
    def disaster_count_timeseries(self, min_year, max_year, countries, disastertype):
        '''
        Summarize the number of disasters for selected period, countries and disaster type.

        Args:
            min_year (int) : start year
            max_year (int) : end year
            countries (list) : countries using EMDAT's unique country names
            disastertype (list) : disaster type using EMDAT's disaster type categorization

        Returns
            pd.Series : annual time series of disaster count (eg. yearly number of flood & storm events in Bulgaria and Romania, 1960-2000).
        '''
        df = self.data
        if type(countries) == str: countries = [countries]
        if type(disastertype) == str: disastertype = [disastertype]

        if min_year and max_year:
            df = df[(df.year > min_year) & (df.year < max_year)]
            
        if countries == ['all'] or not countries:
            pass
        else:
            df = df[df.index.isin(countries)]

        if disastertype == ['all'] or not disastertype:
            pass
        else:
            df = df[df['disaster_type'].isin(disastertype)]

        result = df.groupby(['year','disaster_type'])['dis_no'].count()
        result = result.unstack().fillna(0)
            
        return(result)
    
    def disaster_stats_entire_period(self, min_year, max_year, countries, disastertype, stats):
        '''
        EMDAT summary grouped by disaster type: breakdown for entire period.

        Args:
            min_year (int) : start year
            max_year (int) : end year
            countries (list) : countries using EMDAT's unique country names
            disastertype (list) : disaster type using EMDAT's disaster type categorization
            stats (list) : statistic to use (``deaths, injured, affected, total_affected, homeless, reconstruction_costs, insured_damages, total_damages``)

        Returns
            pd.Series : breakdown of selected disaster statistic for selected period (eg. people affected by flood, storm and earthquake in Pakistan for overall period 2000-2010).
        '''
        df = self.data
        if type(countries) == str: countries = [countries]
        if type(disastertype) == str: disastertype = [disastertype]

        if min_year and max_year:
            df = df[(df.year > str(min_year)) & (df.year < str(max_year))]
            
        if countries == ['all'] or not countries:
            pass
        else:
            df = df[df.country.isin(countries)]

        if disastertype == ['all'] or not disastertype:
            pass
        else:
            df = df[df['disaster_type'].isin(disastertype)]

        result = df.groupby(['disaster_type'])[stats].sum()[stats]
        result = result.fillna(0)[stats]
        result = result.sort_values(by = stats, ascending = False)

        return(result)

    def disaster_stats_timeseries(self, min_year, max_year, countries, disastertype, stats):
        '''
        EMDAT summary grouped by disaster type: annual time series.

        Args:
            min_year (int) : start year
            max_year (int) : end year
            countries (list) : countries using EMDAT's unique country names
            disastertype (list) : disaster type using EMDAT's disaster type categorization
            stats (list) : statistic to use (``deaths, injured, affected, total_affected, homeless, reconstruction_costs, insured_damages, total_damages``)

        Returns
            pd.Series : annual time series of disaster count (eg. USD damages from flood, storm and earthquake in Latin American countries each year from 1960-2000.)
        '''
        df = self.data

        if type(countries) == str: countries = [countries]
        if type(disastertype) == str: disastertype = [disastertype]

        if min_year and max_year:
            df = df[(df.year > min_year) & (df.year < max_year)]
            
        if countries == ['all'] or not countries:
            pass
        else:
            df = df[df.country.isin(countries)]

        if disastertype == ['all'] or not disastertype:
            pass
        else:
            df = df[df['disaster_type'].isin(disastertype)]

        result = df.groupby(['year','disaster_type'])[stats].sum()
        result = result.unstack().fillna(0)
            
        return(result)

    def country_stats_entire_period(self, min_year, max_year, countries, disastertype, stats):
        '''
        EMDAT summary grouped by country: breakdown for entire period.

        Args:
            min_year (int) : start year
            max_year (int) : end year
            countries (list) : countries using EMDAT's unique country names
            disastertype (list) : disaster type using EMDAT's disaster type categorization
            stats (list) : statistic to use (``deaths, injured, affected, total_affected, homeless, reconstruction_costs, insured_damages, total_damages``)

        Returns
            pd.DataFrame : country breakdown of selected disaster statistics, total for period (eg. Nicaragua, Honduras and Belize USD flood damage, 2000-2020). '''
        df = self.dat
        if type(countries) == str: countries = [countries]
        if type(disastertype) == str: disastertype = [disastertype]

        if min_year and max_year:
            df = df[(df.year > min_year) & (df.year < max_year)]
            
        if countries == ['all'] or not countries:
            pass
        else:
            df = df[df.country.isin(countries)]

        if disastertype == ['all'] or not disastertype:
            pass
        else:
            df = df[df['disaster_type'].isin(disastertype)]

        result = df.groupby(['country'])[stats].sum()[stats]
        result = result.unstack().fillna(0)
            
        return(result)

    def country_stats_timeseries(self, min_year, max_year, countries, disastertype, stats):
        '''
        EMDAT summary grouped by country: annual time series.

        Args:
            min_year (int) : start year
            max_year (int) : end year
            countries (list) : countries using EMDAT's unique country names
            disastertype (list) : disaster type using EMDAT's disaster type categorization
            stats (list) : statistic to use (``deaths, injured, affected, total_affected, homeless, reconstruction_costs, insured_damages, total_damages``)

        Returns
            pd.DataFrame : annual time series of disaster statistics grouped by country (eg. Pakistan and India flood, storm and earthquake USD damages each year, 1980-2020)
        '''
        df = self.data
        if type(countries) == str: countries = [countries]
        if type(disastertype) == str: disastertype = [disastertype]

        if min_year and max_year:
            df = df[(df.year > min_year) & (df.year < max_year)]
            
        if countries == ['all'] or not countries:
            pass
        else:
            df = df[df.country.isin(countries)]

        if disastertype == ['all'] or not disastertype:
            pass
        else:
            df = df[df['disaster_type'].isin(disastertype)]

        result = df.groupby(['year','country'])[stats].sum()
        result = result.unstack().fillna(0)
            
        return(result)

    def disaster_stats_total_for_period(self, min_year, max_year, countries, disastertype, stats):
        '''
        Single total for a given statistic.

        Args:
            min_year (int) : start year
            max_year (int) : end year
            countries (list) : countries using EMDAT's unique country names
            disastertype (list) : disaster type using EMDAT's disaster type categorization
            stats (list) : statistic to use (``deaths, injured, affected, total_affected, homeless, reconstruction_costs, insured_damages, total_damages``)

        Returns
             float : total for selected disaster statistic (eg. total people affected by earthquake in Pakistan, 1960-2020).
        '''
        df = self.data

        if type(countries) == str: countries = [countries]
        if type(disastertype) == str: disastertype = [disastertype]

        if min_year and max_year:
            df = df[(df.year > min_year) & (df.year < max_year)]
            
        if countries == ['all'] or not countries:
            pass
        else:
            df = df[df.country.isin(countries)]

        if disastertype == ['all'] or not disastertype:
            pass
        else:
            df = df[df['disaster_type'].isin(disastertype)]

        return(df[stats].sum()[0])

    def aal_by_disaster_type(self, min_year, max_year, countries, disastertype, base_year = 2010,damage_type = 'total_damages'):
        # aal is total loss divided by number of years (but ignore years with no loss)
        damage_by_hazard_df=self.disaster_stats_timeseries(min_year, max_year, countries, disastertype,stats=damage_type)
        damage_by_hazard_real = damage_by_hazard_df.apply(rebase_CPI, axis=0, args=[base_year])
        aal_series = damage_by_hazard_real.sum() / (damage_by_hazard_real.index.max() - damage_by_hazard_real.index.min())
        return(aal_series.astype(int).sort_values(ascending=False))

    def filter_years(self, min_year, max_year):
        '''Filter data by start and end year'''
        df = self.data
        return df[(df.year > str(min_year)) & (df.year < str(max_year))]
    
    def filter_countries(self, countries):
        '''Filter data by country'''
        df = self.data
        return df[df.index.isin(countries)]
    
    def filter_disastertype(self, disastertype):
        '''Filter data by disaster type'''
        df = self.data
        return df[df['disaster_type'].isin(disastertype)]



