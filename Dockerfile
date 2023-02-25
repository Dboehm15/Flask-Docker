


FROM python:3.8

ADD main.py .
ADD main main

RUN pip install flask

CMD ["python", "./main.py"]
