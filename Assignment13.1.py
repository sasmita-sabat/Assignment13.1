
# coding: utf-8

# In[109]:


import pandas as pd
import numpy as np
df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm','Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays':  [[23, 47], [], [24, 43, 87], [13], [67, 32]], 
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )', '12. Air France', '"Swiss Air"']})
#Some values in the the FlightNumber column are missing. These numbers are meant
#to increase by 10 with each row so 10055 and 10075 need to be put in place. Fill in
#these missing numbers and make the column an integer column (instead of a float
#column).
df['FlightNumber'] = df['FlightNumber'].interpolate().astype(int)
df1=df
df2= pd.DataFrame(df1.From_To.str.split('_',1).tolist(),columns = ['From','To'])
df2['From']=df2['From'].apply(lambda x: x.title())
df2['To']=df2['To'].apply(lambda x: x.title())
del df['From_To']
df = pd.concat([df,df2],axis=1)
delays=pd.DataFrame(df['RecentDelays'].apply(pd.Series))
df = pd.concat([df,delays],axis=1)
del df['RecentDelays']
df.columns =['Airline','FlightNumber', 'From','To','delay1','delay2','delay3']
df

