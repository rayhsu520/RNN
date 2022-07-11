FROM jupyter/base-notebook

USER root


RUN apt-get update

WORKDIR /project
COPY requirements.txt requirements.txt 
COPY . /project

RUN pip install -r requirements.txt 
EXPOSE 5000 