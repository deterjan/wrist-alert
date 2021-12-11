# WristAlert: Emergency Caregiver Bracelet
by Deniz Ulusel

## Summary
The toll taken by having to be vigilant at nighttime on home caregivers is a well researched issue 
[[1]](https://adc.bmj.com/content/103/2/137.info)
[[2]](https://journals.sagepub.com/doi/full/10.1177/1074840714562026)
[[3]](https://journals.lww.com/cancernursingonline/fulltext/2000/12000/sleep_and_depression_in_cancer_caregivers.2.aspx). 
Reported problems include sleep disorders and symptoms of clinical depression. WristAlert aims to ease these pressures on home caregivers by working with Bluetooth enabled medical continuous measurement devices such as pulse oximeters, blood pressure monitors or continuous glucose monitors. The vitals sent to WristAlert by the medical device are checked to ensure they are in a predefined "normal" range. When they are out of range, WristAlert wakes the home caregiver up by vibrating. As a result, caregivers can sleep sound knowing that they will be woken up in case of an emergency.

## Diagrams
![yargi_breadboard](https://user-images.githubusercontent.com/7872499/145693524-d035cab0-9e73-427a-a017-53d80aeea62a.png)
Breadboard diagram of the device


<img width="778" alt="" src="https://user-images.githubusercontent.com/7872499/145693713-8b739d15-518e-4166-a78b-9c42f0bfc175.png">
WristAlert's interaction with medical devices

## Components Used

| Component Name  | Count |
| ------------- | ------------- |
| Raspberry Pi Pico  | 1 |
| HC06 Bluetooth Module | 1 |
| SSD1306 OLED screen  | 1 |
| Vibrating Mini Motor Disc  | 2 |
| Pushbutton | 1 |
| Mini breadboard  | 1 |
| Jumper cables  | see breadboard diagram above |
| Sweatband  | 1 |

## Implementation
* A Raspberry Pi Pico sits at the center of the device, connected to other components via GPIOs and UART. It runs a simple MicroPython program ([entry.py](https://github.com/deterjan/wrist-alert/blob/main/entry.py)) to receive data from the HC06 Bluetooth adapter, check the received data, print it on the SSD1306 screen and activate the vibrating discs if necessary.
* The HC06 bluetooth adapter is connected to the Raspberry Pi Pico by UART. It forwards received values to the Pico for processing.
* The SSD1306 screen is driven by the Pico using a library provided by Micropython [here](https://github.com/micropython/micropython/blob/master/drivers/display/ssd1306.py). This library file was also uploaded to this repository for archival purposes.
* The vibrating motors and pushbuttons are connected to the Pico via GPIO ports.
* The circuit rests on two mini breadboards attached to a sweatband.

## Pictures
