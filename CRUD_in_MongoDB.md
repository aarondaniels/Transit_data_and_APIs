# Executing CRUD operations in MongoDB
This project will perform CRUD (create, read, update, delete) operations in a MongoDB using Java. This is an outline of how that will work within the context of this project. For additional detail/instruction, follow [this tutorial](https://www.mongodb.com/developer/languages/java/java-setup-crud-operations/) provided by MongoDB.

## First, create a Docker container:
1. Create a Docker network for your containers called `MBTANetwork`. From a command prompt, run the following command to create the network:
``` 
docker network create MBTANetwork
```
Note that, like MongoDB, Redis does not need to be initialized.

2. Create a container running the MongoDB database and associate the container with the MBTANetwork network. The container name is `some-mongo`. From the command prompt, run the following command to create a MongoDB container:
```
docker run -p 27017:27017 --name some-mongo --network MBTANetwork  -d mongo 
```
3. From the command prompt, run the following command to create a Docker Java Maven container:
```
docker run --name javamaven --network MBTANetwork  -dti --rm -p 8080:8080 maven:3.6.3-openjdk-11 bash
```
4. Use the git command below to download the MongoDB Java classes provided in the tutorial:
```
git clone https://github.com/mongodb-developer/java-quick-start
```
5. From the command prompt, navigate to the parent directory of the java-quick-start folder and run a Docker command to copy the contents of this folder to the javamaven Docker container:
```
docker cp java-quick-start javamaven:/
```
6. Run a bash command prompt by selecting <CLI> from the javamaven Docker desktop. Alternatively, enter the following in terminal to access the Docker CLI:
```
docker exec -it javamaven /bin/bash
```
7. From the bash prompt, list the files under the root directory (/). You should see that the `java-quick-start` folder was copied to that directory:
8. Install the nano text editor:
```
apt-get update
```
```
apt-get install nano
```

## Second, run each class:
1. From the bash command prompt, make sure that you are in the java-quick-start directory and run the following command:
```
mvn compile exec:java -Dexec.mainClass="com.mongodb.quickstart.HelloMongoDB"
```
2. Next, connect to the MongoDB database. From the bash command prompt, make sure that you are in the `java-quick-start` directory and run the following command:
```
mvn compile exec:java -Dexec.mainClass="com.mongodb.quickstart.Connection" -Dmongodb.uri="mongodb://some-mongo:27017"
```
Note: In this command, you are passing the container name as part of the MongoDB URL because you are running MongoDB inside a container.

You are now ready to run all of the classes in the tutorial.