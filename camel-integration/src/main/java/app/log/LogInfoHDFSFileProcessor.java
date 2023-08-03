package app.log;

import static app.log.Constants.HDFS_PATH;
import static app.log.Constants.HDFS_OPTIONS;

import java.util.HashMap;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import org.apache.camel.Exchange;
import org.apache.camel.Processor;

public class LogInfoHDFSFileProcessor implements Processor {

    @Override
    public void process(Exchange exchange) throws Exception {

        String hdfsFileName = HDFS_PATH + "logs" + HDFS_OPTIONS;
        String content = exchange.getIn().getBody(String.class);
        for (String line: content.split("\n")) {
            LogData logData = extractData(line);
            String processedContent = new StringBuilder()
                    .append(logData.user)
                    .append(',')
                    .append(logData.action)
                    .append(',')
                    .append(logData.movie)
                    .append(',')
                    .append(logData.category)
                    .append('\n')
                    .toString();

            exchange.getContext().createProducerTemplate().sendBodyAndHeader(
                    hdfsFileName, processedContent, "CamelHdfsAppend", true);
        }
    }

    public static LogData extractData(String logMessage) {
        
        LogData logData = new LogData();

        String userPattern = "User \"([^\"]+)\"";
        String moviePattern = "watching \"([^\"]+)\"";
        String categoryPattern = "searched for \"([^\"]+)\"";

        // Extract user
        Pattern userRegex = Pattern.compile(userPattern);
        Matcher userMatcher = userRegex.matcher(logMessage);
        if (userMatcher.find()) {
            logData.user = userMatcher.group(1);
        }

        // Extract action
        Map<String, String> actionMap = new HashMap<>();
        actionMap.put("login", "logged in successfully.");
        actionMap.put("search", "searched for");
        actionMap.put("visit", "visited the");
        actionMap.put("start", "started watching");
        actionMap.put("pause", "paused watching");
        actionMap.put("resume", "resumed watching");

        for (Map.Entry<String, String> entry : actionMap.entrySet()) {
            if (logMessage.contains(entry.getValue())) {
                logData.action = entry.getKey();
                break;
            }
        }

        // Extract movie
        Pattern movieRegex = Pattern.compile(moviePattern);
        Matcher movieMatcher = movieRegex.matcher(logMessage);
        if (movieMatcher.find()) {
            logData.movie = movieMatcher.group(1);
        }

        // Extract category
        Pattern categoryRegex = Pattern.compile(categoryPattern);
        Matcher categoryMatcher = categoryRegex.matcher(logMessage);
        if (categoryMatcher.find()) {
            logData.category = categoryMatcher.group(1);
        }

        return logData;
    }

    public static class LogData {
        public String user;
        public String action;
        public String movie;
        public String category;
    }

}
