from picar import back_wheels, front_wheels
from time import sleep
import picar

picar.setup();

fw = front_wheels.Front_Wheels(debug=False, db=db_file)
bw = back_wheels.Back_Wheels(debug=False, db=db_file)

bw.ready()
fw.ready()

SPEED = 60

bw.ready();

bw.speed = SPEED;

bw.forward();
sleep(2.00)
bw.stop();
