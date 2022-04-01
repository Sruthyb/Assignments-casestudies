# -*- coding: utf-8 -*-


import pandas as pd
df=pd.read_excel('iris.xls')

#outliers removing
df.drop([15, 32, 33,60],inplace=True)

# splitting dataset into target and features
x=df.drop(['Classification'],axis=1)
y=df['Classification']

from sklearn.neighbors import KNeighborsClassifier
classifier=KNeighborsClassifier()
# fitting model
m=classifier.fit(x,y)

import pickle 
pickle.dump(classifier,open('model.pkl','wb'))