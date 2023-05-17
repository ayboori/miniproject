from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.q7dgkca.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

import requests
from bs4 import BeautifulSoup

@app.route('/')
def home():
    return render_template('main.html') 
# 우선 메인페이지 연결함

@app.route("/intro", methods=["POST"])
def intro_post():
    comment_receive = request.form['comment_give']

    doc = {
        'comment':comment_receive
    }
    db.intros.insert_one(doc)

    return jsonify({'msg':'댓글 기록 완료!'})

@app.route("/intro", methods=["GET"])
def intro_get():
    all_intros = list(db.intros.find({},{'_id':False}))
    return jsonify({'result':all_intros})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)