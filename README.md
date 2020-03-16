# PV Simulator Challenge
This program generates simulated photovoltaic (PV) values in watts derived from power values in watts sent from a simulated meter.

It is intended to be run with Python 3.7.6 and RabbitMQ 3.8.2

## How to run the simulator
#### Install rabbitmq-server
If you already have rabbitmq-server installed on your system you can skip these next two steps
```
$ sudo apt-get update && sudo apt-get upgrade
$ sudo apt-get install rabbitmq-server
```
#### Install dependencies
- `python3 -m venv env`
- `source env/bin/activate`
- `pip3 install -r requirements.txt`

#### Run program
Begin by launching the rabbitmq-server.
```
make server
```
When done stop the server by running
```
make stop
```
To use the simulator with default values you can start the meter and the PV simulator together by entering `make run`. 

To run each program seperately enter `make meter` and `make pv` respectively.

If you wish to customize the frequency that meter readings are sent out, pass the program a float representing the desired frequency in seconds.

`python3 meter.py <frequency value>`

If you wish to customize the efficiency that the simulator uses to calculate pv values pass the pv simulator a value 0 <= e <= 1 for the efficiency.

`python3 pv_simulator.py <desired efficiency>`
