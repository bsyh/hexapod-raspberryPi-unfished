![banner](files/hexapod_og.jpg)

# hexapod-raspberryPi

hexapod raspberryPi

This is a Hexapod raspberry Pi B4 project, originated with 7697 control board by `SmallpTsai`.
`SmallpTsai` designed the mechanism and drivered it via 7697. 
In this project we will subtitude 7697 by a Raspberry Pi 4B. 

See demo video: https://youtu.be/NJ7DdDEcq3U & https://youtu.be/To2Y6Mhu-CE to get the idea.

<a href='https://youtu.be/NJ7DdDEcq3U'><img src='http://img.youtube.com/vi/NJ7DdDEcq3U/mqdefault.jpg'/></a>
<a href='https://youtu.be/To2Y6Mhu-CE'><img src='http://img.youtube.com/vi/To2Y6Mhu-CE/mqdefault.jpg'/></a>

> More videos can be found at https://smallptsai.github.io/hexapod-web/

## Brief introduction

* **Remote control** is done via `WIFI Socket` or `USB joystick`
* It has 6 legs, each leg has 3 joint. So there are total `18` **Servo motors** (TowerPro `MG92B`)
* `Raspberry Pi 4B` only privides 1 hardwire **PWM control**, so `PCA9685 control board` x 2 with integrated step-down regulator are used to control these servo motors through `IIC`.
* **Power** comes from a `2S Lipo battery (7.4v)`. Also a `mini560 DC-DC` step down voltage regulator are used to power RaspbPi with 5V 5A(max)
* The **body** is 3D printed with `Somos® Imagine 8000` through a third-part 3D printing service.  
* **Angle sensor** `WIT JY61P` connects to RaspbPi through `IIC` in paralell.
* Followed by `SmallpTsai`, everything (3D STL, source code) are included in the project under **GPL license**.

## Skill requirement

If you want to make one hexapod by yourself. You should at least knows how to:

* Mechanism part
    * Use `3D printer` to print a model.
    * Able to adjust 3D model to fit your custom need.
* Electronics
    * Soldering power cord
    * How to use/charge/store `LIPO batteries`
* Software
    * Use `RaspbPi OS (Linux)` 
    * Use `Python 3`

## Table of Content

1. [Mechanism](mechanism/) - How to build the body
1. [Software](software/) - The software running on RaspbPi (TBD)

