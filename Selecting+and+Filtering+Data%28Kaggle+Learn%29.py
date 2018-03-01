
# coding: utf-8

# In[1]:


import pandas as pd
melbourne_data = pd.read_csv(r'C:\Users\George\Documents\biodiversity-in-national-parks\melb_data.csv')
print(melbourne_data.columns)
melbourne_price_data = melbourne_data.Price
print(melbourne_price_data.head()) # head() return the top few data


# In[ ]:


column_of_interest = [ 'Price', 'Address']
two_column_of_data = melbourne_data[column_of_interest]
two_column_of_data.describe() #to see the summaries of those variables

