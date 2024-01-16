# syntax=docker/dockerfile:1

FROM python:3.8
WORKDIR /game_monitor1
ENV FLASK_APP=__main__.py
ENV FLASK_RUN_HOST=127.0.0.1
RUN pip install -r requirements.txt --no-cache-dir
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD python api/__main__.py
