package app;

import org.apache.camel.builder.RouteBuilder;

public class DataToHdfsRoute extends RouteBuilder {

   private static String logPath = System.getenv("LOG_PATH");
   private static String hdfsPath = System.getenv("HDFS_PATH");
   private static String hdfsKafkaPath = System.getenv("HDFS_KAFKA_PATH");
   private static String kafkaPath = System.getenv("KAFKA_PATH"); 


   @Override
   public void configure(){

      log.info("Configuration started.....");

      // log extraction
      from(logPath)
              .log("Picked up")
        //       .convertBodyTo(String.class)
              .process(new LogFileProcessor())
              .to(hdfsPath)
              .log("completed");

      from(kafkaPath)
              .log("Message received from Kafka : ${body}")
              .to(hdfsKafkaPath)
              .log("kafka uploaded to hdfs");
   }
}