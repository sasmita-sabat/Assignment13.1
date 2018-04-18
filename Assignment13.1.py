
# coding: utf-8

# In[48]:


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

del df['From_To']
df = pd.concat([df,df2],axis=1)
df.From.str.title()
df.To.str.title()
df




# In[24]:


import pandas as pd
import numpy as np
df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm','Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays':  [[23, 47], [], [24, 43, 87], [13], [67, 32]], 
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )', '12. Air France', '"Swiss Air"']})
df1=df
df2= pd.DataFrame(df1.From_To.str.split('_',1).tolist(),columns = ['From','To'])
df2
df


# In[19]:


import pandas as pd
import numpy as np
df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm','Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays':  [[23, 47], [], [24, 43, 87], [13], [67, 32]], 
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )', '12. Air France', '"Swiss Air"']})

df = pd.DataFrame(df.From_To.str.split('_',1).tolist(),columns = ['From','To'])
df
df1=df.From.str.title()
df1
df2=df.To.str.title()
df2

