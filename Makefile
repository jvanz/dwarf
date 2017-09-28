.PHONY: dist-scraper

scraper-image: compile-protos
	docker build --tag guilhermesft/dwarf-scraper:$(CIRCLE_BUILD_NUM) --file scraper/Dockerfile scraper

dist-scraper:
	python ./scraper/setup.py sdist

compile-protos:
	python -m grpc_tools.protoc -Iweb_graph --python_out=./web_graph/web_graph\
		--grpc_python_out=./web_graph/web_graph web_graph/web_graph.proto
