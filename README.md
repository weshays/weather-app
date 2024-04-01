# Weather

This project is an app that intereacts with the OpenWeatherMap API to get the weather for a given city.

## Description

This app is a practice project to learn how to interact with APIs with Python 3 and dJango 5. It is a simple app that allows the user to input a city name and get the current weather for that city.

## Installing and getting the project running

This project is meant to run in a docker container.

### System Dependencies

- Docker

### Setup project

Clone the project to your local machine.

```
git clone git@github.com:weshays/weather-app.git
```

### Build the project

You will only need to run this once to build the project.

```
docker-compose build
```

### Run the project

Once you have the project build you will only ever need to run the following command.

```
docker-compose up
```

When you are done you can stop the project by running the following command.

```
docker-compose down
```

### Access the project

Once the project is running you can access the project by going to
http://localhost:8000
in your browser

If successful you should see a HelloWorld page


## NOTES

Build the *project* in the container without having to install/upgrade Python or Django on your local machine.

```
docker-compose build
docker-compose run --rm app sh -c "django-admin startproject app ."
```

Build an *app* in the container without having to install/upgrade Python or Django on your local machine.

```
# docker-compose run --rm app sh -c "python manage.py startapp [app_name]"
docker-compose run --rm app sh -c "python manage.py startapp temperature"
```

## Run migrations

You can run migrations inside the container by logging into the container and running the following commands.

```
docker exec -it weather-app bash
python manage.py makemigrations
python manage.py migrate
```

Or, you can run migrations outside of the container by running the following command.

```
docker-compose run --rm app sh -c "python manage.py makemigrations"
docker-compose run --rm app sh -c "python manage.py migrate"
```