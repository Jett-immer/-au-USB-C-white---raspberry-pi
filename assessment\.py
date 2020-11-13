from sense_hat import SenseHat
import time
sense = SenseHat()
sense.clear()
#to measure the temperature and pressure in the habbital areas of the International space station the sensehat will light up different colours to alert the reading
green = (0,255,0)
red = (255,0,0)

while True:
   
   #take reading  of the temperature
    temp = sense.get_temperature()
    press = sense.get_pressure()
    o = sense.get_orientation()
    
    #set to round to 2 decimal places
    temp = round(temp,2)
    press = round(press,2)
    
    print("temperature:",temp)
    print("pressure:",press)
 
    
    pitch = round(o["pitch"])
    roll = o["roll"]
    yaw = o["yaw"]
    
    print(f"Pitch;{pitch}  Roll:{roll}  Yaw:{yaw}")
    message = "Temp:" + str(temp) + "Pressure:" + str(press) + "Pitch:" + str(pitch) + "Roll:" + str(roll) + "Yaw:" + str(yaw)
    sense.show_message(message, scroll_speed = 0.10)
    #waits 30 seconds before reposting data
    time.sleep(30)
    
    

    