# Learn to create a Python web app 

## With Postgres db and migrations
With `docker-compose up` you can run the postgres container in docker.

## Controllers
Routes are placed in controllers just like is done in an ASP.NET MVC app. For this blueprints are used.

## CRUD logic
All CRUD operations are placed in the book_service. This service in instantiated as global instance so it can be used in for all routes.

## Db in extensions
For single instantiation and easy access the db object is instantiated in a separate extensions file.

# Look and feel
For the UI the material design (light) style is used.