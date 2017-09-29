FROM python:3
LABEL maintainer="guilherme.sft@gmail.com"

RUN apt-get update -y

# install scraper python package
COPY . /scraper
WORKDIR /scraper

RUN pip3 install -r requirements.txt

ENTRYPOINT scrapy crawl link
