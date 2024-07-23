FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

# Expose the port that Django runs on
EXPOSE 8000

CMD ["gunicorn", "weather_project.wsgi:application", "--bind", "0.0.0.0:8000"]

