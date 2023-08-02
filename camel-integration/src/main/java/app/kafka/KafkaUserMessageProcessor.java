package app.kafka;

import org.apache.camel.Exchange;
import org.apache.camel.Processor;

import com.google.gson.Gson;

import static app.kafka.Constants.HDFS_USER_OPTIONS;
import static app.kafka.Constants.HDFS_USER_URL;
import static app.util.TextProcessor.sanitizeStringWithReplace;

public class KafkaUserMessageProcessor implements Processor {
   @Override
   public void process(Exchange exchange){

      String messageJson = exchange.getIn().getBody(String.class);

      Gson gson = new Gson();
      UserMessage message = gson.fromJson(messageJson, UserMessage.class);

      String processedContent;
      String hdfsPath;
      if (message.getAction().equalsIgnoreCase("create")){
         processedContent = new StringBuilder()
                 .append(sanitizeStringWithReplace(message.getData().getUser_id()))
                 .append(',')
                 .append(sanitizeStringWithReplace(message.getData().getUsername()))
                 .append('\n')
                 .toString();

         hdfsPath = HDFS_USER_URL + "users" + HDFS_USER_OPTIONS;

      } else {
         processedContent = new StringBuilder()
                 .append(sanitizeStringWithReplace(message.getData().getUser_id()))
                 .append(',')
                 .append(sanitizeStringWithReplace(message.getAction()))
                 .append('\n')
                 .toString();

         hdfsPath = HDFS_USER_URL + "user_updates" + HDFS_USER_OPTIONS;
      }
      exchange.getContext().createProducerTemplate().sendBodyAndHeader(
              hdfsPath, processedContent, "CamelHdfsAppend", true);
   }
}
