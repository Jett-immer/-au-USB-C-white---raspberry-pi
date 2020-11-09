from sense_hat import SenseHat

sense = SenseHat()
sense.clear()
#to measure the temperature and pressure in the habbital areas of the International space station the sensehat will light up different colours to alert the reading

green = (0,255,0)
red = (255,0,0)

while True:
   
   #take reading  of the temperature
    temp = sense.get_temperature()
    press = sense.get_pressure()
    
    #set to round to 2 decimal places
    temp = round(temp,2)
    press = round(press,2)

