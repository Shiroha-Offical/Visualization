from multiprocessing.sharedctypes import Value
from operator import ge
from unicodedata import name
from django.http import response
from django.shortcuts import render
from flask import Flask, render_template, request,redirect,url_for
from flask import jsonify
from flask_cors import CORS
from matplotlib.pyplot import get
from pathy import BasePath
from spacy import util
import json
from flask_sqlalchemy import SQLAlchemy
import csv

DEBUG = True
PROVINCE = None
DATA1 = None

app = Flask(__name__)
app.config.from_object(__name__)
cors = CORS(app)

#设置编码
app.config['JSON_AS_ASCII'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite'
# 指定数据库文件
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# 允许修改跟踪数据库
db = SQLAlchemy(app)
 
@app.route('/api/getMsg', methods=['GET', 'POST'])
def province():
    response_object = {}
    if request.method == 'POST':
        post_data = request.get_json()
        PROVINCE.append({
            'name': post_data.get('name'),
            'value': post_data.get('value')
        })
    else:
        response_object = PROVINCE
 
    return jsonify(response_object)

@app.route('/api/getScene1', methods=['POST'])
def DATA1():
    return jsonify(DATA1)

# 启动运行
if __name__ == '__main__':
    filename = 'datas.csv'
    csvfile = open ('D:\\VS_code\\code\\JavaScript\\vue\\demo\\flask_data\\static\\' + filename, 'r')
    reader = csv.DictReader(csvfile, delimiter=';')
    result = []
    for row in reader:
        result.append(row)
    result = json.dumps(result)
    PROVINCE = json.loads(result)

    data1 = open('D:\\VS_code\\code\\JavaScript\\vue\\demo\\flask_data\\static\\linedata.json','r',encoding='utf-8')
    DATA1 = json.load(data1)

    app.run()   # 这样子会直接运行在本地服务器，也即是 localhost:5000
   # app.run(host='your_ip_address') # 这里可通过 host 指定在公网IP上运行