#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import libraries
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


#import data
data = pd.read_csv('C:/Users/desum/OneDrive/Desktop/Sem_1/DS/Project/Chicago_Crime.csv')
print('File Read Succesfully')


# In[3]:


data.info()


# In[19]:


#suming the null values in the dataset
data.isnull().sum()


# In[7]:


#HeatMap
plt.figure(figsize=(10,7))
sns.heatmap(data.isnull(),cbar =False, cmap = 'viridis')


# In[8]:


#droping the null columns
data = data.dropna()


# In[11]:


#checking the null values
data.isnull().sum()


# In[10]:


data.head()


# In[12]:


def plot_counts(serie, title):
    df = pd.DataFrame(serie.value_counts()[:15])
    df.columns = ["Freq"]
    df["Type"] = df.index
    fig = px.bar(df, y="Freq", x="Type", text="Freq", color="Freq", color_continuous_scale=px.colors.sequential.OrRd)
    fig.update_traces(texttemplate="%{text:.2s}", textposition="outside")
    #fig.update_layout(uniformtext_minsize=8, uniformtext_mode="hide")
    fig.update_layout(title_text=title)
    fig.show()


# In[13]:


#Converting argument to datetime
data['Date']=pd.to_datetime(data['Date'])


# In[14]:


data.tail()


# In[15]:


data.index= pd.DatetimeIndex(data.Date)
data.index = pd.to_datetime(data.index)


# In[20]:


#Categorical are a pandas data type that corresponds to the categorical variables in statistics. Such variables take 
#on a fixed and limited number of possible values. For examples – grades, gender, blood group type etc. 

data['Primary Type'] = pd.Categorical(data['Primary Type'])
data['Description'] = pd.Categorical(data['Description'])
data['Location Description'] = pd.Categorical(data['Location Description'])


# In[21]:


data['Primary Type']


# In[22]:


#plotting the progress of crimes over years
plt.figure(figsize = (10,5))
data.groupby([data.index.year]).size().plot.line()
plt.title('Crime Over the Years')
plt.xlabel('Year')
plt.ylabel('No. of Crimes ')
plt.show()


# In[23]:


#Plotting crimes happen in a month
plt.figure(figsize = (10,5))
data.groupby([data.index.month]).size().plot.bar()
plt.title('Crime Per Month')
plt.xlabel('Month')
plt.ylabel('No. of Crimes ')
plt.show()


# In[24]:


#Crimes happening on a day in a year
plt.figure(figsize = (10,5))
data.groupby([data.index.day]).size().plot.bar()
plt.title('Crime Per Day Of Month')
plt.xlabel('Day')
plt.ylabel('No. of Crimes ')
plt.show()


# In[25]:


#Crimes happening on an average hour
plt.figure(figsize = (10,5))
data.groupby([data.index.hour]).size().plot.bar()
plt.title('Crime Per Hour')
plt.xlabel('Hour')
plt.ylabel('No. of Crimes ')
# %matplotlib qt                   
plt.show()


# In[26]:


#Overall graph for each type of crime and its graph over years
crimes_count_date = data.pivot_table('ID', aggfunc=np.size, columns='Primary Type', index=data.index.date, fill_value=0)
crimes_count_date.index = pd.DatetimeIndex(crimes_count_date.index)
plo = crimes_count_date.rolling(365).sum().plot(figsize=(50, 50), subplots=True, layout=(-1, 3), sharex=False, sharey=False)
# %matplotlib qt                  


# In[28]:


from sklearn.model_selection import train_test_split

training_data, testing_data = train_test_split(data, test_size=0.2, random_state=25)

print(f"No. of training examples: {training_data.shape[0]}")
print(f"No. of testing examples: {testing_data.shape[0]}")


# In[29]:


print(training_data)


# In[30]:


training_data.head()


# In[ ]:




