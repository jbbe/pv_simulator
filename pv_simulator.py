"""
This file holds the PV simulator class.

It accepts meter readings as messages from a readings channel and calculates
a simulated PV value using an assumed efficiency of 0.75. The efficiency can
be modified by passing a desired frequency to the program when launching it.

Written by Josh Bell
"""
import os
import sys
import meter
import time
import datetime
import pika

class PVSim:
    def __init__(self, out_file="pv_out.csv", period=5, efficiency=0.75):
        if efficiency < 0 or efficiency > 1:
            raise ValueError
        self.out_file = out_file
        self.efficiency = efficiency

        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='readings')
        self.channel.basic_consume(queue='readings',
                                    auto_ack=True,
                                    on_message_callback=self.accept_msg)
        self.channel.start_consuming()

    def accept_msg(self, *args):
        """Accept a message from the broker and write output to file."""
        # arguments are ch, method, properties, body, we only need body
        body = args[3]
        with open(self.out_file, 'a') as f:
            """
            Writes:
            timestamp,
            meter power value,
            PV power value,
            the sum of the powers (meter + PV)
            """
            now = datetime.datetime.now()
            try:
                meter_val = float(body)
            except ValueError:
                print("invalid message from meter: ", body)
                return
            pv_val = self.efficiency * meter_val
            sum_of_powers = meter_val + pv_val

            out_str = f"{now}, {meter_val}, {pv_val}, {sum_of_powers} \n"
            print(out_str)
            f.write(out_str)

def main():
    """Create a PV simulator object which listens for meter readings
    and writes output to an output file."""
    # TODO allow overriding 
    if len(sys.argv) > 1:
        try:
            PVSim(efficiency=float(sys.argv[1]))
        except ValueError:
            print("Invalid frequency input, exiting")
            sys.exit(1)
    else:
        pv = PVSim()

if __name__ == "__main__":
     main()