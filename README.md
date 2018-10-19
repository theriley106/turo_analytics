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

### Valid Search Parameters

| Parameters | (cont.) |
| --- | --- |
| vehicle_image_originalImageUrl | rating |
| reviewCount | owner_image_thumbnails_225x225 |
| owner_name | location_precision_accuracy |
| renterTripsTaken | vehicle_name |
| location_addressLines_0 | location_timeZone |
| vehicle_image_resizableUrlTemplate | rate_monthly |
| images_0_thumbnails_100x60 | distanceLabel |
| location_locationSource | vehicle_marketCountry |
| rate_weekly | rate_averageDailyPrice |
| owner_id | vehicle_listingCreatedTime |
| location_address | vehicle_marketCurrency_decimalPlaces |
| images_0_resizableUrlTemplate | owner_image_id |
| vehicle_registration | vehicle_marketCurrency_currencyCode |
| vehicle_image_thumbnails_170x125 | images_0_thumbnails_170x125 |
| responseTime | images_0_id |
| businessClass | rate_averageDailyPriceWithCurrency_currencyCode |
| vehicle_marketCurrency_symbol | images_0_thumbnails_574x343 |
| distanceWithUnit_unit | owner_lastName |
| vehicle_type | rate_averageDailyPriceWithCurrency_amount |
| owner_image_verified | vehicle_image_verified |
| vehicle_image_thumbnails_620x372 | location_city |
| newListing | vehicle_id |
| distance | location_country |
| images_0_thumbnails_620x372 | vehicle_image_thumbnails_50x30 |
| owner_image_resizableUrlTemplate | location_precision_level |
| distanceWithUnit_scalar | owner_image_thumbnails_84x84 |
| location_state | location_longitude |
| vehicle_trim | owner_image_placeholder |
| images_0_thumbnails_170x102 | vehicle_make |
| vehicle_automaticTransmission | images_0_verified |
| vehicle_image_thumbnails_100x60 | images_0_originalImageUrl |
| distanceWithUnit_unlimited | images_0_thumbnails_50x30 |
| freeDeliveryPromotion | owner_image_thumbnails_32x32 |
| vehicle_image_thumbnails_574x343 | vehicle_url |
| vehicle_image_id | rentableFromSearchedAirport |
| owner_image_thumbnails_300x300 | vehicle_marketCurrency_defaultFractionDigits |
| location_latitude | responseRate |
| owner_firstName | vehicle_image_placeholder |
| vehicle_image_thumbnails_170x102 | owner_image_originalImageUrl |
| instantBookDisplayed | rate_daily |
| vehicle_model | deliveryLabel |
| images_0_placeholder | vehicle_year |

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

```javascript
Endpoint: /api/?filter=vehicle_make&keyword=Tesla&values=vehicle_model,rate_daily&limit=5

Response:
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

```javascript
Endpoint: /api/?filter=vehicle_model&keyword=karma&values=vehicle_make,vehicle_model,rate_daily,location_city&limit=3

Response:
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

```
Endpoint: /api/?filter=vehicle_id&keyword=412367&values=vehicle_model,vehicle_make,rate_daily,location_longitude,location_latitude,vehicle_year

Response:
{
  "data": [
    {
      "location_latitude": 41.053547,
      "location_longitude": -73.541023,
      "rate_daily": 902.0,
      "vehicle_make": "Fisker",
      "vehicle_model": "Karma",
      "vehicle_year": 2012
    }
  ],
  "success": true
}
```

```javascript
Endpoint: /api/?filter=vehicle_make&keyword=Tesla&values=vehicle_name&limit=10

Response:
{
  "data": [
    {
      "vehicle_name": "Jim's Tesla"
    },
    {
      "vehicle_name": "Ken's Tesla Model 3"
    },
    {
      "vehicle_name": "Nathan's Tesla"
    },
    {
      "vehicle_name": "Lei's Tesla"
    },
    {
      "vehicle_name": "Megan's Tesla"
    },
    {
      "vehicle_name": "GSD Rides Maui Tesla Rental Model S P85+"
    },
    {
      "vehicle_name": "Daniel's Tesla Model 3"
    },
    {
      "vehicle_name": "Daniel's Tesla Model S"
    },
    {
      "vehicle_name": "Gavin's Tesla"
    },
    {
      "vehicle_name": "Travis's Tesla"
    }
  ],
  "success": true
}
```

## Misc Visualizations


## Interesting Findings (Info is current to 07/08/2018)

- Matias's Lamborghini Huracan is the most expensive car on Turo with a daily rate of $1140.00

**PS. If Turo is looking for Software Engineering/Data Science Interns for the Spring/Summer of 2019, please let me know.  I would love to join the team in San Francisco :)

My Email: ChristopherLambert106@gmail.com**




