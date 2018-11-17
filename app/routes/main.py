from flask import render_template, redirect, url_for, jsonify
from app import app
from app.utils.main import helloWorld, checkWho


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/hello-world")
def hello():
    response = helloWorld()

    return jsonify({'response': response})


@app.route('/api/whoami')
def whoami():
    response = checkWho()

    return jsonify(response)

