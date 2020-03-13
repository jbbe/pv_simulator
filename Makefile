TESTS := $(wildcard tests/*.in)
PYTHON := python3
BROKER_SOURCES := meter.py

setup:
	rabbitmq-server

run:
	# rabbitmq-server &
	timeout 4
	$(PYTHON) main.py

meter:
	# rabbitmq-server &
	$(PYTHON) meter.py

pv:
	$(PYTHON) pv_simulator.py 

clean:
	rm pv_out.csv
kill-server:
