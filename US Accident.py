# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 13:09:21 2020

@author: acer
"""


import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
pd.options.mode.chained_assignment = None
pd.options.display.max_columns = 999


#Load Data
train_df = pd.read_csv(r"D:\Data Download\US_Accidents_June20.csv")

df = train_df[['ID','Severity', 'Start_Time',
                    'End_Time','Start_Lat','Start_Lng',
                    'State','Temperature(F)','Wind_Chill(F)',
                    'Humidity(%)','Pressure(in)','Visibility(mi)',
                    'Wind_Direction','Wind_Speed(mph)','Precipitation(in)',
                    'Weather_Condition','Sunrise_Sunset'                    
                    ]]

# Map Severity to 0,1
df.loc[df['Severity'] <= 2, 'Severity_Map'] = '0' 
df.loc[df['Severity'] >  2, 'Severity_Map'] = '1' 


# Cast data to datetime
df['Start_Time']= pd.to_datetime(df['Start_Time'])
df['End_Time']= pd.to_datetime(df['End_Time'])

#Segment Start Time
df['Start_Time_Hour'] = df['Start_Time'].dt.hour.map("{:02}".format).astype(int)

df.loc[(df['Start_Time_Hour'] >= 0) & (df['Start_Time_Hour'] < 6), 'Start_Time_Segment']    = '0H-6H'  
df.loc[(df['Start_Time_Hour'] >= 6) & (df['Start_Time_Hour'] < 12), 'Start_Time_Segment']   = '6H-12H' 
df.loc[(df['Start_Time_Hour'] >= 12) & (df['Start_Time_Hour'] < 18), 'Start_Time_Segment']  = '12H-18H'  
df.loc[(df['Start_Time_Hour'] >= 18) & (df['Start_Time_Hour'] < 24), 'Start_Time_Segment']  = '18H-24H'

#Segment End Time
df['End_Time_Hour'] = df['End_Time'].dt.hour.map("{:02}".format).astype(int)

df.loc[(df['End_Time_Hour'] >= 0) & (df['End_Time_Hour'] < 6), 'End_Time_Segment']    = '0H-6H' 
df.loc[(df['End_Time_Hour'] >= 6) & (df['End_Time_Hour'] < 12), 'End_Time_Segment']   = '6H-12H' 
df.loc[(df['End_Time_Hour'] >= 12) & (df['End_Time_Hour'] < 18), 'End_Time_Segment']  = '12H-18H' 
df.loc[(df['End_Time_Hour'] >= 18) & (df['End_Time_Hour'] < 24), 'End_Time_Segment']  = '18H-24H'


df_2016= df[df['Start_Time'].dt.year == 2016]

del df_2016['Severity']
del df_2016['Start_Time']
del df_2016['End_Time']
del df_2016['Start_Time_Hour']
del df_2016['End_Time_Hour']

#Export Data To CSV
df_2016.to_csv(r"D:\Data Download\USAccident_Custom.csv", encoding='utf-8', index=False)


 
 
 
 
 
 
 
 
 