from flask import Flask, render_template, request, url_for, redirect, Markup, jsonify, make_response, send_from_directory, session
import json
import turo
import os

app = Flask(__name__, static_url_path='/static', threaded=True)


@app.route('/', methods=['GET'])
def index():
	#return "<h1>hello world</h1>"
	return render_template("index.html")

@app.route('/teslaViz', methods=['GET'])
def geoViz():
	DATABASE = json.load(open("dataset/teslaViz.json"))
	print len(DATABASE)
	return render_template("geoViz.html", DATABASE=DATABASE)

@app.route('/searchByMake/<make>', methods=['GET'])
def searchByMake(make):
	e = turo.search()
	f = e.searchByMake(make, "dataset/{}Viz.json".format(make))
	return render_template("geoViz.html", DATABASE=f)

@app.route('/searchByModel/<model>', methods=['GET'])
def searchByModel(model):
	e = turo.search()
	print model.replace("%20", " ").lower()
	f = e.searchByModel(model.replace("%20", " ").lower(), "dataset/{}Viz.json".format(model.replace("%20", "")))
	DATABASE = f
	return render_template("geoViz.html", DATABASE=DATABASE)

@app.route('/search/<query>', methods=['GET'])
def search(query):
	if request.args.get('force_load') != "True" and os.path.isfile("dataset/{}Viz.json".format(query.replace("%20", ""))):
		DATABASE = json.load(open("dataset/{}Viz.json".format(query.replace("%20", ""))))
	else:
		e = turo.search()
		print query.replace("%20", " ").lower()
		e.searchByModel(query.replace("%20", " ").lower(), "dataset/{}Viz.json".format(query.replace("%20", "")))
		DATABASE = json.load(open("dataset/{}Viz.json".format(query.replace("%20", ""))))
	print len(DATABASE)
	return render_template("geoViz.html", DATABASE=DATABASE)


@app.route('/makes/', methods=['GET'])
def getAllMakes():
	return jsonify(turo.getMakes())

if __name__ == '__main__':
	app.run(host='127.0.0.1', port=5000, debug=True)


