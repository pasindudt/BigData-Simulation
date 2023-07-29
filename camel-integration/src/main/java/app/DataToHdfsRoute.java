package app;

import org.apache.camel.builder.RouteBuilder;

public class DataToHdfsRoute extends RouteBuilder {

   private static String logPath = System.getenv("LOG_PATH"); // file:/log_location/
   private static String hdfsPath = System.getenv("HDFS_PATH"); // hdfs://namenode:9000/data/?replication=1

   @Override
   public void configure(){

      log.info("Configuration started.....");

      // log extraction
      from(logPath)
              .log("Picked up")
              .to(hdfsPath)
              .log("completed");
   }
}