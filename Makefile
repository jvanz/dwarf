
scraper-image:
	python -m grpc_tools.protoc -Iproto --python_out=./scraper\
		--grpc_python_out=./scraper/ proto/web_graph.proto
	docker build --tag guilhermesft/dwarf-scraper:latest --file scraper/Dockerfile scraper
