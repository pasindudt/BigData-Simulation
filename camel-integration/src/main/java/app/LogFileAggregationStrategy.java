package app;

import org.apache.camel.AggregationStrategy;
import org.apache.camel.Exchange;

public class LogFileAggregationStrategy implements AggregationStrategy {

    @Override
    public Exchange aggregate(Exchange oldExchange, Exchange newExchange) {
        if (oldExchange == null) {
            StringBuilder buffer = new StringBuilder();
            buffer.append(newExchange.getIn().getBody(String.class));
            newExchange.getIn().setBody(buffer);
            return newExchange;
        } else {
            StringBuilder buffer = oldExchange.getIn().getBody(StringBuilder.class);
            buffer.append(newExchange.getIn().getBody(String.class));
            return oldExchange;
        }
    }
}
