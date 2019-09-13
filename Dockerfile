FROM python:3.7

RUN apt-get update
RUN apt-get install openjdk-8-jdk -y
RUN apt-get install php-cli -y

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

ARG PORT_NO
ENV PORT_NO=${PORT_NO}

EXPOSE ${PORT_NO}

RUN bash
