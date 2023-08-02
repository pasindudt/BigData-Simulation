package app.kafka;

import com.google.gson.Gson;
import org.apache.camel.Exchange;
import org.apache.camel.Processor;

import static app.kafka.Constants.HDFS_CATEGORY_OPTIONS;
import static app.kafka.Constants.HDFS_CATEGORY_URL;

import static app.util.TextProcessor.sanitizeStringWithReplace;

public class KafkaCategoryMessageProcessor implements Processor {
   @Override
   public void process(Exchange exchange){

      String messageJson = exchange.getIn().getBody(String.class);

      Gson gson = new Gson();
      CategoryMessage message = gson.fromJson(messageJson, CategoryMessage.class);

      String processedContent;
      String hdfsPath;
      if (message.getAction().equalsIgnoreCase("create")){
         processedContent = new StringBuilder()
                 .append(sanitizeStringWithReplace(message.getData().getCategory_id()))
                 .append(',')
                 .append(sanitizeStringWithReplace(message.getData().getName()))
                 .append('\n')
                 .toString();

         hdfsPath = HDFS_CATEGORY_URL + "categories" + HDFS_CATEGORY_OPTIONS;

      } else {
         processedContent = new StringBuilder()
                 .append(sanitizeStringWithReplace(message.getData().getCategory_id()))
                 .append(',')
                 .append(sanitizeStringWithReplace(message.getAction()))
                 .append('\n')
                 .toString();

         hdfsPath = HDFS_CATEGORY_URL + "category_updates" + HDFS_CATEGORY_OPTIONS;
      }
      exchange.getContext().createProducerTemplate().sendBodyAndHeader(
              hdfsPath, processedContent, "CamelHdfsAppend", true);
   }
}
