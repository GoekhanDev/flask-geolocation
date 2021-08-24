# flask-geolocation
Local IP Geolocation API

## Database

The current implementation uses the free [GeoLite2 City](http://dev.maxmind.com/geoip/geoip2/geolite2/) database from MaxMind.

In the past we had databases from other providers, and at some point even our own database comprised of data from different sources. This means it might change in the future.

If you have purchased the commercial database from MaxMind, you can point the freegeoip web server or (Go API, for dev) to the URL containing the file, or local file, and the server will use it.

In case of files on disk, you can replace the file with a newer version and the freegeoip web server will reload it automatically in background. If instead of a file you use a URL (the default), we periodically check the URL in background to see if there's a new database version available, then download the reload it automatically.

All responses from the freegeiop API contain the date that the database was downloaded in the X-Database-Date HTTP header.
