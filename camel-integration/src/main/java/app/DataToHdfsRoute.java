package app;

import org.apache.camel.builder.RouteBuilder;

import static app.Constants.logPath;

public class DataToHdfsRoute extends RouteBuilder {

        @Override
        public void configure() {

                log.info("Configuration started.....");

                from(logPath)
                                .log("Picked from input dir")
                                .process(new LogFileProcessor())
                                .log("Processed");

                from("direct:contentBasedRouter")
                                .choice()
                                .when(body().contains("INFO"))
                                .to("file:/output/?fileName=info.log&fileExist=Append")
                                .when(body().contains("ERROR"))
                                .to("file:/output/?fileName=error.log&fileExist=Append")
                                .otherwise()
                                .to("file:/output/?fileName=other.log&fileExist=Append")
                                .end();

                from("file:/output/?fileName=info.log")
                                .log("picked up from output dir")
                                .aggregate(constant(true), new LogFileAggregationStrategy())
                                .log("aggregration")
                                .completionSize(100000) // Set the desired data size (in bytes) for aggregation
//                                .completionTimeout(5000) // Set a timeout for aggregation (optional)
                                .process(new HDFSFileProcessor())
                                .log("Uploaded to HDFS");

                // from(kafkaPath)
                // .log("Message received from Kafka : ${body}")
                // .to(hdfsKafkaPath)
                // .log("kafka uploaded to hdfs");
        }
}