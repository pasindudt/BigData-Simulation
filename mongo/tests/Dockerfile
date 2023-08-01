FROM python
RUN pip install pymongo
RUN pip install hdfs
ADD data-import-test.py app.py
ENTRYPOINT ["python", "app.py"]