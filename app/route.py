from app import *
from app.validation import validation

@app.route('/api/geolocation', methods=['GET'])
def geolocation():

    Validate = validation(request.args)

    if Validate != True:
        return Validate

    ip, reader = request.args.get("ip"), geoip2.database.Reader('./data/GeoLite2-City.mmdb')

    return reader.city(ip).raw, 200

