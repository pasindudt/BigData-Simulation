package app.kafka;

import com.google.gson.Gson;
import org.apache.camel.Exchange;
import org.apache.camel.Processor;

import static app.kafka.Constants.HDFS_MOVIE_OPTIONS;
import static app.kafka.Constants.HDFS_MOVIE_URL;
import static app.util.TextProcessor.sanitizeStringWithReplace;
import static app.util.TextProcessor.sanitizeJSONString;

public class KafkaMovieMessageProcessor implements Processor {
   @Override
   public void process(Exchange exchange){

      String messageJson = sanitizeJSONString(exchange.getIn().getBody(String.class));

      Gson gson = new Gson();
      MovieMessage message = gson.fromJson(messageJson, MovieMessage.class);

      String processedContent;
      String hdfsPath;
      if (message.getAction().equalsIgnoreCase("create")){
         processedContent = new StringBuilder()
                 .append(sanitizeStringWithReplace(message.getData().getMovie_id()))
                 .append(',')
                 .append(sanitizeStringWithReplace(message.getData().getTitle()))
                 .append(',')
                 .append(sanitizeStringWithReplace(message.getData().getCategory()))
                 .append('\n')
                 .toString();

         hdfsPath = HDFS_MOVIE_URL + "movies" + HDFS_MOVIE_OPTIONS;

      } else {
         processedContent = new StringBuilder()
                 .append(sanitizeStringWithReplace(message.getData().getMovie_id()))
                 .append(',')
                 .append(sanitizeStringWithReplace(message.getAction()))
                 .append('\n')
                 .toString();

         hdfsPath = HDFS_MOVIE_URL + "movie_updates" + HDFS_MOVIE_OPTIONS;
      }
      exchange.getContext().createProducerTemplate().sendBodyAndHeader(
              hdfsPath, processedContent, "CamelHdfsAppend", true);
   }
}
