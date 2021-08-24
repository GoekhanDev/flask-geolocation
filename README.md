# flask-geolocation

A Free Local/offline geolocation API with accurate information and fast response.

## Requirements
 ```bash 
 pip install -r requirements.txt
```
## API

The API has only one endpoint to retrive geolocation information.

Example:

```bash
curl localhost/api/geolocation?ip=8.8.8.8
```
> Returns the geolocation information of 8.8.8.8.

## Database

The current implementation uses the free [GeoLite2 City](http://dev.maxmind.com/geoip/geoip2/geolite2/) database from MaxMind.

A License Key is required which is obtainable free at [Maxmind](https://www.maxmind.com/en/accounts/current/license-key).

<br/>
<br/>
<a href="https://www.buymeacoffee.com/GoekhanA" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-blue.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 100px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>


