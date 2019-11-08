# mongo.py

from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'blog'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/blog'

mongo = PyMongo(app)

@app.route('/star', methods=['GET'])
def get_all_stars():
  star = mongo.db.sendlist
  output = []
  for s in star.find():
    output.append({'send_title' : s['send_title'], 'send_acro' : s['send_acro'], 'send_explanation' : s['send_explanation']})
  return jsonify({'result' : output})

@app.route('/star/<name>', methods=['GET'])
def get_one_star(name):
  star = mongo.db.sendlist
  s = star.find_one({'send_acro' : name})
  if s:
    output = {'send_title' : s['send_title'], 'send_acro' : s['send_acro'], 'send_explanation' : s['send_explanation']}
  else:
    output = "No such name"
  return jsonify({'result' : output})

@app.route('/star', methods=['POST'])
def add_star():
  star = mongo.db.sendlist
  send_title = request.json['send_title']
  send_acro = request.json['send_acro']
  send_explanation = request.json['send_explanation']
  star_id = star.insert({'send_title': send_title, 'send_acro': send_acro, 'send_explanation': send_explanation})
  new_star = star.find_one({'send_title': send_title })
  output = {'send_title' : new_star['send_title'], 'send_acro' : new_star['send_acro'], 'send_explanation' : new_star['send_explanation']}
  return jsonify({'result' : output})

if __name__ == '__main__':
    app.run(debug=True)