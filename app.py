from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def arctic_frenz():
    return render_template("index.html", title="Arctic Frenz")


"""
#import necessary libraries
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

#load data into a dataframe
df = pd.read_csv('stock_data.csv')

#split data into features and labels
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

#create a linear regression model
regressor = LinearRegression()

#fit the model to the data
regressor.fit(X, y)

#predict the stock prices
y_pred = regressor.predict(X)
    
# An elaborate, high quality docstring for the above function:
"""
"""
This function predicts the stock prices for a given set of features.

Parameters
----------
X : numpy array
    The features for which the stock prices are to be predicted.

Returns
-------
y_pred : numpy array
    The predicted stock prices.

"""