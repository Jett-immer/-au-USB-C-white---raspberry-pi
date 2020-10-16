from sense_hat import SenseHat

sense = SenseHat()

blue = (0,0,255)
red = (255,0,0)
yellow = (255,255,0)
green = (0,255,0)
cyan = (0,255,255)
magenta = (255,0,255)
black = (0,0,0)
white = (255,255,255)

sense.show_letter("J", red)
sense.show_letter("E", blue)
sense.show_letter("T", yellow)
sense.show_letter("T", green)
sense.show_letter("I", green)
sense.show_letter("M", magenta)
sense.show_letter("M", black)
sense.show_letter("E", yellow)
sense.show_letter("R", red)