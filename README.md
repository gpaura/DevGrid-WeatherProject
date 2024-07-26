# DevGrid Weather Project

## Introduction
The DevGrid Weather Project is an application designed to collect and display real-time weather data. The project leverages modern technologies and best practices to ensure performance and scalability.

Technologies Used
Django
Django was chosen as the framework for this application due to the following reasons:

- Rapid Development: Django is known for its ability to accelerate web application development with its "batteries-included" approach and a rich library of ready-to-use components.
Security: Django offers various security features such as protection against CSRF, SQL Injection, and XSS, which helps build more secure applications.
Admin Interface: Django’s built-in admin interface simplifies data management and system administration without creating an admin interface from scratch.
Scalability: Django's architecture is designed to handle large-scale applications, which is crucial for projects that may grow over time.
PostgreSQL
PostgreSQL was chosen as the relational database management system (RDBMS) for data storage due to:

- Performance: PostgreSQL is known for its high performance and scalability.
Advanced Features: It offers advanced features like ACID transaction support, extensibility, and support for complex data types.
Community: It has an active community and extensive documentation and support tools.
Docker
Docker was used to containerize the application and the database, providing a consistent and isolated environment for development and production. This simplifies the configuration and management of the involved services:

- Consistency: Ensures that the application and its dependencies run the same way across different environments.
Ease of Deployment: Simplifies the deployment process, making it faster and less error-prone.
Project Structure
The project is organized as follows:

weather_project/: The main directory containing the Django configuration file and the manage.py file.
weather_service/: The Django application contains the core logic, including models, views, and URLs.
docker-compose.yml: Docker Compose configuration file that defines and runs the containers for the application and the database.
Dockerfile: Configuration file for creating the Docker image of the Django application.
Setup and Running
Clone the Repository


git clone https://github.com/gpaura/DevGrid-WeatherProject.git
cd DevGrid-WeatherProject
Start the Containers

Make sure Docker and Docker Compose are installed, then run:

bash
Copy code
docker-compose up
This will start the containers for the Django application and PostgreSQL database.

Run Migrations

After starting the containers, run the migrations to set up the database:

bash
Copy code
docker-compose exec web python manage.py migrate
Access the Application

The application will be available at http://localhost:8000.

Contributing
If you want to contribute to this project, please open an issue or submit a pull request with your changes.

License
This project is licensed under the MIT License.



- Generating and Viewing Results
The application provides endpoints to fetch weather data in JSON format. Here’s how to interact with the API to generate and view results:

Fetch Weather Data
Collect Weather Data

To collect weather data, you can use the endpoint:


POST http://localhost:8000/weather/collect/
This will trigger the collection of weather data based on the configured sources.

- Get Weather Data Progress

To check the progress of the data collection, you can use the endpoint:

GET http://localhost:8000/weather/progress/
Retrieve Collected Weather Data

To retrieve the collected weather data, use the following endpoint:


GET http://localhost:8000/weather/data/
This will return the weather data in JSON format. Example response:

json
[
    {
        "city": "New York",
        "temperature": "21°C",
        "humidity": "56%",
        "timestamp": "2024-07-26T12:00:00Z"
    },
    {
        "city": "London",
        "temperature": "15°C",
        "humidity": "72%",
        "timestamp": "2024-07-26T12:00:00Z"
    }
]
Example of JSON Output
Here’s an example of the JSON output you can expect:

json
Copy code
{
    "status": "success",
    "data": [
        {
            "city": "San Francisco",
            "temperature": "18°C",
            "humidity": "65%",
            "timestamp": "2024-07-26T12:00:00Z"
        },
        {
            "city": "Tokyo",
            "temperature": "27°C",
            "humidity": "80%",
            "timestamp": "2024-07-26T12:00:00Z"
        }
    ]
}
Troubleshooting
No Data Returned: Ensure that the data collection process has been completed successfully by checking the progress endpoint.
API Errors: Check the application logs for any errors or issues with the endpoints.
Make sure to adjust the endpoint URLs and example data according to your specific setup and project details.


## Generating and Viewing Results

The application provides endpoints to fetch weather data in JSON format. Here’s how to interact with the API to generate and view results:

### Fetch Weather Data

1. **Collect Weather Data**

   To collect weather data, you can use the endpoint:

POST http://localhost:8000/weather/collect/

sql
Copy code

This will trigger the collection of weather data based on the configured sources.

2. **Get Weather Data Progress**

To check the progress of the data collection, you can use the endpoint:

GET http://localhost:8000/weather/progress/

markdown
Copy code

3. **Retrieve Collected Weather Data**

To retrieve the collected weather data, use the following endpoint:

GET http://localhost:8000/weather/data/

kotlin
Copy code

This will return the weather data in JSON format. Example response:

```json
[
    {
        "city": "New York",
        "temperature": "21°C",
        "humidity": "56%",
        "timestamp": "2024-07-26T12:00:00Z"
    },
    {
        "city": "London",
        "temperature": "15°C",
        "humidity": "72%",
        "timestamp": "2024-07-26T12:00:00Z"
    }
]
Example of JSON Output
Here’s an example of the JSON output you can expect:

json
Copy code
{
    "status": "success",
    "data": [
        {
            "city": "San Francisco",
            "temperature": "18°C",
            "humidity": "65%",
            "timestamp": "2024-07-26T12:00:00Z"
        },
        {
            "city": "Tokyo",
            "temperature": "27°C",
            "humidity": "80%",
            "timestamp": "2024-07-26T12:00:00Z"
        }
    ]
}
Troubleshooting
No Data Returned: Ensure that the data collection process has been completed successfully by checking the progress endpoint.
API Errors: Check the application logs for any errors or issues with the endpoints.
