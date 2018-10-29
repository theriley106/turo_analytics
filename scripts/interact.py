import psycopg2
import json
import credentials

values = json.load(open("dataset/data.json"))

conn = psycopg2.connect(host="ec2-54-243-129-189.compute-1.amazonaws.com", database="dbfncufnkimb1n", user=credentials.get_sql_username(), password=credentials.get_sql_password())
listofvalues = ['reviewCount', 'rating', 'owner_image_thumbnails_225x225', 'location_precision_accuracy', 'responseTime', 'rate_monthly', 'owner_image_thumbnails_84x84', 'vehicle_marketCountry', 'vehicle_listingCreatedTime', 'vehicle_marketCurrency_decimalPlaces', 'owner_image_id', 'vehicle_marketCurrency_currencyCode', 'images_0_thumbnails_170x125', 'rate_averageDailyPriceWithCurrency_currencyCode', 'owner_lastName', 'rate_averageDailyPriceWithCurrency_amount', 'owner_firstName', 'vehicle_image_verified', 'location_city', 'vehicle_id', 'vehicle_marketCurrency_symbol', 'images_0_thumbnails_620x372', 'location_country', 'images_0_resizableUrlTemplate', 'vehicle_image_resizableUrlTemplate', 'location_precision_level', 'distanceLabel', 'location_longitude', 'owner_image_placeholder', 'vehicle_automaticTransmission', 'vehicle_make', 'owner_image_verified', 'vehicle_image_thumbnails_574x343', 'vehicle_year', 'images_0_thumbnails_50x30', 'owner_image_thumbnails_32x32', 'vehicle_url', 'rentableFromSearchedAirport', 'vehicle_marketCurrency_defaultFractionDigits', 'responseRate', 'owner_image_originalImageUrl', 'rate_daily', 'deliveryLabel', 'images_0_originalImageUrl', 'vehicle_image_originalImageUrl', 'images_0_id', 'owner_name', 'renterTripsTaken', 'distance', 'images_0_thumbnails_100x60', 'location_locationSource', 'rate_weekly', 'vehicle_image_id', 'location_address', 'images_0_thumbnails_574x343', 'vehicle_registration', 'vehicle_image_thumbnails_170x125', 'vehicle_name', 'businessClass', 'location_timeZone', 'distanceWithUnit_unit', 'vehicle_type', 'rate_averageDailyPrice', 'vehicle_image_thumbnails_620x372', 'location_state', 'location_addressLines_0', 'vehicle_model', 'owner_image_resizableUrlTemplate', 'distanceWithUnit_scalar', 'location_latitude', 'vehicle_trim', 'images_0_thumbnails_170x102', 'vehicle_image_placeholder', 'vehicle_image_thumbnails_100x60', 'distanceWithUnit_unlimited', 'vehicle_image_thumbnails_50x30', 'images_0_verified', 'freeDeliveryPromotion', 'owner_image_thumbnails_300x300', 'newListing', 'vehicle_image_thumbnails_170x102', 'instantBookDisplayed', 'owner_id', 'images_0_placeholder']
cursor = conn.cursor()
cursor.execute("""CREATE TABLE turodb(
   reviewCount                                     BIGINT
  ,rating                                          DECIMAL
  ,owner_image_thumbnails_225x225                  TEXT
  ,location_precision_accuracy                     DECIMAL
  ,responseTime                                    BIGINT
  ,rate_monthly                                    DECIMAL
  ,owner_image_thumbnails_84x84                    TEXT
  ,vehicle_marketCountry                           TEXT
  ,vehicle_listingCreatedTime                      BIGINT
  ,vehicle_marketCurrency_decimalPlaces            TEXT
  ,owner_image_id                                  TEXT
  ,vehicle_marketCurrency_currencyCode             TEXT
  ,images_0_thumbnails_170x125                     TEXT
  ,rate_averageDailyPriceWithCurrency_currencyCode TEXT
  ,owner_lastName                                  TEXT
  ,rate_averageDailyPriceWithCurrency_amount       DECIMAL
  ,owner_firstName                                 TEXT
  ,vehicle_image_verified                          TEXT
  ,location_city                                   TEXT
  ,vehicle_id                                      BIGINT PRIMARY KEY
  ,vehicle_marketCurrency_symbol                   TEXT
  ,images_0_thumbnails_620x372                     TEXT
  ,location_country                                TEXT
  ,images_0_resizableUrlTemplate                   TEXT
  ,vehicle_image_resizableUrlTemplate              TEXT
  ,location_precision_level                        TEXT
  ,distanceLabel                                   TEXT
  ,location_longitude                              DECIMAL
  ,owner_image_placeholder                         TEXT
  ,vehicle_automaticTransmission                   TEXT
  ,vehicle_make                                    TEXT
  ,owner_image_verified                            TEXT
  ,vehicle_image_thumbnails_574x343                TEXT
  ,vehicle_year                                    BIGINT
  ,images_0_thumbnails_50x30                       TEXT
  ,owner_image_thumbnails_32x32                    TEXT
  ,vehicle_url                                     TEXT
  ,rentableFromSearchedAirport                     TEXT
  ,vehicle_marketCurrency_defaultFractionDigits    TEXT
  ,responseRate                                    BIGINT
  ,owner_image_originalImageUrl                    TEXT
  ,rate_daily                                      DECIMAL
  ,deliveryLabel                                   TEXT
  ,images_0_originalImageUrl                       TEXT
  ,vehicle_image_originalImageUrl                  TEXT
  ,images_0_id                                     TEXT
  ,owner_name                                      TEXT
  ,renterTripsTaken                                BIGINT
  ,distance                                        DECIMAL
  ,images_0_thumbnails_100x60                      TEXT
  ,location_locationSource                         TEXT
  ,rate_weekly                                     DECIMAL
  ,vehicle_image_id                                TEXT
  ,location_address                                TEXT
  ,images_0_thumbnails_574x343                     TEXT
  ,vehicle_registration                            TEXT
  ,vehicle_image_thumbnails_170x125                TEXT
  ,vehicle_name                                    TEXT
  ,businessClass                                   TEXT
  ,location_timeZone                               TEXT
  ,distanceWithUnit_unit                           TEXT
  ,vehicle_type                                    TEXT
  ,rate_averageDailyPrice                          DECIMAL
  ,vehicle_image_thumbnails_620x372                TEXT
  ,location_state                                  TEXT
  ,location_addressLines_0                         TEXT
  ,vehicle_model                                   TEXT
  ,owner_image_resizableUrlTemplate                TEXT
  ,distanceWithUnit_scalar                         BIGINT
  ,location_latitude                               DECIMAL
  ,vehicle_trim                                    TEXT
  ,images_0_thumbnails_170x102                     TEXT
  ,vehicle_image_placeholder                       TEXT
  ,vehicle_image_thumbnails_100x60                 TEXT
  ,distanceWithUnit_unlimited                      TEXT
  ,vehicle_image_thumbnails_50x30                  TEXT
  ,images_0_verified                               TEXT
  ,freeDeliveryPromotion                           TEXT
  ,owner_image_thumbnails_300x300                  TEXT
  ,newListing                                      TEXT
  ,vehicle_image_thumbnails_170x102                TEXT
  ,instantBookDisplayed                            TEXT
  ,owner_id                                        BIGINT
  ,images_0_placeholder                            TEXT
);""")
conn.commit()
for i, var in enumerate(values):
	try:
		#raw_input(','.join([str(var[k]) for k in listofvalues]))
		command = "INSERT INTO turodb ( %s ) VALUES ( %s )" % (', '.join(listofvalues), str("%s, " * len(listofvalues))[:-2])
		#prBIGINT placeholders.count("%s")
		#prBIGINT len(var.values())
		var.values()
		for v in listofvalues:
			if v not in var:
				var[v] = None
		cursor.execute(command, [var[v] for v in listofvalues])
		if i % 25 == 0:
			conn.commit()
		print i
	except Exception as exp:
		cursor.execute("ROLLBACK")
		conn.commit()
		print exp

conn.commit()
