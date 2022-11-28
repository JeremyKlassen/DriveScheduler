# API constants
BASE_URL = "https://api.traveltimeapp.com/v4/routes/V4/routes"
API_ID = "e4519f0a"
API_KEY = "db04e55a43e11768c3ba45fba5736975"

# Database constants
DBPATH = 'src/model/main.db'

# Temp/Test constants
GET_EXAMPLE = """https://api.traveltimeapp.com/v4/routes
?type=public_transport
&origin_lat=51.41070
&origin_lng=-0.15540
&destination_lat=51.59974
&destination_lng=-0.19531
&arrival_time=2022-11-18T16:00:00Z
&app_id=YOUR_APP_ID
&api_key=YOUR_API_KEY"""

POST_EXAMPLE = """POST /v4/routes HTTP/1.1
Host: api.traveltimeapp.com
Content-Type: application/json
Accept: application/json
X-Application-Id: ...
X-Api-Key: ...

{
  "locations": [
    {
      "id": "London center",
      "coords": {
        "lat": 51.508930,
        "lng": -0.131387
      }
    },
    {
      "id": "Hyde Park",
      "coords": {
        "lat": 51.508824,
        "lng": -0.167093
      }
    },
    {
      "id": "ZSL London Zoo",
      "coords": {
        "lat": 51.536067,
        "lng": -0.153596
      }
    }
  ],
  "departure_searches": [
    {
      "id": "departure search example",
      "departure_location_id": "London center",
      "arrival_location_ids": [
        "Hyde Park",
        "ZSL London Zoo"
      ],
      "departure_time": "2022-11-18T15:00:00Z",
      "properties": ["travel_time", "distance", "route"],
      "transportation": {
        "type": "driving"
      }
    }
  ],
  "arrival_searches": [
    {
      "id": "arrival search example",
      "departure_location_ids": [
        "Hyde Park",
        "ZSL London Zoo"
      ],
      "arrival_location_id": "London center",
      "arrival_time": "2022-11-18T16:00:00Z",
      "properties": ["travel_time", "distance", "route", "fares"],
      "transportation": {
        "type": "public_transport",
        "max_changes": {
          "enabled": true,
          "limit": 3
        }
      },
      "range": {
        "enabled": true,
        "max_results": 1,
        "width": 1800
      }
    }
  ]
}"""