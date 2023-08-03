package app.log;

public class Constants {
    public static String LOG_PATH = System.getenv("LOG_PATH");
    public static String HDFS_OPTIONS = System.getenv("HDFS_OPTIONS");
    public static String HDFS_PATH = System.getenv("HDFS_PATH");
    public static int HDFS_COMPLETION_SIZE = Integer.parseInt(System.getenv("HDFS_COMPLETION_SIZE"));

    private Constants(){}
}
