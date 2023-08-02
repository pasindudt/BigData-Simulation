FROM python

RUN pip install kafka_python
RUN pip install docker
RUN pip install flask

ADD App.py /app/
ADD kafka_gen/* /app/kafka_gen/
ADD log_gen/* /app/log_gen/
ADD app_util/* /app/app_util/

ENTRYPOINT ["python", "/app/App.py"]