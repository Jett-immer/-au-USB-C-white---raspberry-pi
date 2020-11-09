from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

colour = (255,255,255)
x = (0)
y = (0)

sense.set_pixel(2,2,(255,255,255))

while True:
    for event in sense.stick.get_events():
        print(event.direction, event.action)
            set.set_pixel(x,y,(255,255,255)
        





                
        