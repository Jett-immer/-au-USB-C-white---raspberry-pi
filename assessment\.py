from sense_hat import SenseHat
import time
sense = SenseHat()
sense.clear()

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
 
    
    pitch = o["pitch"]
    roll = o["roll"]
    yaw = o["yaw"]
    
    #rounds pitch, roll and yaw to 5 decimal places 
    pitch = int(round(pitch,5))
    roll = int(round(roll,5))
    yaw = int(round(yaw,5))
    
    print(f"Pitch:{pitch}  Roll:{roll}  Yaw:{yaw}")
    message = "Temp:" + str(temp) + " Pressure:" + str(press) + " Pitch:" + str(pitch) + " Roll:" + str(roll) + " Yaw:" + str(yaw)
    sense.show_message(message, scroll_speed = 0.10)
    #waits 30 seconds before reposting data
    time.sleep(20)
    
    

    