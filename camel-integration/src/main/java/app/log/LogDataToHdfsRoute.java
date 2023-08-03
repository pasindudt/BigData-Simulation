package app.log;

import org.apache.camel.builder.RouteBuilder;

import static app.log.Constants.HDFS_COMPLETION_SIZE;
import static app.log.Constants.LOG_PATH;

public class LogDataToHdfsRoute extends RouteBuilder {

        @Override
        public void configure() {

                log.info("Log Routes Started.....");

                from(LOG_PATH)
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
                                .log("picked up info log from output dir")
                                .aggregate(constant(true), new LogFileAggregationStrategy())
                                .log("info log aggregation")
                                .completionSize(HDFS_COMPLETION_SIZE)
//                                .completionTimeout(5000)
                                .process(new LogInfoHDFSFileProcessor())
                                .log("Info Logs uploaded to HDFS");

                from("file:/output/?fileName=error.log")
                        .log("picked up error log from output dir")
                        .aggregate(constant(true), new LogFileAggregationStrategy())
                        .log("error log aggregation")
                        .completionSize(HDFS_COMPLETION_SIZE)
//                                .completionTimeout(5000)
                        .process(new LogErrorHDFSFileProcessor())
                        .log("Error logs uploaded to HDFS");
        }
}