package app.kafka;

import org.apache.camel.builder.RouteBuilder;

import static app.kafka.Constants.KAFKA_CATEGORY_TOPIC_URL;
import static app.kafka.Constants.KAFKA_MOVIE_TOPIC_URL;
import static app.kafka.Constants.KAFKA_USER_TOPIC_URL;

public class KafkaDataToHdfsRoute extends RouteBuilder {

   @Override
   public void configure() {

      log.info("Kafka Routes Started.....");

      from(KAFKA_USER_TOPIC_URL)
              .log("Message received from Kafka Topic (User) : ${body}")
              .process(new KafkaUserMessageProcessor())
              .log("Message uploaded to hdfs (User)");

      from(KAFKA_MOVIE_TOPIC_URL)
              .log("Message received from Kafka Topic (Movie) : ${body}")
              .process(new KafkaMovieMessageProcessor())
              .log("Message uploaded to hdfs (Movie)");

      from(KAFKA_CATEGORY_TOPIC_URL)
              .log("Message received from Kafka Topic (Category) : ${body}")
              .process(new KafkaCategoryMessageProcessor())
              .log("Message uploaded to hdfs (Category)");

   }
}