from flask import Flask, render_template, request, url_for, redirect, Markup, jsonify, make_response, send_from_directory, session
import json
import turo
import os

app = Flask(__name__, static_url_path='/static')


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
	return render_template("geoViz.html", DATABASE=f, titleVal="Make: {}".format(make))

@app.route('/searchByModel/<model>', methods=['GET'])
def searchByModel(model):
	e = turo.search()
	print model.replace("%20", " ").lower()
	f = e.searchByModel(model.replace("%20", " ").lower(), "dataset/{}Viz.json".format(model.replace("%20", "")))
	DATABASE = f
	return render_template("geoViz.html", DATABASE=DATABASE, titleVal="Model: {}".format(model))

@app.route('/searchByVehicleID/<id_val>', methods=['GET'])
def searchByVehicleID(id_val):
	e = turo.search()
	f = e.searchVehicleID(id_val)
	DATABASE = f
	return render_template("geoViz.html", DATABASE=DATABASE, titleVal="Vehicle ID: {}".format(id_val))

@app.route('/searchByOwnerID/<id_val>', methods=['GET'])
def searchByOwnerID(id_val):
	e = turo.search()
	f = e.searchUserID(id_val)
	DATABASE = f
	return render_template("geoViz.html", DATABASE=DATABASE, titleVal="Owner ID: {}".format(id_val))


@app.route('/makes/', methods=['GET'])
def getAllMakes():
	return jsonify(turo.getMakes())

@app.route('/cool/', methods=['GET'])
def cool():
	return render_template("cool2.html")

if __name__ == '__main__':
	app.run(host='127.0.0.1', port=5000, debug=True, threaded=True)


