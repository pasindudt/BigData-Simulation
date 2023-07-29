FROM alpine

RUN apk add bash

RUN mkdir -p /usr/lib/jvm/

RUN wget https://aka.ms/download-jdk/microsoft-jdk-11.0.19-alpine-x64.tar.gz \
    && tar -xf microsoft-jdk-11.0.19-alpine-x64.tar.gz -C /usr/lib/jvm/ \
    && rm microsoft-jdk-11.0.19-alpine-x64.tar.gz

ENV JAVA_HOME=/usr/lib/jvm/jdk-11.0.19+7
ENV PATH=$PATH:$JAVA_HOME/bin

COPY target/quarkus-app/lib/ /deployments/lib/
COPY target/quarkus-app/*.jar /deployments/
COPY target/quarkus-app/app/ /deployments/app/
COPY target/quarkus-app/quarkus/ /deployments/quarkus/

RUN mkdir /log_location

CMD ["java", "-jar", "/deployments/quarkus-run.jar"]