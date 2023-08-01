#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import seaborn as sns


# In[2]:


df = pd.read_csv(r"C:\Users\naipe\Downloads\mental_health_poll_updated.csv")


# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


df['Question'].value_counts()


# In[6]:


frequency = df[df['Question'] == 'How often are you stressed']


# In[7]:


frequency.head()


# In[8]:


frequency['Event Category'].value_counts()


# In[9]:


frequency['Event Category'].value_counts().plot(kind='bar')


# In[10]:


reason = df[df['Question'] == 'What stresses you out the most']


# In[11]:


reason.head()


# In[12]:


reason['Event Category'].value_counts()


# In[13]:


reason['Event Category'].value_counts().plot(kind='bar')


# In[14]:


solution = df[df['Question']=="What are you most likely to do when you're stressed"]


# In[15]:


solution.head()


# In[16]:


solution['Event Category'].value_counts().plot(kind='bar')


# In[37]:


solution['Event Category'].value_counts()


# In[17]:


resources = df[df['Question'] == "What resources do you use to help" ]


# In[18]:


resources.head()


# In[19]:


resources['Event Category'].value_counts().plot(kind='bar')


# In[36]:


resources['Event Category'].value_counts()


# In[20]:


all_the_time = frequency[frequency['Event Category'] == 'All the time']


# In[21]:


all_the_time['Region'].value_counts().head(10).plot(kind='bar')


# In[22]:


all_the_time['Region'].value_counts().head(10)


# In[43]:


resources.to_csv('resources.csv', index=False)
frequency.to_csv('frequency.csv', index=False)
solution.to_csv('solution.csv', index=False)
reason.to_csv('reason.csv', index=False)


# In[ ]:


df_encoded = pd.get_dummies(df)
correlation_matrix = df_encoded.corr()
print(correlation_matrix)


# In[24]:


solution.describe()


# In[23]:


df['Region'].value_counts()


# In[29]:


drug_drink = solution[solution['Event Category'] == 'Drugs/Drinking']
drug_drink['Region'].value_counts().head(10)


# In[ ]:




