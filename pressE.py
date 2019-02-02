from picar import back_wheels, front_wheels
from time import sleep
import picar
import keyboard

picar.setup();

#can you guys tell me how to make a new program?
#hiihihihihi

fw = front_wheels.Front_Wheels(debug=False, db=db_file)
bw = back_wheels.Back_Wheels(debug=False, db=db_file)

bw.ready()
fw.ready()

SPEED = 60

while True:
    try: 
        if keyboard.is_pressed('E'):
            SPEED = 10
            SPEED+=10
            bw.ready();
            bw.speed = SPEED;
            print("SPEED" + SPEED)
            bw.forward();
            SPEED+=10
            bw.ready();
            bw.speed = SPEED;
            bw.forward();
            SPEED+=10
            bw.ready();
            bw.speed = SPEED;
            bw.forward();
            SPEED+=10
            bw.ready();
            bw.speed = SPEED;
            bw.forward();
            bw.ready();
            bw.speed = SPEED;
            bw.forward();
            SPEED+=10
            SPEED+=10
            bw.ready();
            bw.speed = SPEED;
            sleep(3.00)
              print("Vroom Vroom")
            #Vroom Vroom
        bw.stop();
SPEED = 60  
            break
        else:
            SPEED = 10
            pass
    except:
        break
sleep(2.00)
bw.stop();
