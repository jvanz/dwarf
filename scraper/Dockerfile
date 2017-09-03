FROM python:3
LABEL maintainer="guilherme.sft@gmail.com"

RUN apt-get update -y

# install scraper python package
COPY . /tmp/scraper
WORKDIR /tmp/scraper

RUN pip3 install -r requirements.txt
RUN python3 setup.py install

WORKDIR /
RUN rm -rf /tmp/scraper

ENTRYPOINT bash
