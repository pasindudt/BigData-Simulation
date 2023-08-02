package app.kafka;

public class Constants {

   public static String KAFKA_USER_TOPIC_URL = System.getenv("KAFKA_USER_TOPIC_URL");
   public static String HDFS_USER_URL = System.getenv("HDFS_USER_URL");
   public static String HDFS_USER_OPTIONS = System.getenv("HDFS_USER_OPTIONS");

   public static String KAFKA_MOVIE_TOPIC_URL = System.getenv("KAFKA_MOVIE_TOPIC_URL");
   public static String HDFS_MOVIE_URL = System.getenv("HDFS_MOVIE_URL");
   public static String HDFS_MOVIE_OPTIONS = System.getenv("HDFS_MOVIE_OPTIONS");

   public static String KAFKA_CATEGORY_TOPIC_URL = System.getenv("KAFKA_CATEGORY_TOPIC_URL");
   public static String HDFS_CATEGORY_URL = System.getenv("HDFS_CATEGORY_URL");
   public static String HDFS_CATEGORY_OPTIONS = System.getenv("HDFS_CATEGORY_OPTIONS");
}
