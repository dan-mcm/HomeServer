# Home Server Application

A [Flask](http://flask.pocoo.org/) application that displays useful data on nearby services based on multiple API calls.

Initially setup as a project running on my home network from the Raspberry Pi.

## Shows the following
- Nearby Bus Data (Dublin Bus API)
- Nearby Bike Data (Dublin Bikes API)
- Google Maps (Google Maps API)
- Google Calendar (Google Calendar API)
- GiantBomb Facebook Feed (Facebook API)
- Current Weather (Open Weather Map API)

## To run locally

```
export FLASK_APP=flaskapp.py (windows: set FLASK_APP=flaskapp.py)
flask run
```
