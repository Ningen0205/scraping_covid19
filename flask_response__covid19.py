# webhookに張り付けるURLのサーバーを立てる
from flask import Flask, jsonify
import json
app = Flask(__name__, static_folder='.', static_url_path='')
app.config['JSON_AS_ASCII'] = False

with open("today_covid19.json", encoding='utf-8') as f:
    json_load = json.load(f)

# LINE側が、作ったWEBサイト(webhookで張り付けたURL)にアクセスしたときの処理
@app.route('/')
def index():
    return jsonify(json_load)

@app.route('/user')
def user():
    return 'test'

app.run(port=8000, debug=True)
 