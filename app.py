import json
from flask import Flask, render_template, request
from datetime import datetime
import time
import schedule
import requests
app = Flask(__name__)
def update_data():
    url = "https://min-api.cryptocompare.com/data/v2/histohour?fsym=SOL&tsym=USD&limit=2000&api_key=355dbaeffaa15832d7efde34d6a0473a9a6a2c8e0dc54e05b3e6028836e4ba59"
    response = requests.get(url)
    data = response.json()
    with open('static/data.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file)


@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method == 'POST':
        with open('static/file1.json', encoding='utf-8') as f1, open('static/file2.json', encoding='utf-8') as f2, open('static/file3.json', encoding='utf-8') as f3, open('static/file4.json', encoding='utf-8') as f4, open('static/file5.json', encoding='utf-8') as f5:
            data1 = json.load(f1)
            data2 = json.load(f2)
            data3 = json.load(f3)
            data4 = json.load(f4)
            data5 = json.load(f5)
            data_list = [data1, data2, data3, data4, data5]
            if request.form.get('index_value'):
                index_value = int(request.form.get('index_value'))
            else:
                index_value = 0
            # increment the index
            index_value = index_value + 1
            # if the index is greater than the length of the list, reset to 0
            if index_value > len(data_list) - 1:
                index_value = 0
            # set the button text
            if index_value == 0:
                button_text = 'AI-1'
            elif index_value == 1:
                button_text = 'AI-2'
            elif index_value == 2:
                button_text = 'AI-3'
            elif index_value == 3:
                button_text = 'AI Plus'
            elif index_value == 4:
                button_text = 'Reset'
            # render the template with the new index
            return render_template('index.html', data=data_list[index_value], index_value=index_value, button_text=button_text)
    else:
        # open the first json file
        with open('static/file1.json', encoding='utf-8') as f1:
            # load the json file
            data1 = json.load(f1)
            # set the button text
            button_text = 'AI-1'
            # render the template with the initial index
            return render_template('index.html', data=data1, index=0, button_text=button_text)


if __name__ == '__main__':
    schedule.every(12).hours.do(update_data)
    while True:
        schedule.run_pending()
        app.run()
        time.sleep(1)