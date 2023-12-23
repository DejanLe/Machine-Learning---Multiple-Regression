from flask import Flask, render_template, request, url_for, flash, redirect



import requests

import pandas as pd


data = pd.read_csv('data.csv',  engine='python', encoding='latin').dropna().drop_duplicates()
 
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictions', methods=['POST','GET'])

def prediction(): 
  
    cw = float(request.form['car_weight'])
 
    cv = float(request.form['car_volume'])

    X = data[['Weight', 'Volume']]
    y = data['CO2']
    from sklearn import linear_model

    regr = linear_model.LinearRegression()
    regr.fit(X, y) 
    predictedCO2 = regr.predict([[cw, cv]])
    print(predictedCO2)

    return render_template('predictions.html', predictedCO2=predictedCO2, cw=cw, cv=cv)
 

if __name__ == '__main__':
    app.run(debug=True)
 



