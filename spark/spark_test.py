import sys

import requests
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType


def get_sentiment_score(data):
    url = sys.argv[7]
    response = requests.post(url, data=data)
    if response.status_code == 200:
        result = response.json()
        return result['score']


if __name__ == "__main__":
    print(len(sys.argv))
    if len(sys.argv) != 8:
        print("Invalid arguments", file=sys.stderr)
        sys.exit(-1)

    spark = SparkSession.builder.appName("MovieAnalysis").getOrCreate()

    user_schema = StructType([
        StructField("user_id", StringType(), True),
        StructField("user_name", StringType(), True)
    ]);

    category_schema = StructType([
        StructField("category_id", StringType(), True),
        StructField("category_name", StringType(), True)
    ]);

    movie_schema = StructType([
        StructField("movie_id", StringType(), True),
        StructField("movie_name", StringType(), True),
        StructField("category_id", StringType(), True)
    ]);

    log_schema = StructType([
        StructField("user_id", StringType(), True),
        StructField("action", StringType(), True),
        StructField("movie_id", StringType(), True),
        StructField("category_id", StringType(), True)
    ]);

    error_log_schema = StructType([
        StructField("timestamp", StringType(), True),
        StructField("log_level", StringType(), True),
        StructField("error_code", StringType(), True)
    ]);

    review_schema = StructType([
        StructField("user_id", StringType(), True),
        StructField("movie_id", StringType(), True),
        StructField("review", StringType(), True)
    ]);

    user_df = spark.read.csv(sys.argv[1], header=False, schema=user_schema)
    category_df = spark.read.csv(sys.argv[2], header=False, schema=category_schema)
    movie_df = spark.read.csv(sys.argv[3], header=False, schema=movie_schema)
    log_df = spark.read.csv(sys.argv[4], header=False, schema=log_schema)
    error_log_df = spark.read.csv(sys.argv[5], header=False, schema=error_log_schema)
    review_df = spark.read.csv(sys.argv[6], header=False, schema=review_schema)

    user_df.createOrReplaceTempView("users")
    category_df.createOrReplaceTempView("categories")
    movie_df.createOrReplaceTempView("movies")
    log_df.createOrReplaceTempView("logs")
    error_log_df.createOrReplaceTempView("error_logs")
    review_df.createOrReplaceTempView("reviews")

    top_movies = spark.sql("""
        SELECT movies.movie_name, top_movies_tab.interaction_count
        FROM (SELECT movie_id, COUNT(*) as interaction_count
        FROM logs
        WHERE action IN ('resume', 'start')
        GROUP BY movie_id
        ORDER BY interaction_count DESC) top_movies_tab join movies
        ON top_movies_tab.movie_id = movies.movie_id
        ORDER BY top_movies_tab.interaction_count DESC
        LIMIT 5
    """)

    top_movies.show()

    top_categories = spark.sql("""
    SELECT c.category_name, SUM(top_movies_tab.interaction_count) as total_interactions
    FROM (SELECT movie_id, COUNT(*) as interaction_count
          FROM logs
          WHERE action IN ('resume', 'start')
          GROUP BY movie_id
          ORDER BY interaction_count DESC) top_movies_tab
    JOIN movies m ON top_movies_tab.movie_id = m.movie_id
    JOIN categories c ON m.category_id = c.category_id
    GROUP BY c.category_name
    ORDER BY total_interactions DESC
    LIMIT 5;
    """)

    top_categories.show()

    most_interacted_categories_for_a_given_user = spark.sql("""
    SELECT c.category_name, SUM(top_movies_tab.interaction_count) as total_interactions
    FROM (SELECT movie_id, COUNT(*) as interaction_count
          FROM logs
          WHERE action IN ('resume', 'start')
          and user_id = 'user_0038'
          GROUP BY movie_id
          ORDER BY interaction_count DESC) top_movies_tab
    JOIN movies m ON top_movies_tab.movie_id = m.movie_id
    JOIN categories c ON m.category_id = c.category_id
    GROUP BY c.category_name
    ORDER BY total_interactions DESC
    LIMIT 5;
    """)

    most_interacted_categories_for_a_given_user.show()

    most_interacted_categories_for_users = spark.sql("""
        SELECT top_movies_tab.user_id, c.category_name, SUM(top_movies_tab.interaction_count) as total_interactions
        FROM (
            SELECT user_id, movie_id, COUNT(*) as interaction_count
            FROM logs
            WHERE action IN ('resume', 'start')
            GROUP BY user_id, movie_id
        ) top_movies_tab
        JOIN movies m ON top_movies_tab.movie_id = m.movie_id
        JOIN categories c ON m.category_id = c.category_id
        GROUP BY top_movies_tab.user_id, c.category_name
        ORDER BY top_movies_tab.user_id, total_interactions DESC;
    """)

    most_interacted_categories_for_users.show()

    popular_movies_for_categories = spark.sql("""
    SELECT c.category_name, m.movie_name, SUM(top_movies_tab.interaction_count) as total_interactions
    FROM (
        SELECT movie_id, COUNT(*) as interaction_count
        FROM logs
        WHERE action IN ('resume', 'start')
        GROUP BY movie_id
    ) top_movies_tab
    JOIN movies m ON top_movies_tab.movie_id = m.movie_id
    JOIN categories c ON m.category_id = c.category_id
    GROUP BY c.category_name, m.movie_name
    ORDER BY c.category_name, total_interactions DESC;
    """)

    popular_movies_for_categories.show()

    personalized_movie_recommendation = spark.sql("""
    SELECT top_movies_tab.user_id, c.category_name, m.movie_name, SUM(top_movies_tab.interaction_count) as total_interactions
    FROM (
        SELECT user_id, movie_id, COUNT(*) as interaction_count,
               ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY COUNT(*) DESC) AS rn
        FROM logs
        WHERE action IN ('resume', 'start')
        GROUP BY user_id, movie_id
    ) top_movies_tab
    JOIN movies m ON top_movies_tab.movie_id = m.movie_id
    JOIN categories c ON m.category_id = c.category_id
    WHERE top_movies_tab.rn <= 5  -- Limit to 5 rows per user (you can change the number as per your requirement)
    GROUP BY top_movies_tab.user_id, c.category_name, m.movie_name
    ORDER BY top_movies_tab.user_id, total_interactions DESC;
    """)

    personalized_movie_recommendation.show()

    error_count = spark.sql("""
    SELECT error_code, COUNT(*) as count 
    FROM error_logs 
    GROUP BY error_code 
    ORDER BY count DESC
    """)

    error_count.show()

    review_sentiments = []
    columns = ["user_id", "movie_id", "review", "sentiment_score"]
    for item in review_df.collect():
        review_sentiments.append(
            (item["user_id"], item["movie_id"], item["review"], get_sentiment_score(item["review"])))

    review_sentiments_df = spark.createDataFrame(review_sentiments, columns)

    review_sentiments_df.createOrReplaceTempView("review_sentiments")

    sentiment_df = spark.sql("""
    SELECT 
    m.movie_id as movie_id,
    m.movie_name as movie_name,
    ROUND(AVG(rs.sentiment_score), 2) AS average_sentiment,
    CASE 
        WHEN AVG(rs.sentiment_score) >= 0.05 THEN 'Positive'
        WHEN AVG(rs.sentiment_score) <= -0.05 THEN 'Negative'
        ELSE 'Neutral'
    END AS sentiment
    FROM 
        review_sentiments rs
    JOIN
        movies m ON rs.movie_id = m.movie_id
    GROUP BY 
        m.movie_id, m.movie_name;
    """)

    sentiment_df.show()

    spark.stop()
