
![banner](files/hexapod_og.jpg)

# hexapod-raspberryPi

hexapod raspberry pi

This is a Hexapod raspberry Pi B4 project, originated by `SmallpTsai`.
`SmallpTsai` designed the hexapod mechanism and drove it via 7697. 
In this project, we will substitute 7697 with a Raspberry Pi 4B. 

See demo video: https://youtu.be/NJ7DdDEcq3U & https://youtu.be/To2Y6Mhu-CE to get the idea.

<a href='https://youtu.be/NJ7DdDEcq3U'><img src='http://img.youtube.com/vi/NJ7DdDEcq3U/mqdefault.jpg'/></a>
<a href='https://youtu.be/To2Y6Mhu-CE'><img src='http://img.youtube.com/vi/To2Y6Mhu-CE/mqdefault.jpg'/></a>

> More videos can be found at https://smallptsai.github.io/hexapod-web/

## Brief introduction

* **Remote control** is done via `WIFI Socket` or `USB joystick`
* It has 6 legs, each leg has 3 joints. So there are total of `18` **Servo motors** (TowerPro `MG92B`)
* `Raspberry Pi 4B` only provides 1 hardwire **PWM control**, so `PCA9685 control board` x 2 with the integrated step-down regulator are used to control these servo motors through `IIC`.
* **Power** comes from a `3S Lipo battery (11.1v)`. Also, 3 `mini560 DC-DC` step-down voltage regulators (5V 5A-max) are used, one to power RaspbPi, the other 2 are to power PCA9685 control boards.
* The **body** is 3D printed with `Somos® Imagine 8000` through a third-party 3D printing service.  
* **Angle sensor** `WIT JY61P` connects to RaspbPi through `IIC`.
* Followed by `SmallpTsai`, everything (3D STL, source code) is included in the project under **GPL license**.

## Skill requirement

If you want to make one hexapod by yourself. You should at least know how to:

* Mechanism part
    * Use `3D printer` to print a model.
    * Able to adjust the 3D model to fit your custom need.
* Electronics
    * Soldering power cord
    * How to use/charge/store `LIPO batteries`
* Software
    * Use `RaspbPi OS (Buster)` 
    * Use `Python 3`

## Table of Content

1. [Mechanism](mechanism/) - How to build the body
1. [Software](software/) - The software running on RaspbPi

