TESTS := $(wildcard tests/*.in)
PYTHON := python3
BROKER_SOURCES := meter.py

server:
	/sbin/service rabbitmq-server start

stop:
	/sbin/service rabbitmq-server stop
run:
	$(PYTHON) main.py

meter:
	# rabbitmq-server &
	$(PYTHON) meter.py

pv:
	$(PYTHON) pv_simulator.py 

clean:
	rm pv_out.csv
