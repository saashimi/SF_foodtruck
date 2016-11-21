# SF Foodtruck Locator Application

This is a web application inspired by an Uber code challenge. Namely, how to use
Socrata API data and display it so that a user can find foodtrucks in San Francisco
within a half-mile radius from an input location.

## Development Stack
This project uses PostgreSQL 9.5 and PostGIS for spatial lookups. The Django 1.10.3 
makes navigating the geographic data much easier, especially with gdal tools. Django-leaflet 0.19 is used for the frontend. 

## Screenshot
![alt tag](https://github.com/saashimi/SF_foodtruck/blob/dev/screenshot.gif)  
