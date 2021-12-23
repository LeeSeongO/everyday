from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
import certifi

# mongo DB를 사용할때, 밑에 소스를 사
ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@cluster0.aywva.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)

db = client.dbStock

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/base", methods=["GET"])
def base_get():
    return jsonify({'base': '다음'})

@app.route("/codes", methods=["POST"])
def codes_post():
    market_receive = request.form['market_give']

    find_market = list(db.codes.find({'group': 'market'}, {'_id': False}))

    market_list = [i['name'] for i in find_market]

    market_list = list(set(market_list))

    return jsonify({'market_list': market_list})