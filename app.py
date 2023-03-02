from flask import Flask, render_template
import numpy as np
import pandas as pd
from yahoo_fin import stock_info
from datetime import datetime
import time
import yfinance as yf

start_date = datetime(2023, 3, 1)
this_date = datetime.now()
end_date = this_date.timetuple()[:3]
data = yf.download('SOL-USD', start=start_date, end=end_date)

# save for later use
data.to_csv('sol_data.csv', index=False)

@app.route("/")
def home():
    return render_template("index.html", title="Arctic Frenz")