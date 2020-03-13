# PV Simulator Challenge
This program generates simulated photovoltaic (PV) values using values sent by  


Ran using Python 3.7.6 and RabbitMQ 3.8.2

## How to run the simulator
#### Install rabbitmq-server
If you already have rabbitmq-server installed on your system you can skip these next few steps
```
$ echo 'deb http://www.rabbitmq.com/debian/ testing main' | sudo tee /etc/apt/sources.list.d/rabbitmq.list
$ wget -O- https://www.rabbitmq.com/rabbitmq-release-signing-key.asc | sudo apt-key add -
$ sudo apt-get update
$ sudo apt-get install rabbitmq-server
```
#### Install dependencies
- `python3 venv env --python=3.7.6`
- `pip3 -r requirements.txt`
- `source env/bin/activate`

#### Run program
Begin by either launching rabbitmq-server in another terminal window or running it in the background
```
rabbitmq-server # If running in seperate terminal window
rabbitmq-server &> /dev/null # If running silently in the background
```
To use the simulator after installing rabbitmq first launch the rabbitmq server by running `rabbitmq-server` then to launch the meter and the PV simulator together with default values enter `make run`. To run each seperately enter `make meter` and `make pv` respectively.