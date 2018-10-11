from flask import Flask, redirect, render_template, url_for
import os

app = Flask(__name__)

app_root = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
	#return app_root
	return render_template("index.html")

@app.route('/send', methods=['POST'])
def send():
	target = os.path.join(app_root, "files/")
	return target
