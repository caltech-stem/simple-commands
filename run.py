from picar import back_wheels, front_wheels
from time import sleep
import picar
import random

picar.setup();

fw = front_wheels.Front_Wheels(debug=False, db=db_file)
bw = back_wheels.Back_Wheels(debug=False, db=db_file)

bw.ready()
fw.ready()



bw.ready();



for i in range (10):
  SPEED = random.randint(10,100)
  bw.speed = SPEED;
  bw.forward();
  sleep(random.randint(0,1,2)
  bw.stop();
