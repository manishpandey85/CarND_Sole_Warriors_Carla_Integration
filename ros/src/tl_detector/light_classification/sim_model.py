import numpy as np
import cv2
from styx_msgs.msg import TrafficLight

class SimModel():
  def __init__(self):
    self.GREEN_CHANNEL = 1
    self.RED_CHANNEL = 2
    self.area_thrld = 79
  def predict(self, image):
    """
    image: cv2.Image (BGR)
    """
    red_imge = image[:,:,self.RED_CHANNEL]
    green_imge = image[:,:,self.GREEN_CHANNEL]
    red_area = np.sum(red_imge == red_imge.max())
    green_area = np.sum(green_imge == green_imge.max())


    prediction = TrafficLight.UNKNOWN

    if red_area >= self.area_thrld and green_area <= self.area_thrld:
      prediction = TrafficLight.RED
    elif red_area >= self.area_thrld and green_area >= self.area_thrld:
      prediction = TrafficLight.YELLOW if 0.8 <= red_area / green_area <= 1.2 else TrafficLight.RED
    elif green_area >= self.area_thrld:
      prediction = TrafficLight.GREEN
    else:
      prediction = TrafficLight.UNKNOWN

    print "Traffic Light: ",
    if prediction == TrafficLight.RED:
      print("RED")
    elif prediction == TrafficLight.YELLOW:
      print("YELLOW")
    elif prediction == TrafficLight.GREEN:
      print("CLEAR")
    else:
      print("CLEAR")
      
    return prediction
