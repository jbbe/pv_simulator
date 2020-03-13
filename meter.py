"""
This file holds the Meter class.

Written by Josh Bell
"""
import datetime
import time
import random
import sys
import pika

def daytime():
    """Return whether the current time is between 5am and 9pm."""
    now = datetime.datetime.now()
    five_am = now.replace(hour=5, minute=0, second=0, microsecond=0)
    nine_pm = now.replace(hour=21, minute=0, second=0, microsecond=0)
    return five_am <= now <= nine_pm


class Meter:
    """
    This class produces
    """
    def __init__(self):
        """Initialize a meter that yields random values during the daytime."""
        def val_gen():
            while True:
                if daytime():
                    yield  str(random.randrange(0, 900000) / 100)
                else:
                    yield '0'
        self.next_reading = val_gen()
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='readings')

    def __enter__(self):
        """Initialize rabbitmq connection."""
        return self

    def read(self):
        """Publish a new meter reading to the readings queue."""
        self.channel.basic_publish(exchange='',
                                   routing_key='readings',
                                   body=next(self.next_reading))

    def __exit__(self, *args):
        """Close connection."""
        self.connection.close()

def main():
    """Create a meter object which sends out a reading at either the default
    or input frequency."""
    if len(sys.argv) > 1:
        try:
            frequency = float(sys.argv[1])
        except ValueError:
            print("Invalid frequency input, using default of 5")
            frequency = 5
    else:
        frequency = 5
    with Meter() as meter:
        while True:
            meter.read()
            time.sleep(frequency)

if __name__ == "__main__":
    main()
