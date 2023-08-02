package app.util;

public class TextProcessor {

   public static String sanitizeStringWithReplace(String inputString) {
      String sanitizedString = inputString.replace("\n", "");
      return sanitizedString;
   }
}
