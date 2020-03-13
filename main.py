import threading
import meter
import pv_simulator

def main():
    meter_thread = threading.Thread(target=meter.main)
    pv_thread = threading.Thread(target=pv_simulator.main)
    meter_thread.start()
    pv_thread.start()

if __name__ == "__main__":
    main()