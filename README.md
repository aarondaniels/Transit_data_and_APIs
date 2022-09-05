# Transit Data and APIs
A project that creates a transit data application using APIs, MySQL database, Change Data Capture, Maven, and Mapbox. 

## Arcitecture
Web application connected to a server which is connected to [MBTA API](https://api-v3.mbta.com) that feeds location based data from buses. The server will query and store data from MBTA, build an API for clients and also serve the data on demand. 

## Tools / Concepts

### Mapbox
[Mapbox](https://www.mapbox.com) a free library that assists in creating web applications that contain custom maps.
JSON Web Tokens (JWT) will be used to authenticate the mapbox service. More detail regarding how to set up and use Mapbox is noted [here]()

### MBTA API
This is an API from the Massachusetts Bay Transportation Authority. It provides transit data on it's vehicles. In order to enable the full functionality of the API a key is needed and can be acquired by registering on their [website](https://api-v3.mbta.com/). However, for the purposes of this project a key is not needed. Instead, the data can be accessed at this [URL](https://api-v3.mbta.com/vehicles?filter[route]=1&include=trip), which filters the route vehicle type, and trip. Modify the URL for alternate data.  

### Apache Maven
This project will leverage Java to insert records and read data from a MongoDB database. Maven is used to execute the Java code to perform CRUD oeprations on the MongoDB database. More information on Maven has been documented [here](). Additional instruction on performing CRUD operations on a MongoDB using Java is noted [here]().

### How to peel data from the URL

``` python
import urllib.request
import json

#request json file
url = "https://api-v3.mbta.com/vehicles?filter[route]=1&include=trip"
response = urllib.request.urlopen(url).read() #pull data from url
data = json.loads(response) #parse data

#write to console
print(data)
```
Executing the above script will pull data from the website and put it into a JSON. This approach will be used in the server while requesting and pulling information from MBTA. 

## Project Steps
### Create a MySQL database in a Docker container to store data returned by the MBTA API
1. Create network for containers by entering the following command in terminal
```
docker network create MBTANetwork
```

### Make calls to the MBTA API for Route 1 periodically (every 10 seconds). Then, parse the JSON results returned and store the data in the MySQL database for further analysis
- First, analyze the calls made to the MBTA API to view fields and make decisions on which fields are preferable. I have done this using a (Jupyter notebok)[] using the following code: 
``` python
mbtaURL = "https://api-v3.mbta.com/vehicles?filter[route]=1&include=trip"

import urllib.request, json
with urllib.request.urlopen(mbtaURL) as url:
    data = json.loads(url.read().decode())
   
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)
   
    with open('data.txt', 'w') as outfile:
        json.dump(json.dumps(data, indent=4, sort_keys=True), outfile)
       
    print(json.dumps(data, indent=4, sort_keys=True))
```
Add any additional fields to mbta_buses table inside the (the MBTA.sql[] file. Additional information on the MBTA API can be found [here](https://www.mbta.com/developers/v3-api) and via MBTA Swagger [here](https://api-v3.mbta.com/docs/swagger/index.html)
### Perform Change Data Capture (CDC) on the MySQL database and propogate any changes to the MongoDB
1. Create a MongoDB Docker container to be used for CDC. Ensure the MongoDB container is part of the same network as the MySQL container (i.e. MBTANetwork). In this case, the MongoDB container will be called `some-mongo` and will be created using the followingn command in terminal:
```
docker run -p 27017:27017 --name some-mongo --network MBTANetwork -d mongo
```
2. Navigate from a shell prompt to the folder where the docker file is stored and run the Docker command to create a Docker image called `mysqlmbtamasterimg` using the following command: 
```
docker build -t mysqlmbtamasterimg .
```
3. Create a container for MySQL server database using the following command: 
``` 
docker run --rm --name mysqlserver -p 33061:3306 --network MBTANetwork -d mysqlmbtamasterimg
```
*note: the port on the local machine will be 33061 as 3306 is not available.*
### Initialize the Flask server on your local machine 
- The Flask server for this project is captured [here](). 
- Modify the code in the [mysqldb.py]() and [MBTAApiClient.py]() files to include the columns defined in the `mbta_busses` SQL table
- In order to use Mapbox, you will need to create an access token. Follow the instructions at this site to obtain your own access token. With token available, update the [index.html]() file with the access token. 
- From VS Code, run the `server.py` file  **running into error at this point - unable to locate mbtadb despite confirming it exists in docker via mysql workbench** 
- Open a browser window and navigate to localhost:3000

### Allow the server to run for at least 12 hours, storing data in the MySQL database. 