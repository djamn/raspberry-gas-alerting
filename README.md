# MQ Gas Alerting System
This repository contains an explanation to implement a simple gas checking system that toggles a Piezo-Buzzer when MQ-Sensor specific high concentration is detected

The script also sends a notifcation to Discord, if ``WEBHOOK_URL`` has a valid url

## Getting Started
- **Needed:** **Transistor** (to enable buzzer when GPIO Pin is triggered), **Resistor** for better accuracy (used 10kΩ), **MQ-Sensor** (used MQ-135) and Piezo-Buzzer (or similar)
- **Software:** Python3 & pip
- **Hardware:** Raspberry Pi 3b+
  

## Execution of air quality script
- ``python3 check-air.py`` is the main script
- (Optional) Add a Discord webhook url to ``WEBHOOK_URL`` and toggle ``HAS_BUZZER`` variable
  <br>
- Remove file ending of main script -> It is executable without python3 command due to ``#!/usr/bin/env/python3``
- Script must then be moved to ``/usr/local/bin`` to be executable by simply writing the filename
  - ``sudo mv FILENAME /usr/local/bin/``
  - ``sudo chmod +x /usr/local/bin/FILENAME`` - Add execution permission
- To start the script on boot of Raspberry Pi:
  - Create ``**FILENAME**.sh`` script from repo
  - Move it to **/etc/init.d** and make it executable
    - ``sudo mv FILENAME.sh /etc/init.d/``
    - ``sudo chmod +x /etc/init.d/FILENAME.sh``
  - Register script to be executed on boot:
    - ``sudo update-rc.d FILENAME.sh defaults``
  - Reboot Raspberry Pi or manually start the script:
    - ``sudo /etc/init.d/FILENAME.sh start``

> :warning: Files that are moved to **/usr/local/bin** must be encoded in **LF**, not CRLF, otherwise they are not executable.
> **Fix (VSCode):** At the bottom right, change CRLF to LF
> **Fix (Terminal):** ``sudo sed -i -e 's/\r$//' /PATH/FILENAME``

## How To
![Build 1](/assets/build_1.jpg)  
![Build 2](/assets/build_2.jpg)  
![Build 3](/assets/build_3.jpg)  
![Build 4](/assets/build_4.jpg)  
![Build 5](/assets/build_5.jpg)
![GPIO Pins](/assets/raspberry-pi-gpio.png)
(https://www.elektronik-kompendium.de/sites/raspberry-pi/bilder/raspberry-pi-gpio.png)