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


# Model S *Used* Market Prices
| Model   | Market Price   |
| -------------------- |----------:|
|2016.5 AWD 70D | $64,688.71|
|RWD 85 kWh Battery | $59,365.30|
|2016.5 4dr Sedan AWD 60D | $71,496.00|
|90D AWD | $85,877.00|
|AWD 90D Dual Motor | $78,599.00|
|75 RWD | $68,713.08|
|P85D - NAV - SNRF - RRVW | $78,995.00|
|Performance | $54,251.15|
|75D AWD | $78,689.00|
|4dr Sedan Performance | $51,747.00|
|AWD P85D Performance | $71,238.36|
|RWD 70 kWh Battery | $59,738.50|
|2016.5 AWD 90D | $75,068.14|
|P100D AWD | $109,993.00|
|2016.5 4dr Sedan RWD 60 | $61,329.00|
|Sedan | $46,943.38|
|P85D 1 Owner Clean Carfax Autopilot | $76,888.00|
|2016.5 AWD P90D | $94,989.67|
|P85D | $65,309.50|
|4dr Sedan P85D | $65,995.00|
|2016.5 RWD 75 kWh Battery | $66,626.33|
|2016.5 4dr Sedan AWD P100D | $115,561.33|
|100D AWD | $81,497.50|
|2016.5 AWD 75D | $70,492.40|
|4dr Sedan | $46,988.00|
|AWD 70D Dual Motor | $61,823.19|
|4dr Sedan Signature Performance | $48,500.00|
|RWD 60 kWh Battery | $50,832.86|
|4dr Sedan 85 kWh Battery | $52,683.95|
|4dr Sedan Signature | $49,151.60|
|AWD 85D Dual Motor | $64,942.06|

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

## Misc Visualizations


**PS. If Turo is looking for Software Engineering/Data Science Interns for the Spring/Summer of 2019, please let me know.  I would love to join the team in San Francisco :)

My Email: ChristopherLambert106@gmail.com**




