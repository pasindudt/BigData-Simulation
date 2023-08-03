package app.log;

import org.apache.camel.Exchange;
import org.apache.camel.Processor;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.HashMap;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import static app.log.Constants.HDFS_OPTIONS;
import static app.log.Constants.HDFS_PATH;

public class LogErrorHDFSFileProcessor implements Processor {

    @Override
    public void process(Exchange exchange) throws Exception {

        String hdfsFileName = HDFS_PATH + "error_logs" + HDFS_OPTIONS;
        String content = exchange.getIn().getBody(String.class);
        for (String line: content.split("\n")) {
            LogData logData = extractData(line);
            String processedContent = new StringBuilder()
                    .append(logData.timeStamp)
                    .append(',')
                    .append(logData.logLevel)
                    .append(',')
                    .append(logData.errorCode)
                    .append('\n')
                    .toString();

            exchange.getContext().createProducerTemplate().sendBodyAndHeader(
                    hdfsFileName, processedContent, "CamelHdfsAppend", true);
        }
    }

    public static LogData extractData(String logMessage) {
        
        LogData logData = new LogData();

        Pattern logPattern = Pattern.compile("\\[(.*?)\\] (.*?) - .*? Error code: (\\d+)\\.");
        SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");

        Matcher matcher = logPattern.matcher(logMessage);
        if (matcher.find()) {
            String timestampString = matcher.group(1);
            Date timestamp = null;
            try {
                timestamp = dateFormat.parse(timestampString);
            } catch (ParseException e) {
                System.err.println("Error parsing timestamp: " + timestampString);
            }

            String logLevel = matcher.group(2);
            int errorCode = Integer.parseInt(matcher.group(3));

            logData.timeStamp = dateFormat.format(timestamp);
            logData.logLevel = logLevel;
            logData.errorCode = String.valueOf(errorCode);
        } else {
            System.err.println("Invalid log format: " + logMessage);
        }

        return logData;
    }

    public static class LogData {
        public String timeStamp;
        public String logLevel;
        public String errorCode;
    }

}
