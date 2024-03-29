# -*- coding: utf-8 -*-
"""heart_disease_prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MJ8fAVxDQbE4StOzhL7E-OW95TM2F3Cs
"""



import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

heart_data=pd.read_csv("uday-venkatesha/Multiple_disease_prediction/Data Set/heart_disease_data.csv")

heart_data.head()

heart_data.shape

heart_data.describe

heart_data.isnull().sum()

#statistical measure of data
heart_data.describe()

#checkin the ditribution of target variable 
heart_data['target'].value_counts()
#here 1 is defective heart 0 is healthy heart

x=heart_data.drop(columns='target',axis=1)
y=heart_data['target']

print(x)

print(y)

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,stratify=y,random_state=2)

print(x.shape,x_train.shape,x_test.shape)

model=LogisticRegression()

#training the logistic regression model with training data
model.fit(x_train,y_train)

#evaluate 
x_pred=model.predict(x_train)
training_data_accuracy=accuracy_score(x_pred,y_train)
print(training_data_accuracy)

# testing data prediction
x_test_pred=model.predict(x_test)
testing_data_accuracy=accuracy_score(x_test_pred,y_test)
print(testing_data_accuracy)

input_data=(41,0,1,130,204,0,0,172,0,1.4,2,0,2)
#change the input data to numpy array
input_data_as_np_array=np.asarray(input_data)

input_data_as_np_array.shape

input_data_reshaped=input_data_as_np_array.reshape(1,-1)

predicton=model.predict(input_data_reshaped)
print(predicton)

# saving the model used, needed in multiple disease prediction project
import pickle
filename='heart_model.sav'
pickle.dump(model,open(filename,'wb'))
loaded_model= pickle.load(open(filename,'rb'))

