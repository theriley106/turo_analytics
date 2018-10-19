# turo_analytics
Analyzing Turo rental car data to find vehicle arbitrage opportunities in San Francisco
<center><h1><a href="https://www.kaggle.com/theriley106/turo-rental-car-pricing-info">Download the Dataset Here</a></h1></center>

<center><h1><a href="http://turo-analytics.herokuapp.com/">Check out the Turo Analytics Web App</a></h1></center>



## Dataset

### Getting Dataset

To create the dataset I needed to pull information on every vehicle listing while using the least amount of networks requests as possible.  To do this, I created a (pretty greedy) algorithm in *genLatLong.py* that attempts to find the largest covered area while using the least amount of coordinates.

<p align="center">
  <img src="src/searchLongLat.png"/>
</p>

<i><h3 align="center">Data Visualization representing the Long/Lat points used to create the Dataset</h3></i>

This dataset contains information on roughly ~40,000 currently listed (As of 07/08/2018) vehicles on Turo.  The dataset contains the following information for each vehicle.

### Example Response

| **Paramater** |
| --- |
| rating |
| owner_image_thumbnails_225x225 |
| location_precision_accuracy |
| vehicle_name |
| location_timeZone |
| rate_monthly |
| distanceLabel |
| vehicle_marketCountry |
| rate_averageDailyPrice |
| vehicle_listingCreatedTime |
| vehicle_marketCurrency_decimalPlaces |
| owner_image_id |
| vehicle_marketCurrency_currencyCode |
| images_0_thumbnails_170x125 |
| images_0_id |
| rate_averageDailyPriceWithCurrency_currencyCode |
| images_0_thumbnails_574x343 |
| owner_lastName |
| rate_averageDailyPriceWithCurrency_amount |
| vehicle_image_verified |
| location_city |
| vehicle_id |
| location_country |
| vehicle_image_thumbnails_50x30 |
| location_precision_level |
| owner_image_thumbnails_84x84 |
| location_longitude |
| owner_image_placeholder |
| vehicle_make |
| images_0_verified |
| images_0_originalImageUrl |
| images_0_thumbnails_50x30 |
| owner_image_thumbnails_32x32 |
| vehicle_url |
| rentableFromSearchedAirport |
| vehicle_marketCurrency_defaultFractionDigits |
| responseRate |
| vehicle_image_placeholder |
| owner_image_originalImageUrl |
| rate_daily |
| deliveryLabel |
| vehicle_year |
| vehicle_image_originalImageUrl |
| reviewCount |
| owner_name |
| renterTripsTaken |
| location_addressLines_0 |
| vehicle_image_resizableUrlTemplate |
| images_0_thumbnails_100x60 |
| location_locationSource |
| rate_weekly |
| owner_id |
| location_address |
| images_0_resizableUrlTemplate |
| vehicle_registration |
| vehicle_image_thumbnails_170x125 |
| responseTime |
| businessClass |
| vehicle_marketCurrency_symbol |
| distanceWithUnit_unit |
| vehicle_type |
| owner_image_verified |
| vehicle_image_thumbnails_620x372 |
| newListing |
| distance |
| images_0_thumbnails_620x372 |
| owner_image_resizableUrlTemplate |
| distanceWithUnit_scalar |
| location_state |
| vehicle_trim |
| images_0_thumbnails_170x102 |
| vehicle_automaticTransmission |
| vehicle_image_thumbnails_100x60 |
| distanceWithUnit_unlimited |
| freeDeliveryPromotion |
| vehicle_image_thumbnails_574x343 |
| vehicle_image_id |
| owner_image_thumbnails_300x300 |
| location_latitude |
| owner_firstName |
| vehicle_image_thumbnails_170x102 |
| instantBookDisplayed |
| vehicle_model |
| images_0_placeholder |



```javascript
{
    "distance": 17.0,
    "reviewCount": 0,
    "businessClass": false,
    "renterTripsTaken": 0,
    "rating": null,
    "distanceLabel": "17 mi",
    "newListing": false,
    "distanceWithUnit":
    {
        "scalar": 17,
        "unlimited": false,
        "unit": "MI"
    },
    "owner":
    {
        "lastName": "B.",
        "image":
        {
            "verified": false,
            "thumbnails":
            {
                "32x32": "https://d1zgdcrdir5wgt.cloudfront.net/media/driver/iXYfdNi1ReyINVNz8F4o_A.32x32.jpg",
                "225x225": "https://d1zgdcrdir5wgt.cloudfront.net/media/driver/iXYfdNi1ReyINVNz8F4o_A.300x300.jpg",
                "84x84": "https://d1zgdcrdir5wgt.cloudfront.net/media/driver/iXYfdNi1ReyINVNz8F4o_A.84x84.jpg",
                "300x300": "https://d1zgdcrdir5wgt.cloudfront.net/media/driver/iXYfdNi1ReyINVNz8F4o_A.300x300.jpg"
            },
            "resizableUrlTemplate": "https://d1zgdcrdir5wgt.cloudfront.net/media/driver/iXYfdNi1ReyINVNz8F4o_A.{width}x{height}.jpg",
            "placeholder": false,
            "id": null,
            "originalImageUrl": "https://d1zgdcrdir5wgt.cloudfront.net/media/driver/iXYfdNi1ReyINVNz8F4o_A.jpg"
        },
        "id": 4783843,
        "firstName": "Marcus",
        "name": "Marcus B."
    },
    "rate":
    {
        "monthly": 0.3,
        "averageDailyPrice": 902.0,
        "weekly": 0.15,
        "daily": 902.0,
        "averageDailyPriceWithCurrency":
        {
            "amount": 902.0,
            "currencyCode": "USD"
        }
    },
    "rentableFromSearchedAirport": false,
    "freeDeliveryPromotion": false,
    "location":
    {
        "city": "Rochester Hills",
        "country": "US",
        "precision":
        {
            "level": "APPROXIMATE",
            "accuracy": 0.09320565
        },
        "longitude": -83.12675,
        "locationSource": "GOOGLE",
        "state": "MI",
        "addressLines": ["Rochester Hills, MI"],
        "address": "Rochester Hills, MI 48307",
        "latitude": 42.639309,
        "timeZone": "America/New_York"
    },
    "responseTime": null,
    "vehicle":
    {
        "trim": null,
        "automaticTransmission": true,
        "name": "Marcus's Maserati",
        "url": "/rentals/cars/mi/rochester-hills/maserati-quattroporte/355498",
        "image":
        {
            "verified": false,
            "thumbnails":
            {
                "620x372": "https://d1zgdcrdir5wgt.cloudfront.net/media/vehicle/images/nZw5PNEHRV20pm2JLYAHoA.620x372.jpg",
                "50x30": "https://d1zgdcrdir5wgt.cloudfront.net/media/vehicle/images/nZw5PNEHRV20pm2JLYAHoA.50x30.jpg",
                "170x125": "https://d1zgdcrdir5wgt.cloudfront.net/media/vehicle/images/nZw5PNEHRV20pm2JLYAHoA.170x102.jpg",
                "574x343": "https://d1zgdcrdir5wgt.cloudfront.net/media/vehicle/images/nZw5PNEHRV20pm2JLYAHoA.620x372.jpg",
                "170x102": "https://d1zgdcrdir5wgt.cloudfront.net/media/vehicle/images/nZw5PNEHRV20pm2JLYAHoA.170x102.jpg",
                "100x60": "https://d1zgdcrdir5wgt.cloudfront.net/media/vehicle/images/nZw5PNEHRV20pm2JLYAHoA.100x60.jpg"
            },
            "resizableUrlTemplate": "https://d1zgdcrdir5wgt.cloudfront.net/media/vehicle/images/nZw5PNEHRV20pm2JLYAHoA.{width}x{height}.jpg",
            "placeholder": false,
            "id": null,
            "originalImageUrl": "https://d1zgdcrdir5wgt.cloudfront.net/media/vehicle/images/nZw5PNEHRV20pm2JLYAHoA.jpg"
        },
        "marketCountry": "US",
        "year": 2012,
        "id": 355498,
        "listingCreatedTime": 1513255482000,
        "registration": null,
        "model": "Quattroporte",
        "type": "car",
        "make": "Maserati",
        "marketCurrency":
        {
            "decimalPlaces": 2,
            "defaultFractionDigits": 2,
            "symbol": "USD",
            "currencyCode": "USD"
        }
    },
    "images": [
    {
        "verified": false,
        "thumbnails":
        {
            "620x372": "https://d1zgdcrdir5wgt.cloudfront.net/media/vehicle/images/nZw5PNEHRV20pm2JLYAHoA.620x372.jpg",
            "50x30": "https://d1zgdcrdir5wgt.cloudfront.net/media/vehicle/images/nZw5PNEHRV20pm2JLYAHoA.50x30.jpg",
            "170x125": "https://d1zgdcrdir5wgt.cloudfront.net/media/vehicle/images/nZw5PNEHRV20pm2JLYAHoA.170x102.jpg",
            "574x343": "https://d1zgdcrdir5wgt.cloudfront.net/media/vehicle/images/nZw5PNEHRV20pm2JLYAHoA.620x372.jpg",
            "170x102": "https://d1zgdcrdir5wgt.cloudfront.net/media/vehicle/images/nZw5PNEHRV20pm2JLYAHoA.170x102.jpg",
            "100x60": "https://d1zgdcrdir5wgt.cloudfront.net/media/vehicle/images/nZw5PNEHRV20pm2JLYAHoA.100x60.jpg"
        },
        "resizableUrlTemplate": "https://d1zgdcrdir5wgt.cloudfront.net/media/vehicle/images/nZw5PNEHRV20pm2JLYAHoA.{width}x{height}.jpg",
        "placeholder": false,
        "id": null,
        "originalImageUrl": "https://d1zgdcrdir5wgt.cloudfront.net/media/vehicle/images/nZw5PNEHRV20pm2JLYAHoA.jpg"
    },
    {
        "verified": false,
        "thumbnails":
        {
            "620x372": "https://d1zgdcrdir5wgt.cloudfront.net/media/vehicle/images/fxG0_Sd0TL6p55sBd4mxYQ.620x372.jpg",
            "50x30": "https://d1zgdcrdir5wgt.cloudfront.net/media/vehicle/images/fxG0_Sd0TL6p55sBd4mxYQ.50x30.jpg",
            "170x125": "https://d1zgdcrdir5wgt.cloudfront.net/media/vehicle/images/fxG0_Sd0TL6p55sBd4mxYQ.170x102.jpg",
            "574x343": "https://d1zgdcrdir5wgt.cloudfront.net/media/vehicle/images/fxG0_Sd0TL6p55sBd4mxYQ.620x372.jpg",
            "170x102": "https://d1zgdcrdir5wgt.cloudfront.net/media/vehicle/images/fxG0_Sd0TL6p55sBd4mxYQ.170x102.jpg",
            "100x60": "https://d1zgdcrdir5wgt.cloudfront.net/media/vehicle/images/fxG0_Sd0TL6p55sBd4mxYQ.100x60.jpg"
        },
        "resizableUrlTemplate": "https://d1zgdcrdir5wgt.cloudfront.net/media/vehicle/images/fxG0_Sd0TL6p55sBd4mxYQ.{width}x{height}.jpg",
        "placeholder": false,
        "id": null,
        "originalImageUrl": "https://d1zgdcrdir5wgt.cloudfront.net/media/vehicle/images/fxG0_Sd0TL6p55sBd4mxYQ.jpg"
    },
    {
        "verified": false,
        "thumbnails":
        {
            "620x372": "https://d1zgdcrdir5wgt.cloudfront.net/media/vehicle/images/3gPCguRtTpGrLxtiEMWzUA.620x372.jpg",
            "50x30": "https://d1zgdcrdir5wgt.cloudfront.net/media/vehicle/images/3gPCguRtTpGrLxtiEMWzUA.50x30.jpg",
            "170x125": "https://d1zgdcrdir5wgt.cloudfront.net/media/vehicle/images/3gPCguRtTpGrLxtiEMWzUA.170x102.jpg",
            "574x343": "https://d1zgdcrdir5wgt.cloudfront.net/media/vehicle/images/3gPCguRtTpGrLxtiEMWzUA.620x372.jpg",
            "170x102": "https://d1zgdcrdir5wgt.cloudfront.net/media/vehicle/images/3gPCguRtTpGrLxtiEMWzUA.170x102.jpg",
            "100x60": "https://d1zgdcrdir5wgt.cloudfront.net/media/vehicle/images/3gPCguRtTpGrLxtiEMWzUA.100x60.jpg"
        },
        "resizableUrlTemplate": "https://d1zgdcrdir5wgt.cloudfront.net/media/vehicle/images/3gPCguRtTpGrLxtiEMWzUA.{width}x{height}.jpg",
        "placeholder": false,
        "id": null,
        "originalImageUrl": "https://d1zgdcrdir5wgt.cloudfront.net/media/vehicle/images/3gPCguRtTpGrLxtiEMWzUA.jpg"
    }],
    "instantBookDisplayed": true,
    "responseRate": null,
    "deliveryLabel": null
}
```

## Web Application

<p align="center">
  <img src="src/mainPage.png"/>
</p>
<i><h3 align="center">Main Page</h3></i>


<p align="center">
  <img src="src/searchByMake.png"/>
</p>
<i><h3 align="center">Search By Make: Tesla</h3></i>

<p align="center">
  <img src="src/specific.png"/>
</p>
<i><h3 align="center">Search Results</h3></i>


## API

<h3 align="center">/api/?filter={}&keyword={}&values={},{}&limit={}</h3>

I wrote the API to make it easier to interact with the dataset.  It's a simple Flask-Based REST API that will return specified vehicle information based on the filters and parameters you use in the URL.  GET and POST methods are both supported.

### Examples:

<h4 align="center">/api/?filter=vehicle_make&keyword=Tesla&values=vehicle_model,rate_daily&limit=5</h4>

```javascript
{
  "data": [
    {
      "rate_daily": 252.0,
      "vehicle_model": "Model S"
    },
    {
      "rate_daily": 140.0,
      "vehicle_model": "Model 3"
    },
    {
      "rate_daily": 116.0,
      "vehicle_model": "Model S"
    },
    {
      "rate_daily": 430.0,
      "vehicle_model": "Model X"
    },
    {
      "rate_daily": 574.0,
      "vehicle_model": "Model X"
    }
  ],
  "success": true
}
```

<h4 align="center">/api/?filter=vehicle_model&keyword=karma&values=vehicle_make,vehicle_model,rate_daily,location_city&limit=3</h4>

```javascript
{
  "data": [
    {
      "location_city": "Stamford",
      "rate_daily": 902.0,
      "vehicle_make": "Fisker",
      "vehicle_model": "Karma"
    },
    {
      "location_city": "Fontana",
      "rate_daily": 717.0,
      "vehicle_make": "Fisker",
      "vehicle_model": "Karma"
    },
    {
      "location_city": "Atlanta",
      "rate_daily": 299.0,
      "vehicle_make": "Fisker",
      "vehicle_model": "Karma"
    }
  ],
  "success": true
}
```

<h4 align="center">/api/?filter=vehicle_id&keyword=412367&values=all&limit=1</h4>

```
{
  "data": [
    {
      "businessClass": "false",
      "deliveryLabel": "FREE DELIVERY",
      "distance": 14.0,
      "distanceLabel": "14 mi",
      "distanceWithUnit_scalar": 14,
      "distanceWithUnit_unit": "MI",
      "distanceWithUnit_unlimited": "false",
      "freeDeliveryPromotion": "false",
      "images_0_id": null,
      "images_0_originalImageUrl": "https://d1zgdcrdir5wgt.cloudfront.net/media/vehicle/images/_KIhWmaxStihwbT_WW9XEQ.jpg",
      "images_0_placeholder": "false",
      "images_0_resizableUrlTemplate": "https://d1zgdcrdir5wgt.cloudfront.net/media/vehicle/images/_KIhWmaxStihwbT_WW9XEQ.{width}x{height}.jpg",
      "images_0_thumbnails_100x60": "https://d1zgdcrdir5wgt.cloudfront.net/media/vehicle/images/_KIhWmaxStihwbT_WW9XEQ.100x60.jpg",
      "images_0_thumbnails_170x102": "https://d1zgdcrdir5wgt.cloudfront.net/media/vehicle/images/_KIhWmaxStihwbT_WW9XEQ.170x102.jpg",
      "images_0_thumbnails_170x125": "https://d1zgdcrdir5wgt.cloudfront.net/media/vehicle/images/_KIhWmaxStihwbT_WW9XEQ.170x102.jpg",
      "images_0_thumbnails_50x30": "https://d1zgdcrdir5wgt.cloudfront.net/media/vehicle/images/_KIhWmaxStihwbT_WW9XEQ.50x30.jpg",
      "images_0_thumbnails_574x343": "https://d1zgdcrdir5wgt.cloudfront.net/media/vehicle/images/_KIhWmaxStihwbT_WW9XEQ.620x372.jpg",
      "images_0_thumbnails_620x372": "https://d1zgdcrdir5wgt.cloudfront.net/media/vehicle/images/_KIhWmaxStihwbT_WW9XEQ.620x372.jpg",
      "images_0_verified": "false",
      "instantBookDisplayed": "false",
      "location_address": "Stamford, CT 06901",
      "location_addressLines_0": "Stamford, CT",
      "location_city": "Stamford",
      "location_country": "US",
      "location_latitude": 41.053547,
      "location_locationSource": "GOOGLE",
      "location_longitude": -73.541023,
      "location_precision_accuracy": 0.09320565,
      "location_precision_level": "APPROXIMATE",
      "location_state": "CT",
      "location_timeZone": "America/New_York",
      "newListing": "false",
      "owner_firstName": "Paula",
      "owner_id": 6049856,
      "owner_image_id": null,
      "owner_image_originalImageUrl": "https://d1zgdcrdir5wgt.cloudfront.net/media/driver/OYh-3gDqQfCcgC72bArw5g.jpg",
      "owner_image_placeholder": "false",
      "owner_image_resizableUrlTemplate": "https://d1zgdcrdir5wgt.cloudfront.net/media/driver/OYh-3gDqQfCcgC72bArw5g.{width}x{height}.jpg",
      "owner_image_thumbnails_225x225": "https://d1zgdcrdir5wgt.cloudfront.net/media/driver/OYh-3gDqQfCcgC72bArw5g.300x300.jpg",
      "owner_image_thumbnails_300x300": "https://d1zgdcrdir5wgt.cloudfront.net/media/driver/OYh-3gDqQfCcgC72bArw5g.300x300.jpg",
      "owner_image_thumbnails_32x32": "https://d1zgdcrdir5wgt.cloudfront.net/media/driver/OYh-3gDqQfCcgC72bArw5g.32x32.jpg",
      "owner_image_thumbnails_84x84": "https://d1zgdcrdir5wgt.cloudfront.net/media/driver/OYh-3gDqQfCcgC72bArw5g.84x84.jpg",
      "owner_image_verified": "false",
      "owner_lastName": "G.",
      "owner_name": "Paula G.",
      "rate_averageDailyPrice": 902.0,
      "rate_averageDailyPriceWithCurrency_amount": 902.0,
      "rate_averageDailyPriceWithCurrency_currencyCode": "USD",
      "rate_daily": 902.0,
      "rate_monthly": 0.3,
      "rate_weekly": 0.15,
      "rating": null,
      "rentableFromSearchedAirport": "false",
      "renterTripsTaken": 0,
      "responseRate": null,
      "responseTime": null,
      "reviewCount": 0,
      "vehicle_automaticTransmission": "true",
      "vehicle_id": 412367,
      "vehicle_image_id": null,
      "vehicle_image_originalImageUrl": "https://d1zgdcrdir5wgt.cloudfront.net/media/vehicle/images/_KIhWmaxStihwbT_WW9XEQ.jpg",
      "vehicle_image_placeholder": "false",
      "vehicle_image_resizableUrlTemplate": "https://d1zgdcrdir5wgt.cloudfront.net/media/vehicle/images/_KIhWmaxStihwbT_WW9XEQ.{width}x{height}.jpg",
      "vehicle_image_thumbnails_100x60": "https://d1zgdcrdir5wgt.cloudfront.net/media/vehicle/images/_KIhWmaxStihwbT_WW9XEQ.100x60.jpg",
      "vehicle_image_thumbnails_170x102": "https://d1zgdcrdir5wgt.cloudfront.net/media/vehicle/images/_KIhWmaxStihwbT_WW9XEQ.170x102.jpg",
      "vehicle_image_thumbnails_170x125": "https://d1zgdcrdir5wgt.cloudfront.net/media/vehicle/images/_KIhWmaxStihwbT_WW9XEQ.170x102.jpg",
      "vehicle_image_thumbnails_50x30": "https://d1zgdcrdir5wgt.cloudfront.net/media/vehicle/images/_KIhWmaxStihwbT_WW9XEQ.50x30.jpg",
      "vehicle_image_thumbnails_574x343": "https://d1zgdcrdir5wgt.cloudfront.net/media/vehicle/images/_KIhWmaxStihwbT_WW9XEQ.620x372.jpg",
      "vehicle_image_thumbnails_620x372": "https://d1zgdcrdir5wgt.cloudfront.net/media/vehicle/images/_KIhWmaxStihwbT_WW9XEQ.620x372.jpg",
      "vehicle_image_verified": "false",
      "vehicle_listingCreatedTime": 1524611104000,
      "vehicle_make": "Fisker",
      "vehicle_marketCountry": "US",
      "vehicle_marketCurrency_currencyCode": "USD",
      "vehicle_marketCurrency_decimalPlaces": "2",
      "vehicle_marketCurrency_defaultFractionDigits": "2",
      "vehicle_marketCurrency_symbol": "USD",
      "vehicle_model": "Karma",
      "vehicle_name": "Paula's Fisker",
      "vehicle_registration": null,
      "vehicle_trim": null,
      "vehicle_type": "car",
      "vehicle_url": "/rentals/cars/ct/stamford/fisker-karma/412367",
      "vehicle_year": 2012
    }
  ],
  "success": true
}
```

## Misc Visualizations


**PS. If Turo is looking for Software Engineering/Data Science Interns for the Spring/Summer of 2019, please let me know.  I would love to join the team in San Francisco :)

My Email: ChristopherLambert106@gmail.com**




