# Software
## Architecture
* servo_server: opens a port, reads signals as movement command 
* joystick_controller: connects to a joystick, sends commands to servo_server port
* imu: instantiates angle senser, provide service to read current pos and speed.


## Path Generator
Running the generator, a bunch of binary files will be generated to `output` folder, which includes basic movement path.
