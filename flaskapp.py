from flask import Flask, render_template
from flask_googlemaps import GoogleMaps, Map, icons
import requests
import json

app = Flask(__name__)

app.config['GOOGLEMAPS_KEY'] = "AIzaSyB4ipnj_JcaXKHFruw172nwitgJWdcV9Fk"
GoogleMaps(app)


@app.route('/')
def mapview():
    
    output = []

    r = requests.get("https://api.jcdecaux.com/vls/v1/stations?contract=Dublin&apiKey=c64916b14c557faa49fdf72b8902e4d9ff9afe35")
    data = r.json()
    #note this data is actually a list of elements....

    #35 is another smithfield station
    infobox = "Dublin Bike Station" + "</br>" + "Name: " + str(data[0]["name"]) + "<br/>" + "Status: " + str(data[0]["status"]) + "<br/>" + "Available Stands: " + str(data[0]["available_bike_stands"]) + "</br>" + "Available Bikes: " + str(data[0]["available_bikes"])

    latitude = data[0]["position"]["lat"]
    longitude = data[0]["position"]["lng"]
    
    output.append(
            {	
	    	'icon': icons.dots.blue,
		'lat': data[0]["position"]["lat"],
		'lng': data[0]["position"]["lng"],
		'infobox': infobox
	    }
	)

    trdmap = Map(
        identifier="trdmap",
	lat=53.350140,
	lng=-6.266155,
	style="height:600px;width:800px;color:black",
	markers=output
	)

    return render_template('index.html', trdmap=trdmap)


if __name__ == "__main__":
    app.run()
