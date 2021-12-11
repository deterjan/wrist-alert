# WristAlert: Emergency Caregiver Bracelet
by Deniz Ulusel, for COMP_ENG 495: Wearable and Mobile Computing at Northwestern University.

## Summary
The toll taken by having to be vigilant at nighttime on home caregivers is a well researched issue 
[[1]](https://adc.bmj.com/content/103/2/137.info)
[[2]](https://journals.sagepub.com/doi/full/10.1177/1074840714562026)
[[3]](https://journals.lww.com/cancernursingonline/fulltext/2000/12000/sleep_and_depression_in_cancer_caregivers.2.aspx). 
Reported problems include sleep disorders and symptoms of clinical depression. WristAlert aims to ease the pressure on home caregivers by working with Bluetooth enabled medical continuous measurement devices such as pulse oximeters, blood pressure monitors or continuous glucose monitors. The vitals sent to WristAlert by the medical device are checked to ensure they are in a predefined "normal" range. If they are out of this range, WristAlert wakes the home caregiver up by vibrating. As a result, caregivers can sleep soundly knowing that they will be woken up in case of an emergency.

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
* A Raspberry Pi Pico sits at the center of the device, connected to other components via GPIOs and UART. MicroPython firmware was installed on the Pico following the steps [here](https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/3).
It runs a simple program ([entry.py](https://github.com/deterjan/wrist-alert/blob/main/entry.py)) to receive data from the HC06 Bluetooth adapter, check the received data, print it on the SSD1306 screen and activate the vibrating discs if necessary.
* The HC06 bluetooth adapter is connected to the Raspberry Pi Pico by UART. It forwards received values to the Pico for processing.
* The SSD1306 screen is driven by the Pico using a library provided by Micropython 
([ssd1306.py - original](https://github.com/micropython/micropython/blob/master/drivers/display/ssd1306.py)). 
This file was also uploaded to this repository for archival purposes 
([ssd1306.py - copy](https://github.com/deterjan/wrist-alert/blob/main/ssd1306.py)).
* The vibrating motors and pushbuttons are connected to the Pico via GPIO ports.
* The circuit rests on two mini breadboards attached to a sweatband.

## Pictures
![wrist1](https://user-images.githubusercontent.com/7872499/145694231-3ab6d688-b87c-462f-b586-8eff4f4b35cc.jpg)
WristAlert worn by a user (me!)

![bb1](https://user-images.githubusercontent.com/7872499/145694305-32284cbf-01f1-48be-aedf-852e735caa91.jpg)
A view of the first breadboard.

![bb2](https://user-images.githubusercontent.com/7872499/145694317-4a2383d6-82db-4eb4-bec5-1cb17242a3d5.jpg)
A view of the second breadboard.

## Lessons Learned

* Do NOT flash custom programs on your brand new ESP-01 if you are unsure about using the AT firmware! Once a sketch is flashed on the board, the AT firmware that was installed and tested by the manufacturer is lost forever. Restoring this firmware is difficult because there are many different manufacturers of ESP-01 and a ton of different AT firmware in the wild. Nobody can tell you which exact firmware will work well on the board in your hands. I intended to use WiFi for communication in this prototype but fell back to Bluetooth after hours of unfruitful efforts to restore the firmware on my ESP-01.
* Do NOT put infinitely looping MicroPython programs in the file main.py on your Raspberry Pi Pico! The Pico will start running this program automatically on boot and will not respond to stop commands sent via the USB port. I was caught in this pitfall couple of times and had to reinstall the MicroPython firmware. [Here](https://forums.raspberrypi.com/viewtopic.php?t=321332) is a discussion of this problem if you are curious.
* Do plan/sketch breadboard layouts before you start plugging the jumper wires in! I had to change many GPIOs I was using on the Pico while switching to the mini breadboards because the Pico isn't small enough to fit all of its IO on a mini breadboard.
