# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 14:33:03 2019

@author: amrob
"""


import pandas as pd 
import numpy as np 
import os
import datetime as dt


class Traffic_View:
    
    
    """This function Cleans the traffic and view it in a long format instead of wide. the filename workbook and the sheetname for the month should be passed as parameters.  """
    def Clean_Traffic(filename: str, sheetname: str):
        
        df = pd.read_excel(filename, sheet_name = sheetname)

        df_Date = df.iloc[2:33,0]
        print(df_Date)

        # Central Region DataFrame
        df_Central = df.iloc[1:33,1:16]
        df_Central.columns = df_Central.iloc[0]
        df_Central = df_Central.iloc[1:]
        df_Central = df_Central.melt(var_name = 'Store Number',value_name = 'Traffic' )
        df_Central = df_Central.assign(Region='Central')
   
        lst1 = []
        for i in range(15):
              for j in df_Date:
                    lst1.append(j)
        
        df_Central['Date'] = lst1
        print(df_Central)
        
        # Western Region DataFrame
        df_Western = df.iloc[1:33,16:26]
        df_Western.columns = df_Western.iloc[0]
        df_Western = df_Western.iloc[1:]
        df_Western = df_Western.melt(var_name = 'Store Number',value_name = 'Traffic' )
        df_Western = df_Western.assign(Region='Western')

        lst2 = []
        for i in range(10):
             for j in df_Date:
                   lst2.append(j)
        
        df_Western['Date'] = lst2
        print(df_Western)

        #Eastern Region DataFrame
        df_Eastern = df.iloc[1:33,26:33]
        df_Eastern.columns = df_Eastern.iloc[0]
        df_Eastern = df_Eastern.iloc[1:]
        df_Eastern = df_Eastern.melt(var_name = 'Store Number',value_name = 'Traffic' )
        df_Eastern = df_Eastern.assign(Region='Eastern')

        lst3 = []
        for i in range(7):
             for j in df_Date:
                  lst3.append(j)
        
        df_Eastern['Date'] = lst3
        print(df_Eastern)
    
        #appending the 3 Regions in one Dataframe 
        df1 = df_Central.append(df_Western)
        df_all = df1.append(df_Eastern)
        print(df_all)
        
        # adding columns from Date
        df_all['WeekDay'] = df_all['Date'].dt.weekday_name
        df_all['ISO_Week'] = df_all['Date'].dt.week
        df_all['Month'] = df_all['Date'].dt.strftime('%B')
        df_all['Year'] = df_all['Date'].dt.year
        df_all['Traffic'].replace('', np.nan, inplace=True)
        df_all.dropna(subset=['Traffic'], inplace=True)
        print(df_all)
        
        return df_all;
    
    
    
    """ This Function appends the dataframes resulting from sheets(months) in one dataframe."""
    def appending_months(df1: pd.DataFrame, df2: pd.DataFrame):
        
        df_all = df1.append(df2)
        return df_all;
        
        
        