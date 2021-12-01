---
layout:      post
title:       Droneh Update 1
categories:  droneh tinkering
image:       droneh/alive.gif
---

# It's alive!

It's been a few weeks since I started with my *DIY-drone-from-scratch* project
and it's going forward! During the first few weeks after project initialization
I had exams coming up so I couldn't spend any time on it. That didn't matter too much
because I had to wait for the pcb and parts to arrive anyways. As a heads-up, this post
has some photos taken from my phone which aren't the best quality. Hopefully, you can still see the important stuff in them 😃.

Before we proceed, let me first give you a quick reminder of the main components that will make up the drone:

| **Part** | **Purpose** | **Module** |
| --- | --- | --- |
| Flight controller | Used to control and connect everything.  | [Raspberry pi pico](https://www.raspberrypi.com/products/raspberry-pi-pico/) |
| Radio | Used to communicate with the host (PC, hand-control etc) | [nRF24L01](https://www.sparkfun.com/datasheets/Components/SMD/nRF24L01Pluss_Preliminary_Product_Specification_v1_0.pdf) |
| 6 Dof IMU | 3-axis accelerometer and 3-axis gyroscope, used to measure acceleration and rotation | [MPU-6050](https://invensense.tdk.com/wp-content/uploads/2015/02/MPU-6000-Datasheet1.pdf) |
| ToF laser-ranging sensor | Used to measure height. | [VL53L1X](https://www.st.com/en/imaging-and-photonics-solutions/vl53l1x.html) |
| Barometer | Used to measure height. | [BMP180](https://nl.mouser.com/datasheet/2/783/BST-BMP180-DS000-1509579.pdf) |
| MOSFET Motor control | Since I'm using DC, at pretty low currents, using a simple mosfet to control the motor current should (hopefully) be good enough. | [LNSC2302](https://lcsc.com/product-detail/MOSFETs_LONTEN-LNSC2302_C424190.html) |
| Battery | Used to power the drone. | 1s lipo, 3.7V 250mAh |

To assemble the drone, I ordered a cheap soldering iron as well as a supercheap 3D-printer (90 euro)
[Easythreed-X1](http://www.easythreed.com/h-col-1223.html) to make the frame for
the drone.

{% include image.html url="droneh/1.jpg" description="Easythreed-X1 3D printer arrived, in less than 24 hours after order, amazing!"%}
{% include image.html url="droneh/pcb_v01_front.jpg" description="Front side of PCB."%}
{% include image.html url="droneh/pcb_v01_back.jpg" description="Back side of PCB."%}

As you can see from the images above, the idea for this first version was to solder other
pcb's *onto* this pcb. This obviously won't look very professional, but I think it's a good
way to start. Also, buying pcb's for the sensors and radio is sometimes cheaper
than buying the individual chips and components and mounting everything myself.
For instance, you can get the NRF24L01 radio module for around 2-3 euros, and if you
were to buy only the chip NRF24L01, it's pretty much the same price (if not more).

### Soldering electronics

The first step was to do the soldering, which took a few hours to get right.
It's my first time soldering smd components (very tiny things), so I had to be
very gentle and patient, but it actually wasn't as hard as I had thought.
Once everything was soldered, it was time to start debugging and seeing which pin connections
worked and which didn't. After (many) hours of debugging, I discovered & learned the following:

- **Ensure solder connections are proper** - There were a few
places on the pcb where the solder pads wasn't properly soldered, so it didn't conduct, or
it conducted very poorly. This caused major headaches when the software didn't work (looking at you I2C).
- **Check wiring one more time before ordering pcb** - This is probably very obvious
and a classic noobie-misstake, but I had accidently swapped two of the SPI pins
for the radio module, so MOSI was connected to SCK of the pico, vice versa.
- **Be gentle if you remove pins from breakout-boards** - I must have accidently
either pushed too hard on the board, or used to high temperature on the soldering
iron, but I managed to destroy the radio module when removing the pre-soldered pins
and trying to solder it onto my pcb.
- **Use high resistor values for power-indicator-led** - I used 50 ohm resistors for all the LEDS on the board, and they're a bit too bright. I should have either taken high values for the resistors, or looked at the LED spec to choose some LEDS that weren't as intense. I can't look straight at the power led without hurting my eyes a bit 😆.

{% include image.html url="droneh/2.jpg" description="NRF24L01 module that I broke 😥"%}

This is how the pcb looked before I realized that the radio wasn't working:
{% include image.html url="droneh/3.jpg" description="Upside of the PCB."%}
{% include image.html url="droneh/4.jpg" description="Downside of the PCB."%}

So, since I had swapped the connections for the radio module, I had to either order
a new pcb, or connect the radio with wires. I didn't feel like waiting any longer for
new pcbs, and I knew that I would probably find more things that I'd like to improve
for the next iteration of the pcb, so I decided to connect it with wires instead.
Also, since I broke it, I had to order a new one, which arrived after a few days.

Once the new radio module arrived, and some more hours of debugging in both hardware
and software, all the sensors and drivers were now working. This included:
- BMP180 - Barometer
- MPU6050 - IMU
- VL53L1X - ToF laser sensor
- NRF24L01 - Radio
- Powering from battery and/or USB
- 2 Output leds
- 4 PWM output, each connected to a MOSFET, to control the motors.

### Frame

Once the electronics worked, I had to start working on the frame that the pcb
was going to be mounted on, as well as the motors and battery. I designed
the frame in Fusion360 and it consists of 3 seperate parts, which were glued together.

{% include image.html url="droneh/frame0.png" description="Drone frame in Fusion360."%}
{% include image.html url="droneh/frame2.jpg" description="Main body part."%}
{% include image.html url="droneh/frame1.jpg" description="All 3 frame parts printed."%}

After mounting the pcb on the frame, as well as the motors and the propellers,
droneh looked like this:
{% include image.html url="droneh/droneh.jpg" description="Droneh v0.1."%}


### WILL IT EVEN FLY?
Since all drivers and connections were now working, it was time to answer the
one question, which was going to impact the rest of the project: **Will it even fly?**

I honestly wasn't sure of this, I hadn't done any calculations of weight, propeller lift
or anything like that, but I instead just tried to keep the weight as low as possible
and hoped for the best.

After writing some code, mounting the propellers (without looking at their direction,
due to my excitement to see it fly), I decided to give it full thrust on all motors
to see if it could lift.

{% include image.html url="droneh/alive.gif" description=""%}

And it did! **SUCCESS**.
I know the quality sucks, but it is indeed in the air, so I have to consider my
first goal for droneh (get it to fly) as **reached**.
Even though I wouldn't want to be on-board a vehicle that flew this bad, I must say that this made me
so happy and excited because it proved that the project was indeed going to work!

## Next steps
Having a drone that can crash straight into stuff might be cool, somewhat
dangerous, but very costly in the long run.
So the next step in the project is going to be to control the drone
with a control. This is really where the hard part begins I think, because I need
to write drivers for all the sensors (well, not from scratch), and implement
a control flow that allows the drone to take some requested set-points and then
do some magic until the set-points are reached.

So, while it's a ton of work, I'm very excited for the future of this project.
Until then, fly safe! 🚁
