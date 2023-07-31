import sys

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Pass file path as an argument", file=sys.stderr)
        sys.exit(-1)

    spark = SparkSession.builder.appName("MovieAnalysis").getOrCreate()

    schema = StructType([
        StructField("user", StringType(), True),
        StructField("resume", StringType(), True),
        StructField("movie", StringType(), True),
        StructField("genre", StringType(), True)
    ]);

    df = spark.read.csv(sys.argv[1], header=False, schema=schema)

    df.createOrReplaceTempView("movies")

    # Analyze data using SQL queries
    # 1. Count the number of movies per genre
    movies_per_genre = spark.sql("""
        SELECT genre, COUNT(*) AS movie_count
        FROM movies
        GROUP BY genre
        ORDER BY movie_count DESC
    """)
    movies_per_genre.show()

    # 2. Find the most watched movie
    most_watched_movie = spark.sql("""
        SELECT movie, COUNT(*) AS watch_count
        FROM movies
        GROUP BY movie
        ORDER BY watch_count DESC
        LIMIT 1
    """)
    most_watched_movie.show()

    # 3. Find the top users who watched the most movies
    top_users = spark.sql("""
        SELECT user, COUNT(*) AS watch_count
        FROM movies
        GROUP BY user
        ORDER BY watch_count DESC
        LIMIT 5
    """)
    top_users.show()

    spark.stop()
