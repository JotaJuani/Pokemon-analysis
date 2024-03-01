#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


df = pd.read_csv(r"C:\Users\juani\OneDrive\Desktop\PYTHON\myexercises\data\pokemon analysis\Pokemon.csv")


# In[5]:


df.head(10)


# In[6]:


df.shape


# In[7]:


df.info()


# In[8]:


##Attack greater than 150


# In[9]:


df.loc[df['Attack'] > 150].shape


# In[10]:


#how many pokemons have a speed less than 10
Slow_pokemons_df = df.loc[df['Speed'] <= 10]


# In[11]:


# how many pokemos have sp.def value of 25 or less 


# In[48]:


df.loc[df['Sp. Def'] <= 25].shape


# In[ ]:


# select only the pokemons that legendary 


# In[ ]:


df['legendary']


# In[ ]:





# In[16]:


df.loc[df['Legendary']]


# In[19]:


df['Legendary'].sum()


# In[20]:


##how many fire flying pokemons are over there? 


# In[24]:


df.loc[(df['Type 1'] == 'Fire') & (df['Type 2'] == 'Flying')]


# In[ ]:


#how many pokemons are poison type?


# In[47]:


df.loc[(df['Type 1'] == 'Poison') | (df['Type 2'] == 'Poison')]


# In[ ]:





# In[ ]:


# what pokemon of type 1 ice has the strongest defence 


# In[41]:


df.loc[df['Type 1'] =='Ice','Defense'].max()


# In[42]:


df.loc[(df['Type 1'] == 'Ice') & (df['Defense'] == 184 )]


# In[43]:


#what is the most legendary type of pokemons


# In[46]:


df.loc[df['Legendary'], 'Type 1'].value_counts().plot(kind='bar')


# In[49]:


df.head(10)


# In[50]:


## the most powerful pokemon of the total from the first 3 generations of the type water


# In[57]:


df.loc[(df['Type 1'] =='Water') &
      df['Generation'].isin([1,2,3])].sort_values(by='Total', ascending = False).head()
                            


# In[58]:


##most powerfull dragon of the type Dragon from the last two generations


# In[65]:


df.loc[((df['Type 1'] =='Dragon') |
       (df['Type 2'] =='Dragon')) &
       (df['Generation'].isin({5,6}))
      ].sort_values(by='Total', ascending = False).head(1)


# In[66]:


#Select most powerfull fire-type pokemons


# In[68]:


powerful_fire_df = df.query("Attack > 100 and `Type 1` == 'Fire'")
powerful_fire_df


# In[69]:


# select all water and fire 


# In[70]:


water_flying_df = df.query("`Type 1` == 'Water' and `Type 2` == 'Flying'")
water_flying_df


# In[71]:


# select specific columns of Legendary pokemons of type Fire


# In[75]:


legendary_fire_df = df.loc[
    (
        (df['Type 1'] == 'Fire') & 
        df['Legendary']),
                          ['Name', 'Attack', 'Generation']
                          ]
legendary_fire_df


# In[ ]:




