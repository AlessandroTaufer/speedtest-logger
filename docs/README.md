# speedtest-logger
Periodically logs the current network speed

Based on speedtest-cli 2.0.2 (https://pypi.org/project/speedtest-cli/)
##Requirements
* `sudo apt-get install python2.7`
* `sudo curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`
* `sudo python get-pip.py`
* `sudo pip install speedtest-cli`

##Configure
Edit __conf.txt__ file
```
// Time between two measurements (min)
20
// Log file location (must already exist)
../resources/speedData.log
```

##Run
In the __src__ folder run: <br>
* `python2.7 speedtest.py`

##Output
Logs will be saved in the selected log file  (default configuration: __resources/speedData.log__)