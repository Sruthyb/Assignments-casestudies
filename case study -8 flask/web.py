# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 22:51:56 2022

@author: sruthy
"""
from flask import Flask,render_template,request
import pickle
app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict',methods=['POST'])
def predict():
    sepalwidth=float(request.values['sw'])
    sepallength=float(request.values['sl'])
    petalwidth=float(request.values['pw'])
    petallength=float(request.values['pl'])
    output=model.predict([[sepalwidth,sepallength,petalwidth,petallength]])
    output=output.item()
    return render_template('predict.html',prediction_text='Predicted iris species is "{}"'.format(output))
if __name__=="__main__":
    app.run(port=8000)
