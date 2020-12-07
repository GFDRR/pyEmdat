import pandas as pd

class emdat():

    def __init__(self,fn):

        cols_dict = {"Year":"year",
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

        df = pd.read_excel(fn, header = 6, index_col = 'Country')
        self.df = df.rename(columns = cols_dict)
        
    def filter_years(self, min_year, max_year):
        df = self.df
        return df[(df.year > min_year) & (df.year < max_year)]
    
    def filter_countries(self, countries):
        df = self.df

        return df[df.index.isin(countries)]
    
    def filter_disastertype(self, disastertype):
        df = self.df
        return df[df['disaster_type'].isin(disastertype)]
    
    def disaster_count_timeseries(self, min_year, max_year, countries, disastertype):
        self.df = self.df[self.df['disaster_type'].isin(disastertype)]
        if min_year and max_year:
            self.df = self.filter_years(min_year, max_year)
            
        if countries:
            self.df=self.filter_countries(countries)
            
        return(self.df.groupby(['year','disaster_type'])['Dis No'].count())
    
    def disaster_stats_timeseries(self, min_year, max_year, countries, disastertype, stats):
        '''stats: deaths, injured, affected, total_affected, homeless, reconstruction_costs, insured_damages, total_damages'''
        if disastertype:
            self.df = self.df[self.df['disaster_type'].isin(disastertype)]
        if min_year and max_year:
            self.df = self.filter_years(min_year, max_year)
            
        if countries:
            self.df=self.filter_countries(countries)
            
        return(self.df.groupby(['year','disaster_type'])[stats].sum())

    #def add_GDP(self)



