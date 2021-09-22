import re
import flask
from flask import Flask,request,jsonify
from flask.helpers import make_response
from flask import Request

app = Flask(__name__)
@app.route('/')
def index():
    return '</h3> Hello World </h2>'

@app.route('/user/<name>')
def user(name):
    return '<h2> Hello ,%s!<h2>' %name

@app.route('/header')
def header():
    user_agent = request.headers.get('User-Agent')
    return '<p> you brouser is %s </p>'%user_agent


income = [{'des':"Product Based",'amount': 500}]


@app.route('/incomes')
def get_income():
    return jsonify(income)


@app.route('/incomes', methods=["POST"])
def add_incomes():
    income.append(request.get_json())
    return 'Created',201


if __name__=='__main__':
    print(income)
    app.run(debug=True)
