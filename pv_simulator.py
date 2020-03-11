"""
This file holds the PV class.

Written by Josh Bell
"""
import os
import meter
import time
import datetime
import pika

class PVSim:
    def __init__(self, out_file="pv_out.txt", period=5):
        self.out_file = out_file

        self.current_power = 0
        self.pv_value = 0
        self.readings_this_hour = 0
        self.avg_dict = {i : [0, 0.0] for i in range(60) }
        self.hourly_avg = 0
        self.last_update_time = 0

        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='readings')
        self.channel.basic_consume(queue='readings',
                                    auto_ack=True,
                                    on_message_callback=self.accept_msg)
        self.channel.start_consuming()
        # self.channel.queue_declare(queue='readings') 

    def accept_msg(self, ch, method, properties, body):
        with open(self.out_file, 'a') as f:
            # Writes:
            # timestamp, 
            # meter power value, 
            # PV power value
            # the sum of the powers (meter + PV
            now = datetime.datetime.now()
            if time.time() - self.last_update_time > 60:
                self.update_avg()
            self.readings_this_hour += 1
            self.avg_dict[now.minute][0] += 1
            # TODO watch for overflow here
            self.avg_dict[now.minute][1] += float(body) # TODO convert to int
            out_str = f"{now} {body} {self.current_power} {self.hourly_avg} \n"
            print(out_str)
            f.write(out_str)

    def update_avg(self):
        # Keep dictionary of min stamp
        new_avg = 0
        now = datetime.datetime.now()
        self.last_update_time = time.time()
        if self.readings_this_hour > 0:
            for min_avg in self.avg_dict.values():
                new_avg += (min_avg[0] / self.readings_this_hour) * min_avg[1]

            self.readings_this_hour -= self.avg_dict[now.minute][0]
            self.avg_dict[now.minute][0] = 0
            self.avg_dict[now.minute][1] = 0
        self.hourly_avg = new_avg

    def gen_pv_val(self, new_val):
        pass


def main():
    pv = PVSim()
    # while True:

if __name__ == "__main__":
    main()