.PHONY: dist-scraper

scraper-image:
	docker build --tag guilhermesft/k9-scraper:latest --file scraper/Dockerfile scraper

dist-scraper:
	python ./scraper/setup.py sdist

protos:
	python -m grpc_tools.protoc -Iproto --python_out=./proto --grpc_python_out=./proto proto/graph_builder.proto
