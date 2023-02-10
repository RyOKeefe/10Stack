from flask import Flask, request, render_template
import requests
from riotwatcher import LolWatcher, ApiError
import os
app = Flask(__name__)
url = 'https://americas.api.riotgames.com/riot'
my_region = 'na1'

lol_watcher = LolWatcher(os.environ.get('key'))


my_region = 'na1'


@app.route('/')
def home():
    name = request.form['gameName']
    me = lol_watcher.summoner.by_name(my_region, 'DeSolu')

    return  render_template('index.html')


if __name__ == '__main__':
    app.run()
