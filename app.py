from flask import Flask, render_template, request, url_for, redirect, Markup, jsonify, make_response, send_from_directory, session
import json
import turo

app = Flask(__name__, static_url_path='/static')


@app.route('/', methods=['GET'])
def index():

	return render_template("geoViz.html")

@app.route('/teslaViz', methods=['GET'])
def geoViz():
	DATABASE = json.load(open("dataset/teslaViz.json"))
	print len(DATABASE)
	return render_template("geoViz.html", DATABASE=DATABASE)

@app.route('/searchByMake/<make>', methods=['GET'])
def searchByMake(make):
	make = make.lower()
	try:
		DATABASE = json.load(open("dataset/{}Viz.json".format(make)))
	except:
		e = turo.search()
		e.searchByMake(make, "dataset/{}Viz.json".format(make))
		DATABASE = json.load(open("dataset/{}Viz.json".format(make)))
	print len(DATABASE)
	return render_template("geoViz.html", DATABASE=DATABASE)

@app.route('/searchByModel/<model>', methods=['GET'])
def searchByModel(model):
	try:
		DATABASE = json.load(open("dataset/{}Viz.json".format(model.replace("%20", ""))))
	except:
		e = turo.search()
		print model.replace("%20", " ").lower()
		e.searchByModel(model.replace("%20", " ").lower(), "dataset/{}Viz.json".format(model.replace("%20", "")))
		DATABASE = json.load(open("dataset/{}Viz.json".format(model.replace("%20", ""))))
	print len(DATABASE)
	return render_template("geoViz.html", DATABASE=DATABASE)

if __name__ == '__main__':
	app.run(host='127.0.0.1', port=5000, debug=True)
