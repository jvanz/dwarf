# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import grpc

import web_graph_pb2 as gb
import web_graph_pb2_grpc as gb_grpc


class SendToGraphBuilder(object):
    """ The link found to the graph builder """

    def __init__(self):
        self.channel = grpc.insecure_channel("localhost:50051")
        self.stub = gb_grpc.WebGraphStub(self.channel)

    def process_item(self, item, spider):
        response = self.stub.AddEdge(gb.Edge(source=item["source"], destination=item["destination"]))
        print(response.status)
        return item
