

protos:
	python -m grpc_tools.protoc -Iproto --python_out=./scraper/scraper/ --grpc_python_out=./scraper/scraper proto/graph_builder.proto
