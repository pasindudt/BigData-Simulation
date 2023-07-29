package app;


import io.quarkus.runtime.Quarkus;
import io.quarkus.runtime.annotations.QuarkusMain;
import org.apache.camel.CamelContext;
import org.apache.camel.impl.DefaultCamelContext;

import javax.inject.Inject;

import static io.smallrye.config.ConfigLogging.log;

@QuarkusMain
public class Main {


   public static void main(String[] args){

      log.info("Starting application...");

      CamelContext camelContext = new DefaultCamelContext();

      try {
         // Add the route to the context
         camelContext.addRoutes(new DataToHdfsRoute());

         // Start the Camel context
         camelContext.start();
         Quarkus.run(args);

      } catch (Exception e) {
         log.error("Error while running Camel application: " + e.getMessage());
         e.printStackTrace();
      } finally {
         // Stop the Camel context when finished
         try {
            camelContext.stop();
         } catch (Exception e) {
            log.error("Error while stopping Camel context: " + e.getMessage());
            e.printStackTrace();
         }
      }

   }
}
