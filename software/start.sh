ps -ef | grep python | cut -c 9-15| xargs kill -s 9

python3 joystick.py  & 
python3 moveServer.py  & 
python3 realsense.py  
