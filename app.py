from flask import Flask, render_template, request, url_for, redirect, Markup, jsonify, make_response, send_from_directory, session
import json
import turo
import os

app = Flask(__name__, static_url_path='/static')


@app.route('/', methods=['GET'])
def index():

	return render_template("index.html")

@app.route('/teslaViz', methods=['GET'])
def geoViz():
	DATABASE = json.load(open("dataset/teslaViz.json"))
	print len(DATABASE)
	return render_template("geoViz.html", DATABASE=DATABASE)

@app.route('/searchByMake/<make>', methods=['GET'])
def searchByMake(make):
	make = make.lower()
	if request.args.get('force_load') != "True" and os.path.isfile("dataset/{}Viz.json".format(make)):
		DATABASE = json.load(open("dataset/{}Viz.json".format(make)))
	else:
		e = turo.search()
		e.searchByMake(make, "dataset/{}Viz.json".format(make))
		DATABASE = json.load(open("dataset/{}Viz.json".format(make)))
	print len(DATABASE)
	return render_template("geoViz.html", DATABASE=DATABASE)

@app.route('/searchByModel/<model>', methods=['GET'])
def searchByModel(model):
	if request.args.get('force_load') != "True" and os.path.isfile("dataset/{}Viz.json".format(model.replace("%20", ""))):
		DATABASE = json.load(open("dataset/{}Viz.json".format(model.replace("%20", ""))))
	else:
		e = turo.search()
		print model.replace("%20", " ").lower()
		e.searchByModel(model.replace("%20", " ").lower(), "dataset/{}Viz.json".format(model.replace("%20", "")))
		DATABASE = json.load(open("dataset/{}Viz.json".format(model.replace("%20", ""))))
	print len(DATABASE)
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
