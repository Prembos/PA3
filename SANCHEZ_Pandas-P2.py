#!/usr/bin/env python
# coding: utf-8

# # PROBLEM 2

# In[6]:


import pandas as pd


# In[8]:


cars = pd.read_csv('cars.csv')


# In[38]:


cars[1:11:2]


# In[42]:


cars.head(1)


# In[88]:


cars.iloc[[23],[0,2]]


# In[90]:


cars.loc[[1,18,28],['Model','cyl','gear']]


# In[ ]:




