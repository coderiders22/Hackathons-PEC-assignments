#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import StandardScaler


# In[2]:


df = pd.read_csv('exoPlanets.csv')
X = df.drop('LABEL', axis=1)
y = df['LABEL']


# In[3]:


X_train, X_test, y_train, y_test= train_test_split(X,y, train_size=0.8, random_state=0)


# In[4]:


def score_dataset(X_train, X_test, y_train, y_test):
    model = RandomForestClassifier(min_samples_leaf=4, random_state=0)
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    accuracy_knc = accuracy_score(y_test, pred)
    print('Accuracy:', accuracy_knc * 100)


# In[5]:


columns_with_missing_values = [col for col in X_train.columns if X_train[col].isnull().any()]

missing_val_count_by_column = (X_train.isnull().sum())
print(missing_val_count_by_column[missing_val_count_by_column > 0])


# In[6]:


myimputer=SimpleImputer(strategy="mean")
imputed_X_train=pd.DataFrame(myimputer.fit_transform(X_train))
imputed_X_test=pd.DataFrame(myimputer.transform(X_test))
print(score_dataset(imputed_X_train, imputed_X_test, y_train, y_test))


# In[7]:


import pickle
from sklearn.ensemble import RandomForestClassifier
clf_decisiontree=DecisionTreeClassifier(criterion="entropy",random_state=0)
model=clf_decisiontree.fit(X,y)
with open('finalized_model',"wb") as f:
    pickle.dump(model,f)


# In[8]:


import pickle
with open('finalized_model', 'rb') as f:
    mod = pickle.load(f)


# In[11]:


print(mod.predict('new.csv'))


# In[12]:


import joblib
joblib.dump(model, 'finalized_joblib.pkl')


# In[13]:


classifier  = joblib.load('finalized_joblib.pkl')


# In[16]:


classifier.predict([[-131.59,-134.8,-186.97,-244.32]])


# In[ ]:




