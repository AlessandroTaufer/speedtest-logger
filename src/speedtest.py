#
#   Author: Alessandro Taufer
#   Email: alexander141220@gmail.com
#   Url: https://github.com/AlessandroTaufer
#
import subprocess
import datetime
import time


class SpeedTest:

    def __init__(self):
        self.conf = "../resources/conf.txt"  # Path to the configuration file
        self.delta = 20  # Time between two measurements (min)
        self.logfile = "../resources/speedData.log"  # Log file path
        self.load_configuration()
        self.routine()

    def routine(self):  # Periodically acquire measures
        print("Program started")
        counter = 0
        while True:
            try:
                output = self.run()
                self.write_data(self.logfile, self.convert_to_csv(output))
                print("\nMeasure " + str(counter) + ":\nTime: " + str(datetime.datetime.now()) + "\n" + output)
                time.sleep(self.delta * 60)
            except (KeyboardInterrupt, SystemExit):
                raise
            except:
                print("----Something went wrong, repeating the measurement---")

    def load_configuration(self):  # Load configurations from a file
        print("Loading configurations..")
        txt = ""
        with open(self.conf, "r") as f:
            txt = f.read()
        txt = txt.split("\n")
        config_text = []
        for row in txt:
            if "//" not in row:
                config_text.append(row)
        self.delta = int(config_text[0])
        self.logfile = config_text[1]

    @staticmethod
    def run():  # Runs a speed test
        output = subprocess.check_output(['speedtest-cli', '--simple'])
        return output

    @staticmethod
    def convert_to_csv(speed):  # Convert the speed test in a csv string
        csv = datetime.datetime.now().strftime('%Y,%m,%d,%H,%M,%S')
        speed = speed.split(" ")
        csv += speed[1] + ";" + speed[3] + ";" + speed[5] + "\n"
        return csv

    @staticmethod
    def write_data(file, txt):  # Append a string to a file
        with open(file, "a") as f:
            f.write(txt)


if __name__ == "__main__":
    SpeedTest()
