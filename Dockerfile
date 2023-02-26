


FROM python:3.8

ADD main.py .
ADD templates templates
ADD main* main

RUN pip install flask

CMD ["python", "./main.py"]