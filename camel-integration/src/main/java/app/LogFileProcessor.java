package app;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;

import org.apache.camel.Exchange;
import org.apache.camel.Processor;

public class LogFileProcessor implements  Processor {

    @Override
    public void process(Exchange exchange) throws Exception {

        // Get the input stream from the exchange (stream-based processing)
        BufferedReader reader = new BufferedReader(new InputStreamReader(exchange.getIn().getBody(InputStream.class)));

        // Prepare a StringBuilder to collect the extracted lines
        StringBuilder extractedLines = new StringBuilder();

        // Process the file line by line
        String line;
        while ((line = reader.readLine()) != null) {
            if (line.startsWith("START")) {
                extractedLines.append(line).append("\n");
            }
        }

        // Set the extracted lines as the new body to be further processed or saved
        exchange.getIn().setBody(extractedLines.toString());
    }

}
