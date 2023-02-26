


FROM python:3.8

ADD main.py .
ADD templates templates
ADD main* main
ADD test* test

RUN pip install flask
RUN pip install requests

CMD ["python", "./main.py"]