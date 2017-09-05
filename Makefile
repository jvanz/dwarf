.PHONY: dist-scraper

scraper-image: compile-protos
	docker build --tag guilhermesft/dwarf-scraper:$(CIRCLE_BUILD_NUM) --file scraper/Dockerfile scraper

dist-scraper:
	python ./scraper/setup.py sdist

compile-protos:
	python -m grpc_tools.protoc -Iproto --python_out=./proto --grpc_python_out=./proto proto/graph_builder.proto
	cp proto/graph_builder_pb2.py scraper/scraper
	cp proto/graph_builder_pb2_grpc.py scraper/scraper
