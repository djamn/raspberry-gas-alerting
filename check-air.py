#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time
import requests  # Import requests library
from datetime import datetime, timedelta

# Version Control
LATEST_VERSION = "1.2.0 (14/04/2024)"

# Config
GPIO_BUZZER_PIN = 10
GPIO_SENSOR_PIN = 8
HAS_BUZZER = True       # Only trigger buzzer if buzzer is connected
SLEEP_INTERVAL = 0.2
STARTDATE = datetime.now().strftime("%d/%m/%Y %I:%M:%S (%p)")
ALERT_DURATION = timedelta(seconds=5)  # Configurable buzzer alert duration
ALERT = False
ALERT_TIME = None  # Variable to store the time when a high concentration was detected
WEBHOOK_URL = "" # INSERT YOUR DISCORD WEBHOOK URL
DATE_FORMAT = "[%d/%m/%Y-%I:%M:%S (%p)]"

# GPIO Config
GPIO.setmode(GPIO.BOARD)
GPIO.setup(GPIO_SENSOR_PIN, GPIO.IN)
GPIO.setup(GPIO_BUZZER_PIN, GPIO.OUT)

def send_discord_alert(message):
    data = {"content": message}
    response = requests.post(WEBHOOK_URL, json=data)
    date = datetime.now().strftime(DATE_FORMAT)
    print(date, "Alert sent to Discord:", response.status_code)

print("\n\n**SCRIPT STARTED - Monitoring air quality....**\n")
print("********************************************************************************")
print("[DEBUG] Latest Version:", LATEST_VERSION)
print("[DEBUG] GPIO used sensor pin:", GPIO_SENSOR_PIN)
print("[DEBUG] GPIO used buzzer pin:", GPIO_BUZZER_PIN)
print("[DEBUG] Start Date:", STARTDATE)
print("********************************************************************************\n")

GPIO.output(GPIO_BUZZER_PIN, GPIO.LOW)

try:
    while True:
        date = datetime.now().strftime(DATE_FORMAT)
        if GPIO.input(GPIO_SENSOR_PIN) == 1:
            print(date, "Air quality is normal")
            if ALERT and datetime.now() - ALERT_TIME >= ALERT_DURATION:
                if HAS_BUZZER:
                    GPIO.output(GPIO_BUZZER_PIN, GPIO.LOW)
                ALERT = False
        else:
            if not ALERT:
                ALERT_TIME = datetime.now()
                ALERT = True
                alert_message = f"{date} High gas concentration detected!"
                print(alert_message)
                if HAS_BUZZER:
                  GPIO.output(GPIO_BUZZER_PIN, GPIO.HIGH)  
                if WEBHOOK_URL:
                    send_discord_alert(alert_message)  # Sends alert to Discord
        time.sleep(SLEEP_INTERVAL)

except KeyboardInterrupt:
    GPIO.cleanup()  # Clean up GPIO on CTRL+C exit
