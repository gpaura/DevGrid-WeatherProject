# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Set environment variables for Django
ENV DJANGO_SETTINGS_MODULE=weather_project.settings
ENV PYTHONUNBUFFERED 1

# Expose port 8000 for the app
EXPOSE 8000

# Run database migrations and then start the application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "weather_project.wsgi:application"]

RUN pip install dj-database-url
