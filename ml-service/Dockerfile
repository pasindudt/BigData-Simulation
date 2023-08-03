FROM python

RUN pip install flask
RUN pip install vaderSentiment

ADD App.py /app/App.py

ENTRYPOINT ["python", "/app/App.py"]