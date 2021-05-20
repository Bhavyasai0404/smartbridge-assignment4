import numpy as np
import pandas as pd
data=pd.read_csv("bank.csv")
print("data",data)
p=data.isnull().any()
print("null",p)
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
data["deposit"]=le.fit_transform(data["deposit"])
print(data["deposit"])
data.drop("default",axis=1,inplace=True)
data.drop("contact",axis=1,inplace=True)
data.drop("poutcome",axis=1,inplace=True)
print(data)
q=data["job"].unique()
print(q)
r=data["marital"].unique()
print(r)
s=data["education"].unique()
print(s)
t=data["housing"].unique()
print(t)
u=data["loan"].unique()
print(u)
v=data["month"].unique()
print(v)
x=data.iloc[:,0:13].values
print("x:",x)
y=data.iloc[:,13].values
print("y:",y)
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
ct=ColumnTransformer([("encoder",OneHotEncoder(),[1,2,3,6,5,8])],remainder="passthrough")
x=ct.fit_transform(x)
print(x)
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.fit_transform(x_test)
print("xtest",x_test)
from sklearn.linear_model import LogisticRegression
logreg=LogisticRegression()
logreg.fit(x_train,y_train)
ypred=logreg.predict(x_test)
print("ypred",ypred)
print("ytest",y_test)
from sklearn.metrics import accuracy_score
accuracy=accuracy_score(ypred,y_test)
print(accuracy)
