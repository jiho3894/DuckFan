from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient(
    'url',
    connect=False)
db = client.db


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/Duck", methods=["POST"])
def homework_post():
    name_receive = request.form["name_give"]
    comment_receive = request.form["comment_give"]
    comment_list = list(db.Duck.find({}, {'_id': False}))
    count = len(comment_list) + 1

    doc = {
        'num': count,
        'name': name_receive,
        'comment': comment_receive,
    }

    db.Duck.insert_one(doc)
    return jsonify({'msg': '응원 완료!'})


@app.route("/Duck", methods=["GET"])
def homework_get():
    comment_list = list(db.Duck.find({}, {'_id': False}))
    return jsonify({'comments': comment_list})


@app.route("/Duck/Delete", methods=["POST"])
def bucket_done():
    num_receive = request.form['num_give']
    db.Duck.delete_one({'num': int(num_receive)})
    return jsonify({'msg': '삭제 완료!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
