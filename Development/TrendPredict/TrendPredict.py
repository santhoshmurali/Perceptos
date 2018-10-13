# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 22:53:14 2018

@author: Santhosh
"""
import quandl
import numpy as np
import pandas as pd
import yaml

#Setting up the Configuration Variables
# Reading the formula
with open(r'C:\Home\Work\Ordinarily\ML_Trading\Config.yml','r') as configFile:
    cfg = yaml.load(configFile)

quandl.ApiConfig.api_key = cfg['Quandl']['api_key']
current_month_contracts = cfg['Continous_Futures_MCX_1']['Active']
next_month_contracts = cfg['Continous_Futures_MCX_2']['Active']
data_frequency = cfg['Quandl']['freq']

DailyData_Current = pd.DataFrame()
DailyDataList = []
for k in current_month_contracts:
    df_result = quandl.get(current_month_contracts[k],collapse='daily')
    Commodity = k
    df_result['Commodity'] = Commodity
    df_result['Depth'] = 'Current'
    DailyDataList.append(df_result)

for k in next_month_contracts:
    df_result = quandl.get(next_month_contracts[k],collapse='daily')
    Commodity = k
    df_result['Commodity'] = Commodity
    df_result['Depth'] = 'Next'
    DailyDataList.append(df_result)


DailyData_Current = pd.concat(DailyDataList)