import math
def sound(signalpower,noisepower,radians):
    ratio=signalpower/noisepower
    decibels=10*(math.log10(ratio))
  
    
    height=math.sin(radians)
    return height,decibels
sound(0.001555,0.004,66)