FROM python:3.6
LABEL maintainer="guilherme.sft@gmail.com"

RUN apt-get update -y


#copy gRPC files
COPY web_graph_pb2.py /usr/local/lib/python3.6
COPY web_graph_pb2_grpc.py /usr/local/lib/python3.6

# install web_graph python package
COPY . /web_graph
WORKDIR /web_graph

RUN pip3 install -r requirements.txt
RUN python3 setup.py install

WORKDIR /

RUN rm -rf /web_graph

ENTRYPOINT python3 -m web_graph
