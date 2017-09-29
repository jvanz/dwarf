FROM python:3.6
LABEL maintainer="guilherme.sft@gmail.com"

RUN apt-get update -y

# install scraper python package
COPY . /scraper
WORKDIR /scraper

RUN pip3 install -r requirements.txt

#copy gRPC files
COPY web_graph_pb2.py /usr/local/lib/python3.6
COPY web_graph_pb2_grpc.py /usr/local/lib/python3.6

ENTRYPOINT scrapy crawl link
