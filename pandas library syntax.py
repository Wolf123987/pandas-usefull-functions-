#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np


# In[2]:


df=pd.read_csv(r"C:\Users\91983\Downloads\pokemon_data.csv")


# In[3]:


df.head()


# In[5]:


df.iloc[0:4]


# In[76]:


Name = df["Type 1"] ## to look at the specefic columns name,  only for string


# In[78]:


Name


# In[18]:


df.loc[df["Name"]  == "Charmeleon"] ### to  look ate the specefic  value ina specific columns  name 


# In[31]:


### to  combined some columns and create a new columns 

df["Total"] = df["Defense"]+df["HP"]+df["Attack"]+df["Defense"]+df["Sp. Atk"]+df["Sp. Atk"]+df["Speed"] 


# In[32]:


df.head()


# In[34]:


df.head() ## to see top rows of data


# In[46]:


d= "hcum yrev mih evol i dna nos ym si hsnardur " [::-1] #### to reverse the string 


# In[47]:


d


# In[52]:


df.dropna() ## drop row when aleats one element is missing 


# In[63]:


df.dropna(axis= 1) ## drop columns when aleats one element is missing  


# In[53]:


df.dropna(how="all") ## drop row where all  elements are missiong 


# In[65]:


df.take([2, 3],axis= 1) ##( axis = 0 for row, axis = 1 for columns ) [2,3] means columns or row indexing ]


# In[55]:


df.take([-1, -2])


# In[83]:


e=df[["Name","Type 1"]] ### to combine two string columns and  make a new columns 


# In[85]:


e.head()


# In[86]:


import matplotlib.pyplot as plt


# In[105]:


xpoints=df.("Defense")


# In[112]:


df.plot(kind = 'scatter', x = 'Defense', y = 'Speed',marker="D")


# In[122]:


####to compare the data  of two columns ,here alpha  value may be 1 for less transperant and 0.5 for more transperent 

df.plot(kind="hist",x="Defense",color="g",)


# In[103]:


df["Speed"]=df["Speed"]/df["Speed"].mean()


# In[104]:


df["Speed"]


# In[123]:


from sklearn  import linearRegression 


# In[125]:


import scikitlearn as sk


# In[126]:


from sklearn.linear_model import LinearRegression


# In[128]:


x=df[["Defense"]]


# In[130]:


y=df[["Speed"]]


# In[134]:


lm=LinearRegression()


# In[136]:


lm=Fit(x,y)


# In[ ]:




