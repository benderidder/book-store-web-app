# Learn to create a Python web app 

## Database and migrations
If you not have Docker (desktop for Windows) running on your system install it first.
With the command `docker-compose up` (in project root) you can run the postgres container. On application start all tables will be created automatically and seeded with some example data.
To create a new migration you can run:
```python
flask db migrate -m "YourMigrationName"
```
Next time you start the application your migration will be applied.

For database access and ORM SQLAlchemy is used.

## Controllers
Routes are placed in controllers just like is done in an ASP.NET MVC app. For this blueprints are used.

## CRUD logic
All CRUD operations are placed in the services. This services are instantiated as global instances so they can be used in for all routes.

## Db in extensions
For single instantiation and easy access the db object is instantiated in a separate extensions file.

# Look and feel
For the UI the material design (light) style is used. Further used a central layout for the base of each page. Per page only the title and content are defined. For the grid views a separate reusable grid component is created, so all logic, like search, column sorting and paging is centralized.