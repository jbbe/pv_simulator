# PV Simulator Challenge
This program generates simulated photovoltaic (PV) values using values sent by  

It is intended to be ran with Python 3.7.6 and RabbitMQ 3.8.2

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
Begin by either launching rabbitmq-server in another terminal window or running it in the background
```
rabbitmq-server # If running in seperate terminal window
rabbitmq-server &> /dev/null # If running silently in the background
```
To use the simulator after installing rabbitmq first launch the rabbitmq server by running `rabbitmq-server` then to launch the meter and the PV simulator together with default values enter `make run`. 

To run each program seperately enter `make meter` and `make pv` respectively.

If you wish to customize the frequency that meter readings pass the program a float for the desired frequency.

`python3 meter.py <frequency value>`

If you wish to customize the efficiency that the simulator uses to calculate pv values pass the pv simulator a value 0 <= e <= 1 for the efficiency.

`python3 pv_simulator.py <desired efficiency>