"""
This file holds the Meter class.

Written by Josh Bell
"""

import random
import pika

class Meter:
    """
    This class produces
    """
    def __init__(self):
        """Initialize a meter with a random seed."""
        # self. # TODO init with rand seed
        def val_gen():
            while True:
                yield  str(random.randrange(0, 900000) / 100)
        self.next_reading = val_gen()

            
    def __enter__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='readings')
        return self

    def read(self):
        self.channel.basic_publish(exchange='',
                                    routing_key='readings',
                                    body=next(self.next_reading))
    


    def __exit__(self, _, _, _):
        # print("exiting:", a, b, c)
        self.connection.close()

def main():
    # m = Meter()
    # print("M is: ", m)
    with Meter() as m:
        print("M is: ", m)
        while True:
            m.read()

if __name__ == "__main__":
    main()