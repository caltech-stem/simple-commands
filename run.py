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
bw.speed = FSPEED;
fw.turn_right();
delay = 1
#dance time LOL
for i in range(10):
  delay = delay - 0.1
  bw.speed = 100
  bw.forward();
  sleep(delay)
  bw.stop();
  bw.speed = -100
  bw.forward();
  sleep(delay)
  bw.stop();
