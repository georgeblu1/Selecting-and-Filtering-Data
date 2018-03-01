
# coding: utf-8

# In[18]:


import pandas as pd
melbourne_data = pd.read_csv(r'C:\Users\George\Documents\biodiversity-in-national-parks\melb_data.csv')
melbourne_data = melbourne_data.dropna(axis=0)


# In[19]:


y = melbourne_data.Price


# In[20]:


#Choosing the predicting target, which is the price 
melbourne_predictors = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 'YearBuilt', 'Lattitude', 'Longtitude'] 


# In[21]:


X = melbourne_data[melbourne_predictors] #assign it to X


# In[22]:


# we will select the predictors and the target shouldnt be within it


# In[23]:


from sklearn.tree import DecisionTreeRegressor

melbourne_model = DecisionTreeRegressor() #define the model

melbourne_model.fit(X,y) #x is the predictors, y is the target 


# In[24]:


print("Making predictions for the following 5 houses:")
print(X.head())
print("The predictions are")
print(melbourne_model.predict(X.head()))#using the prediction function


# In[25]:


print(melbourne_data)


# In[ ]:


melbourne_predictors = ['LotArea', 'Bathroom', 'Landsize', 'BuildingArea', 'YearBuilt', 'Lattitude', 'Longtitude'] 

