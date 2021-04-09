import pandas as pd
import wbdata
import os

data = os.getenv('data')

def rebase_CPI(damage_series,base_year=2010):
    cpi = pd.read_csv(data + '/US_CPI.csv',skiprows=1,index_col='year',squeeze=True)
    cpi_base_year = cpi.loc[base_year]
    cpi_multiplier = cpi_base_year / cpi
    cpi_dict = cpi_multiplier.to_dict()
    damage_rebased = [int(val * cpi_dict[year]) for year,val in zip(damage_series.index, damage_series.values)]
    return(damage_rebased)


def get_GNI(df):
    '''Takes a dataframe where the columns are country names and the rows are dates. 
    Returns population from the WDI.

    Parameters
    ----------

    df: a Pandas dataframe'''
    countries = df.columns
    date_tuple = df.index.min(),df.index.max()

    ISO_dict = pd.read_csv(data+'/ISO_codes.csv',index_col=[0]).ISO.to_dict()

    ISOs = [ISO_dict[country] for country in countries]
    indicators = {'NY.GNP.MKTP.CD':'GNI_current_USD'}
    result = wbdata.get_dataframe(indicators,country=ISOs)
    result=result['GNI_current_USD'].unstack().T
    return(result)

def get_pop(df):
    '''Takes a dataframe where the columns are country names and the rows are dates. 
    Returns population from the WDI.

    Parameters
    ----------

    df: a Pandas dataframe'''
    countries = df.columns
    date_tuple = df.index.min(),df.index.max()

    ISO_dict = pd.read_csv(data+'/ISO_codes.csv',index_col=[0]).ISO.to_dict()

    ISOs = [ISO_dict[country] for country in countries]
    indicators = {'SP.POP.TOTL':'population'}
    result = wbdata.get_dataframe(indicators,country=ISOs)
    result=result['population'].unstack().T
    return(result)