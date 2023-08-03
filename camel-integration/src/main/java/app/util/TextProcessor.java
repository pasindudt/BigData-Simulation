package app.util;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;

public class TextProcessor {

   public static String sanitizeStringWithReplace(String inputString) {
      String sanitizedString = inputString.replace("\n", "");
      return sanitizedString;
   }
   public static String sanitizeJSONString(String input) {
      // Check if the input starts and ends with double quotes
      if (input.startsWith("\"") && input.endsWith("\"")) {
         // Extract the substring in between the leading and ending double quotes
         input = input.substring(1, input.length() - 1);
      }

      // Remove the backslash character
      return input.replaceAll("\\\\", "");

   }
}
