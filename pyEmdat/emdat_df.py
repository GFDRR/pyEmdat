import pandas as pd
import wbdata

class emdat():

    def __init__(self,fn):

        cols_dict = {"Year":"year",
        "Country":"country",
        "Dis No":"dis_no",
             "Total Deaths":"deaths",
             "Disaster Group":"disaster_group",
             "Disaster Type":"disaster_type",
             "Disaster Subgroup":"disaster_subgroup",
             "Disaster Subtype":"disaster_subtype",
             "Event Name":"event_name",
             "No Injured":"injured",
             "No Affected":"affected",
             "No Homeless":"homeless",
             "Total Affected":"total_affected",
             "Reconstruction Costs ('000 US$)":"reconstruction_costs",
             "Insured Damages ('000 US$)":"insured_damages",
             "Total Damages ('000 US$)":"total_damages"}

        self.df = pd.read_excel(fn, header = 6, parse_dates=['Year']).rename(columns = cols_dict)
        print('squawk')
        
    def filter_years(self, min_year, max_year):
        df = self.df
        return df[(df.year > str(min_year)) & (df.year < str(max_year))]
    
    def filter_countries(self, countries):
        df = self.df

        return df[df.index.isin(countries)]
    
    def filter_disastertype(self, disastertype):
        df = self.df
        return df[df['disaster_type'].isin(disastertype)]
    
    def disaster_count_timeseries(self, min_year, max_year, countries, disastertype):
        df = self.df
        if type(countries) == str: countries = [countries]
        if type(disastertype) == str: disastertype = [disastertype]

        if min_year and max_year:
            df = df[(df.year > str(min_year)) & (df.year < str(max_year))]
            
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
    
    def disaster_stats_df(self, min_year, max_year, countries, disastertype, stats):
        '''stats: deaths, injured, affected, total_affected, homeless, reconstruction_costs, insured_damages, total_damages'''
        df = self.df
        if type(countries) == str: countries = [countries]
        if type(disastertype) == str: disastertype = [disastertype]

        if min_year and max_year:
            df = df[(df.year > str(min_year)) & (df.year < str(max_year))]
            
        if countries == ['all'] or not countries:
            pass
        else:
            df = df[df.index.isin(countries)]

        if disastertype == ['all'] or not disastertype:
            pass
        else:
            df = df[df['disaster_type'].isin(disastertype)]

        result = df.groupby(['year','disaster_type'])[stats].sum()
        result = result.unstack().fillna(0)
            
        return(result)

    def disaster_stats_series(self, min_year, max_year, countries, disastertype, stats):
        '''stats: deaths, injured, affected, total_affected, homeless, reconstruction_costs, insured_damages, total_damages'''
        df = self.df
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
            
        return(result)

    def country_stats_timeseries(self, min_year, max_year, countries, disastertype, stats):
        '''stats: deaths, injured, affected, total_affected, homeless, reconstruction_costs, insured_damages, total_damages'''
        df = self.df
        if type(countries) == str: countries = [countries]
        if type(disastertype) == str: disastertype = [disastertype]

        if min_year and max_year:
            df = df[(df.year >   str(min_year)) & (df.year < str(max_year))]
            
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

    def disaster_stats_timeseries(self, min_year, max_year, countries, disastertype, stats):
        '''stats: deaths, injured, affected, total_affected, homeless, reconstruction_costs, insured_damages, total_damages'''
        df = self.df

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

        result = df.groupby(['year','disaster_type'])[stats].sum()
        result = result.unstack().fillna(0)
            
        return(result)

    def disaster_stats_total_for_period(self, min_year, max_year, countries, disastertype, stats):
        df = self.df

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

        return(df[stats].sum()[0])



