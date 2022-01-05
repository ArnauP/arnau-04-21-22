# Search bar webapp 

This web application consists in a search bar that looks for items in a MongoDB database. 

## Installation

### Requirements

To be able to run locally this project you will need:
* [docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
* [docker-compose](https://docs.docker.com/compose/install/)

### Setup
Build the application with
```
docker-compose build
```

Run the application with
```
docker-compose up -d
```
Stop the application
```
docker-compose down
```
### First steps
In order to have the database ready to go you need to first follow a few steps:
* Connect to the mongodb database through `localhost:27017` using your desired tool.
* Create a database named `db`.
* Create a collection named `garment_items`.
* Import the JSON [garment_items.jl](https://stylr-ai-engine-srv-data.s3.eu-west1.amazonaws.com//srv/data/new_scrapes/shopstyle-1689-men-18-03-2019/garment_items.jl).

## Usage
Once the application is up and running you will have the following URL available:
* Backend: http://localhost:5000
* Frontend: http://localhost:3000

The backend has the following endpoints available:
* `/search`

### Backend query example
```
http://localhost:5000/search?q=shirt
```

## Testing
To run the unit tests execute the following command
```
docker-compose exec backend python -m unittest discover
```

## Developer notes
To run the code linter use
```
docker-compose exec backend flake8
```