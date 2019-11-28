# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 12:11:07 2019

@author: Kamakshi
"""

import pandas as pd
import numpy as np
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import glob

#allFiles = glob.glob("finaldata/*.csv")
allFiles = glob.glob("finaldata/*.csv") 
frame = pd.DataFrame()
list_ = []
for file_ in allFiles:
    df = pd.read_csv(file_,index_col=0,encoding='latin-1')
    df = df.drop('text', 1)
    df = df.drop('date', 1)
    list_.append(df)
frame = pd.concat(list_)
frame.dropna(axis=1,how='any',inplace=True)
#print(frame)

dfinputs = frame.drop('difference',1)

X= np.array(dfinputs).astype(float)
y= np.array(frame['difference'].values).astype(float)

print(y)

#(X_train,X_test,y_train,y_test) = train_test_split(X, y, test_size=0.3, random_state=0)

def predict_prices(X, Y):
    #dates = np.reshape(dates,(len(dates),1))
    #svr_lin = SVR(kernel = 'linear' , C=1.0)
    #svr_poly = SVR(kernel= 'poly' , C=1.0, degree=2)
    svr_rbf = SVR(kernel='rbf' , C=1.0, gamma = 0.1)
    #svr_poly.fit(X, Y)
    svr_rbf.fit(X, Y)
    #svr_lin.fir(X,Y)
    #svr_lin.predict(X_test)
    #plt.scatter(dates, prices, color='black', label='Data')
    plt.plot(X[0], svr_rbf.predict(X), color='red', label='RBF model')
    #plt.plot(X[0], svr_lin.predict(X), color='green', label='Linear model')
    #plt.plot(X[0], svr_poly.predict(X), color='blue', label='Polynomial model')
    plt.xlabel('Combined value')
    plt.ylabel('Change in stock value')
    plt.title('Support Vector Regression')
    plt.legend()
    plt.show()

    #return svr_rbf.predict(X)[0], svr_lin.predict(X)[0], svr_poly.predict(X)[0]
    return svr_rbf.predict(X)[0]
#
predicted_price = predict_prices(X,y)

print(predicted_price)

#print(predicted_price)