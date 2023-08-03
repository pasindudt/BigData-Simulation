# BigData-Simulation

## Build Camel Integration
```
cd camel-integration/
mvn clean install
sh build_docker_image.sh
```

## Build Test Data Generator
```
cd test-data-generator/
sh build_docker_image.sh
```

## Build Machine Learning Service
```
cd ml-service/
sh build_docker_image.sh
```

## Build Spark Job
```
cd spark/
sh build_docker_image.sh
```

## Start Docker Services
```
cd docker-services/
sh start_server.sh
```

## Stop Docker Services
```
cd docker-services/
sh stop_server.sh
```