package app;

import app.kafka.KafkaDataToHdfsRoute;
import app.log.LogDataToHdfsRoute;
import io.quarkus.runtime.Quarkus;
import io.quarkus.runtime.annotations.QuarkusMain;
import org.apache.camel.CamelContext;
import org.apache.camel.impl.DefaultCamelContext;

import static io.smallrye.config.ConfigLogging.log;

@QuarkusMain
public class Main {

   public static void main(String[] args){

      log.info("Starting application...");

      try (CamelContext camelContext = new DefaultCamelContext();){

         // Add the routes to the context
         camelContext.addRoutes(new LogDataToHdfsRoute());
         camelContext.addRoutes(new KafkaDataToHdfsRoute());

         // Start the Camel context
         camelContext.start();

         // Start Quarkus app
         Quarkus.run(args);

      } catch (Exception e) {
         log.error("Error occurred while application start", e);
      }

   }
}
