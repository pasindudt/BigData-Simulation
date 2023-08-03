FROM python

RUN pip install kafka_python
RUN pip install flask
RUN pip install pymongo
RUN pip install hdfs

ADD App.py /app/
ADD kafka_gen/* /app/kafka_gen/
ADD log_gen/* /app/log_gen/
ADD app_util/* /app/app_util/
ADD mongo/* /app/mongo/

ENTRYPOINT ["python", "/app/App.py"]