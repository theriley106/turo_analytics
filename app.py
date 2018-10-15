from flask import Flask, render_template, request, url_for, redirect, Markup, jsonify, make_response, send_from_directory, session
import json
import turo
import os
import random

ALL_KEYS = ['rating', 'owner_image_thumbnails_225x225', 'location_precision_accuracy', 'vehicle_name', 'location_timeZone', 'rate_monthly', 'distanceLabel', 'vehicle_marketCountry', 'rate_averageDailyPrice', 'vehicle_listingCreatedTime', 'vehicle_marketCurrency_decimalPlaces', 'owner_image_id', 'vehicle_marketCurrency_currencyCode', 'images_0_thumbnails_170x125', 'images_0_id', 'rate_averageDailyPriceWithCurrency_currencyCode', 'images_0_thumbnails_574x343', 'owner_lastName', 'rate_averageDailyPriceWithCurrency_amount', 'vehicle_image_verified', 'location_city', 'vehicle_id', 'location_country', 'vehicle_image_thumbnails_50x30', 'location_precision_level', 'owner_image_thumbnails_84x84', 'location_longitude', 'owner_image_placeholder', 'vehicle_make', 'images_0_verified', 'images_0_originalImageUrl', 'images_0_thumbnails_50x30', 'owner_image_thumbnails_32x32', 'vehicle_url', 'rentableFromSearchedAirport', 'vehicle_marketCurrency_defaultFractionDigits', 'responseRate', 'vehicle_image_placeholder', 'owner_image_originalImageUrl', 'rate_daily', 'deliveryLabel', 'vehicle_year', 'vehicle_image_originalImageUrl', 'reviewCount', 'owner_name', 'renterTripsTaken', 'location_addressLines_0', 'vehicle_image_resizableUrlTemplate', 'images_0_thumbnails_100x60', 'location_locationSource', 'rate_weekly', 'owner_id', 'location_address', 'images_0_resizableUrlTemplate', 'vehicle_registration', 'vehicle_image_thumbnails_170x125', 'responseTime', 'businessClass', 'vehicle_marketCurrency_symbol', 'distanceWithUnit_unit', 'vehicle_type', 'owner_image_verified', 'vehicle_image_thumbnails_620x372', 'newListing', 'distance', 'images_0_thumbnails_620x372', 'owner_image_resizableUrlTemplate', 'distanceWithUnit_scalar', 'location_state', 'vehicle_trim', 'images_0_thumbnails_170x102', 'vehicle_automaticTransmission', 'vehicle_image_thumbnails_100x60', 'distanceWithUnit_unlimited', 'freeDeliveryPromotion', 'vehicle_image_thumbnails_574x343', 'vehicle_image_id', 'owner_image_thumbnails_300x300', 'location_latitude', 'owner_firstName', 'vehicle_image_thumbnails_170x102', 'instantBookDisplayed', 'vehicle_model', 'images_0_placeholder']

app = Flask(__name__, static_url_path='/static')

def clean_data(jsonValue):
	jsonValue['rate_daily'] = str('{0:.2f}'.format(jsonValue['rate_daily']))
	jsonValue['location_address'] = jsonValue['location_address'].replace(" , ", ", ")
	return jsonValue

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
	print f
	return render_template("geoViz.html", DATABASE=f, titleVal="Make: {}".format(make))

@app.route('/searchByModel/<model>', methods=['GET'])
def searchByModel(model):
	e = turo.search()
	print model.replace("%20", " ").lower()
	f = e.searchByModel(model.replace("%20", " ").lower(), "dataset/{}Viz.json".format(model.replace("%20", "")))
	DATABASE = f
	print f
	return render_template("geoViz.html", DATABASE=DATABASE, titleVal="Model: {}".format(model))

@app.route('/searchByVehicleID/<id_val>', methods=['GET'])
def searchByVehicleID(id_val):
	e = turo.search()
	f = e.searchVehicleID(id_val)
	DATABASE = f
	print f
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

@app.route('/random', methods=['GET'])
def getNew():
	all_vals = open("randomIDs.txt").read().split("\n")
	return redirect(url_for('getSingleVehicle', id_val=random.choice(all_vals)))

@app.route('/vehicle/<id_val>', methods=['GET'])
def getSingleVehicle(id_val):
	info = {}
	e = turo.search()
	vals = e.searchSingleID(id_val)
	if len(vals) == 0:
		return redirect(url_for("getNew"))
	else:
		vals = vals[0]
	print vals
	for i, val in enumerate(vals):
		info[ALL_KEYS[i]] = val
	info['avg_price'] = e.getAveragePriceModel(info['vehicle_model'])
	info['total_count'] = e.getTotalModel(info['vehicle_model'])
	info = clean_data(info)
	return render_template("resultPage.html", result=info)

@app.route('/cool/', methods=['GET'])
def cool():
	return render_template("cool2.html")

if __name__ == '__main__':
	app.run(host='127.0.0.1', port=5000, debug=True, threaded=True)


