package app;

import static app.Constants.hdfsPath;
import static app.Constants.hdfsOptions;

import org.apache.camel.Exchange;
import org.apache.camel.Processor;

public class HDFSFileProcessor implements Processor {

    @Override
    public void process(Exchange exchange) throws Exception {

        String hdfsFileName = hdfsPath + "logs" + hdfsOptions;

        // + exchange.getIn().getHeader("CamelFileName", String.class);
        String content = exchange.getIn().getBody(String.class);

        exchange.getContext().createProducerTemplate().sendBodyAndHeader(
                hdfsFileName, content, "CamelHdfsAppend", true);
    }

}
