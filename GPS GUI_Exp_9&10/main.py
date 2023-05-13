from flask import Flask,render_template
import geocoder
import folium
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="MyApp")

g = geocoder.ip('me')
print(g.latlng)
coordinates=g.latlng
location = geolocator.reverse(coordinates)

address = location.raw['address']

city = address.get('city', '')
state = address.get('state', '')
country = address.get('country', '')
print(city,state,country)
m = folium.Map(location=(coordinates[0],coordinates[1]), tiles="cartodb positron")
folium.Marker(location=[coordinates[0], coordinates[1]],popup="Your Here").add_to(m)

m.save("templates/footprint.html")
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html',hide='0')

@app.route('/gps')
def gps():
    return render_template('index.html',hide='1',gps='1',gpscoord=str(coordinates),location=city+" "+state+" "+country)
@app.route('/map')
def map():
    return render_template('footprint.html')
if __name__=="__main__":
    app.run(debug=True)