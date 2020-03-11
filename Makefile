TESTS := $(wildcard tests/*.in)
PYTHON := python3
BROKER_SOURCES := meter.py

setup:
	rabbitmq-server

run:
	$(PYTHON) meter.py &
	$(PYTHON) pv_simulator.py 