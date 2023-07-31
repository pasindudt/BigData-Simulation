package app;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;

import org.apache.camel.Exchange;
import org.apache.camel.Processor;

public class LogFileProcessor implements Processor {

    @Override
    public void process(Exchange exchange) throws Exception {  

        try (BufferedReader reader = new BufferedReader(new InputStreamReader(exchange.getIn().getBody(InputStream.class)))) {
            String line;
            while ((line = reader.readLine()) != null) {
                // exchange.getIn().setHeader("CamelFileName", fileName);
                exchange.getIn().setBody(line);

                exchange.getContext().createProducerTemplate()
                        .send("direct:contentBasedRouter", exchange);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

}
