from flask import Flask, render_template, request
from datetime import datetime
import json
import time
import schedule
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def update_content():
    """
    This function retrieves data from the specified URL and saves it to a local JSON file.
    """
    url = "https://min-api.cryptocompare.com/data/v2/histohour?fsym=SOL&tsym=USD&limit=2000&api_key=355dbaeffaa15832d7efde34d6a0473a9a6a2c8e0dc54e05b3e6028836e4ba59"
    response = requests.get(url, timeout=10)
    data = response.json()
    with open('static/file1.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file)



def index():
    """
    This function processes a POST request and updates the index value and button text accordingly. It also retrieves data from local JSON files and formats it for display on the index page.
    """
    index_value = 0
    button_text = 'AI-1'
    data_list = []
    for i in range(1, 6):
        with open(f'static/file{i}.json', encoding='utf-8') as f:
            data_list.append(json.load(f))
    if request.method == 'POST':
        index_value = int(request.form.get('index_value', 0))
        index_value = (index_value + 1) % len(data_list)
        button_text = ['AI-1', 'AI-2', 'AI-3', 'AI Plus', 'Reset'][index_value]
    data = data_list[index_value]
    last_set = data['Data']['Data'][-9:]
    time_close = []
    for item in last_set:
        local_date = datetime.fromtimestamp(item["time"]).strftime('%d-%b')
        local_time = datetime.fromtimestamp(item["time"]).strftime('%H:%M')
        time_close.append({"date": local_date, "time": local_time, "close": item["close"]})
    return render_template('index.html', data=time_close, index_value=index_value, button_text=button_text)


def check_time():
    with open('static/file1.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        time_to = data['TimeTo']
        current_time = time.time()
        if current_time - time_to > 12 * 60 * 60:
            update_content()

if __name__ == '__main__':
    # Run the check_time() function every minute
    schedule.every(1).minutes.do(check_time)
    while True:
        schedule.run_pending()
        time.sleep(1)