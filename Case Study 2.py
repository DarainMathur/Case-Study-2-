#!/usr/bin/env python
# coding: utf-8

# ## Import relevant packages

# In[165]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# ## Import Dataset as a dataframe

# In[166]:


data = pd.read_csv("C:/Users/mdara/Jupyter/Untitled Folder/Stout Projects/Case Study 2/casestudy.csv")


# ## Quick Overview of the data

# In[167]:


data.info()
data.head(50)


# ## Total revenue for the current year (Current = 2017)

# In[168]:


rev_table = data[['net_revenue', 'year']]
rev_table2 = rev_table.groupby('year').sum().sort_values('net_revenue')

rev_table2


# The total revenue for the current year is $31,417,495.03

# ## New Customer Revenue

# In[169]:


ncr = data.copy()
ncr = ncr.assign(New = np.where(~ncr['customer_email'].duplicated(), 'New', 'Existing'))

new_customers = ncr[(ncr['year'] == 2017) & (ncr['New'] == 'New')]
print('New customer revenue for 2017 was:', str(new_customers['net_revenue'].sum()))
ncr.head(5)


# #### Existing Customer Growth (Revenue of existing customers for current year –(minus) Revenue of existing customers from the previous year)

# In[171]:


rev_ex_17 = ncr[(ncr['year'] == 2017) & (ncr['New'] == "Existing")].net_revenue.sum()
rev_ex_16 = ncr[(ncr['year'] == 2016) & (ncr['New'] == 'Existing')].net_revenue.sum()
print('Existing customer growth(minus means shrinkage): ',rev_ex_17-rev_ex_16)


# ## Revenue lost from attrition

# In[172]:


rev_16 = ncr[ncr['year'] == 2016].net_revenue.sum() 
rev_ex_17 - rev_16

print("Revenue lost from attrition for year 2017 is: ", -(rev_ex_17 - rev_16))


# ### Existing Customer Revenue Current Year

# In[173]:


print('Existing Customer Revenue Current Year:',rev_ex_17)


# ### Existing Customer Revenue Prior Year

# In[174]:


print('Existing Customer Revenue Prior Year',rev_ex_16)


# ## Total customers Current Year

# In[175]:


print('Total customers Current Year:',ncr[ncr['year'] == 2017]['customer_email'].count())


# ### Total Customers Previous Year

# In[176]:


print('Total customers previous Year:',ncr[ncr['year'] == 2016]['customer_email'].count())


# ### New Customers

# In[177]:


new_cust = ncr[(ncr['year'] == 2017)&(ncr['New'] == 'New')]['customer_email'].count()
print("New customers: ",new_cust)


# ### Lost Customers
# ###### Equation Used: Total customers in '16 - Existing customers in '17

# In[178]:


lost_cust = ncr[(ncr['year'] == 2016)]['customer_email'].count()-ncr[(ncr['year']==2017)&(ncr['New']=='Existing')]['customer_email'].count()
print("Lost customers: ",lost_cust)


# # Visualizations

# In[179]:


rev_table2 = rev_table2.reset_index()


# In[183]:


rev_table2 = rev_table2.sort_values('year', ascending = True)
rev_table2


# In[184]:


fig_a, ax_a = plt.subplots(figsize = (6,6))
sns.set_theme(style="whitegrid")
ax = sns.barplot(x="year", y="net_revenue", data=rev_table2,
                palette="Blues_d")


# Revenue was at 29.03M in 2015, dipped to 25.73M in 2016, then rose to 31.42M in 2017.

# In[185]:


new_15 = 231294
new_16 = 145062
exist_16 = 59584
new_17 = 228262
exist_17 = 21725

fig0, ax0 = plt.subplots(figsize = (5,5))
labels = ['New']
ax0.pie([new_15], labels = labels)
plt.legend(loc='upper left',labels=labels)
ax0.legend(loc="lower right")
plt.title('Customer breakdown in 2015')
plt.show()


# In[153]:


fig1, ax1 = plt.subplots(figsize = (5,5))
labels = ['Existing', 'New']
ax1.pie([exist_16, new_16], labels = labels)
plt.legend(loc='upper left',labels=labels)
ax1.legend(loc="lower right")
plt.title('Customer breakdown in 2016')
plt.show()


# In[154]:


fig2, ax2 = plt.subplots(figsize = (5,5))
labels = ['Existing', 'New']
ax2.pie([exist_17, new_17], labels = labels)
plt.legend(loc='upper left',labels=labels)
ax2.legend(loc="lower right")
plt.title('Customer breakdown in 2017')
plt.show()


# From the three pie charts we can clearly see the trend of an steady increase in new customers.
