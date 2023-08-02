FROM python
RUN pip install pymongo
RUN pip install hdfs
COPY randam_review_gen.py /randam_review_gen.py
COPY data-import-test.py /data-import-test.py
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]


#ADD data-import-test.py app.py
#ENTRYPOINT ["python", "app.py"]