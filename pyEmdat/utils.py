import pandas as pd
import wbdata
import os

data = os.getenv('data')

def get_GNI(df):
    # Takes a dataframe where the columns are country names and the rows are dates
    # Returns GNI in current US dollars from the WDI
    countries = df.columns
    date_tuple = df.index.min(),df.index.max()

    ISO_dict = pd.read_csv(data+'/ISO_codes.csv',index_col=[0]).ISO.to_dict()

    ISOs = [ISO_dict[country] for country in countries]
    indicators = {'NY.GNP.MKTP.CD':'GNI_current_USD'}
    result = wbdata.get_dataframe(indicators,country=ISOs)
    result=result['GNI_current_USD'].unstack().T
    return(result)

def get_pop(df):
    # Takes a dataframe where the columns are country names and the rows are dates
    # Returns population from the WDI
    countries = df.columns
    date_tuple = df.index.min(),df.index.max()

    ISO_dict = pd.read_csv(data+'/ISO_codes.csv',index_col=[0]).ISO.to_dict()

    ISOs = [ISO_dict[country] for country in countries]
    indicators = {'SP.POP.TOTL':'population'}
    result = wbdata.get_dataframe(indicators,country=ISOs)
    result=result['population'].unstack().T
    return(result)