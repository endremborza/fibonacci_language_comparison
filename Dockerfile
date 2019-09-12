FROM python:3.7

RUN apt-get update
RUN apt-get install openjdk-8-jdk -y
RUN apt-get install php-cli -y


RUN bash
