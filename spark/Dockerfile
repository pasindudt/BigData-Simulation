FROM bde2020/spark-python-template:3.2.1-hadoop3.2

ADD spark_test.py /app/
#ADD test.txt /app/
#RUN chmod 777 /app/test.txt

ENV SPARK_APPLICATION_PYTHON_LOCATION /app/spark_test.py
#ENV SPARK_APPLICATION_ARGS hdfs://namenode:9000/data/logs