.PHONY: dist-scraper

dist-scraper:
	python ./scraper/setup.py sdist

protos:
	python -m grpc_tools.protoc -Iproto --python_out=./scraper/scraper/ --grpc_python_out=./scraper/scraper proto/graph_builder.proto
