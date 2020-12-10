#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

dataset = pd.read_csv('dataSolution_Writing.csv').values
print(dataset)


# In[2]:


data = dataset[:, 0:2]
target = dataset[:, 2]


# In[3]:


train_data, test_data, train_target, test_target = train_test_split(
    data, target, test_size=0.1)


# In[4]:


#from sklearn.svm import SVC

# model=SVC(kernel='rbf')

model = KNeighborsClassifier()

#from sklearn.naive_bayes import GaussianNB

# model=GaussianNB()

#from sklearn.tree import DecisionTreeClassifier

# model=DecisionTreeClassifier()

model.fit(train_data, train_target)


# In[5]:


predicted_target = model.predict(test_data)


# In[6]:


print('Actual Target:', test_target)
print('Predicted Target:', predicted_target)


# In[7]:


acc = accuracy_score(test_target, predicted_target)
print('Accuracy:', acc)
print('Confusion Matrix:', confusion_matrix(test_target, predicted_target))
print('Classification Report:', classification_report(
    test_target, predicted_target))


# In[8]:


joblib.dump(model, 'Writing_Activity_Suggestion.sav')


# In[9]:


# In[ ]:
