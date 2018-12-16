from picar import back_wheels, front_wheels
from time import sleep
import picar

picar.setup();

db_file = "/home/pi/SunFounder_PiCar-V/remote_control/remote_control/driver/config"

fw = front_wheels.Front_Wheels(debug=False, db=db_file)
bw = back_wheels.Back_Wheels(debug=False, db=db_file)

bw.ready()
fw.ready()

FSPEED = 100

bw.ready();
fw.ready();
bw.speed = FSPEED;
fw.speed = FSPEED;
bw.forward();
fw.left();
sleep(1.00)
bw.stop();
fw.stop();
