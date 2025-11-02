# Book Store - Python CRUD web app

## Story
As an experienced .NET developer, I became curious about the often-discussed Python language. Initially, I thought it was primarily used by data engineers and data scientists, which I am not. However, I soon learned that Python is also widely used for creating web applications, REST APIs, background tasks, and more. This piqued my interest, prompting me to discover why it has become so popular and successful.

I decided to attempt building a CRUD web application similar to a Microsoft ASP.NET MVC application using Entity Framework. I wondered if I could achieve features such as creating migrations, applying them at runtime, implementing dependency injection for services, and setting up controllers to manage routes. Additionally, I aimed to use views for each page with a main layout and styles in separate files, allowing me to apply the DRY (Don't Repeat Yourself) and SRP (Single Responsibility Principle) principles.

The short answer is: yes. In fact, everything I aimed to achieve was not as difficult as I anticipated, especially with access to robust libraries. I must admit that the integration of Co-Pilot in VS Code was also quite helpful. Overall, it truly does not seem challenging to create such an application with Python, even for someone like me, who has grown up with Microsoft and .NET.

## Application Architecture Overview 

### Database and Migrations
If you do not have Docker (Desktop for Windows) running on your system, please install it first. You can start the PostgreSQL container by running the command 'docker-compose up` in the project root. Upon application startup, all tables will be created automatically and seeded with example data.

To add models (tables) to your database, add them to the data/models.py file. To create a new migration for it, execute the following command:

```bash
flask db migrate -m "YourMigrationName"
```

The next time you start the application, your migration will be applied.

For database access and Object-Relational Mapping (ORM), SQLAlchemy is utilized.

### Controllers
Routes are organized in controllers, similar to how it is done in an ASP.NET MVC application. Blueprints are used for this purpose.

### CRUD Logic
All CRUD operations are contained within services. These services are instantiated as global instances, making them accessible across all routes.

### Database in Extensions
To ensure a single instantiation and easy access, the database object is instantiated in a separate extensions file.

### Look and Feel
The user interface employs a Material Design (light) style. A central layout serves as the foundation for each page, with only the title and content defined per page. For grid views, a separate reusable grid component has been created, centralizing all logic such as search, column sorting, and pagination.