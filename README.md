# IoT-TempHumidity-Monitor
This is the project presented for the introduction to IoT course.

## Overview

**Name**: Fabian Dacic
**Student credentials**: fd222fr

`IoT-TempHumidity-Monitor` is an IoT system built using MicroPython for Raspberry Pi Pico W, designed to monitor and evaluate environmental conditions. The system reads temperature and humidity data from a DHT11 sensor, evaluates the data, and provides immediate visual feedback through LEDs. The collected data is also sent to Adafruit IO for visualization and tracking.

**Time to Complete**: Approximately 5-10 hours.

## Objective

The objective of this project was to create an environment monitoring system that not only provides real-time data to users but also visualizes this data immediately on the device itself, and this immediate feedback can help users take quick actions in case of adverse conditions. The data sent to Adafruit IO allows users to track environmental conditions over time, offering valuable insights into patterns and trends.

## Material

### List of Material and Specifications

(Will update this part)

1. **Raspberry Pi Pico W**: Used as the main microcontroller for this project.
2. **DHT11 Sensor**: A sensor for detecting and recording temperature and humidity.
3. **LEDs**: Three LEDs (Red, Yellow, Green) used to indicate the current environmental conditions.

All of these components were bought from Electrokit as a part of the Starter Kit for the IoT course.

## Computer Setup

The device was programmed using Thonny. To flash the firmware and upload the code to the Raspberry Pi Pico, the steps as described in the MicroPython / course documentation were followed. 

## Putting Everything Together

(Circuit diagram here)

## Platform

Adafruit IO is used as the platform because of its ease of use, its robust MQTT support, and its excellent data visualization capabilities. 

## The Code

The code is split into four Python files:

1. `boot.py`: Handles the internet connectivity.
2. `led.py`: Manages the LED status based on temperature and humidity data.
3. `aio.py`: Controls the connection to Adafruit IO and the publishing of data to Adafruit IO feeds.
4. `main.py`: Coordinates the overall process of reading sensor data, updating the LEDs, and publishing data to Adafruit IO.

(Will go into more detail into what each file does)

## Transmitting the Data / Connectivity
The data is sent to Adafruit IO feeds using MQTT protocol over Wi-Fi. The temperature and humidity data are sent every 15 seconds.

## Presenting the Data
The data is presented on Adafruit IO dashboard where it can be visualized and monitored in real-time.
There are two feeds for humidity and temperature, and a dashboard that incorporates the two.

## Finalizing the Design

**Show final results of the project**
(Diagrams, and what could have been done better)

**Pictures**
(Real pictures of the device in action)
