from picar import back_wheels, front_wheels
from time import sleep
import picar

picar.setup();

db_file = "/home/pi/SunFounder_PiCar-V/remote_control/remote_control/driver/config"

fw = front_wheels.Front_Wheels(debug=False, db=db_file)
bw = back_wheels.Back_Wheels(debug=False, db=db_file)

bw.ready()
fw.ready()

<<<<<<< HEAD
SPEED = 100

bw.ready();



bw.speed = SPEED;
=======
FSPEED = 100

fw.turn_right();
>>>>>>> 56258d93db581525ac8c5ae64152cacfb4cb82d8

for i in range(5):
  bw.speed = FSPEED;
  bw.forward();
sleep(1.00)
bw.stop();
bw.backward();
sleep(2.00)
bw.stop();
sleep(2.00)
bw.foward();
fw.turn_right()
sleep(2.00)
bw.stop();
fw.turn_straight()
sleep(2.00)
bw.backward();
fw.turn_right
sleep(2.00)
bw.stop
bw.forward();
fw.turn_left()
bw.stop();
fw.turn_straight()
sleep(2.00)
bw.stop();
bw.foward();
fw.turn_right()
fw.turn_straight();
fw.turn_left();
sleep(2.00)
bw.stop();
fw.turn_straight()
sleep(2.00)
