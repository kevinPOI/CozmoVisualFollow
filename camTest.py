from cozmo_fsm import *
from yoloDetect import *
import time
import numpy as np
import cv2
c = 0
img_cache = np.zeros([240,320,3])
class GetTurn(StateNode):
    def __init__(self):
        super().__init__()
        
    def start(self, event=None):
        super().start(event)
        turn = 0
        turn = detect(img_cache)
        turn *= -0.5
        self.post_data(cozmo.util.Angle(turn))
class GetCurve(StateNode):
    def __init__(self):
        super().__init__()
        
    def start(self, event=None):
        speed = 50
        diff = 35
        super().start(event)
        turn = 0
        turn = detect(img_cache)
        left = turn * diff + speed
        right = -turn * diff + speed
        self.post_data([left, right])


class camTest(StateMachineProgram):
    # setup{
    #     start: ClearCache() =TM=> query: Query("Is cube2 sideways?") 
    #     =TM=> Query("ow many cubes are there?")
    # =TM=> Query("What is the distance between cube1 and cube2?")
    # =TM=> Query("Which cube is closest to cube1?")
    # =TM=> Query("Please remember that all cubes are 45 mm on a side.") 
    # =TM=> Query("How big is cube1?") 
    # =TM=> Query("What is the volume of cube3?") 
    
    # }
    def user_image(self,image,gray):
        self.robot.myimage = gray
        global c
        global img_cache
        c += 1
        #print(image.shape)
        if c == 10:
            cv2.imshow("img", cv2.cvtColor(image.astype(np.uint8), cv2.COLOR_BGR2RGB))
            
            img_cache = image
            c = 0

    
    # setup{
    #     ColorImageEnabled() =C=> getTurn: GetTurn() =D=> DriveWheel =C=> getTurn
    # }
    def setup(self):

        colorimageenabled1 = ColorImageEnabled() .set_name("colorimageenabled1") .set_parent(self)
        getCurve = GetCurve() .set_name("getCurve") .set_parent(self)
        
        completiontrans1 = CompletionTrans() .set_name("completiontrans1")
        completiontrans1 .add_sources(colorimageenabled1) .add_destinations(getCurve)
        
        nulltrans1 = NullTrans() .set_name("nulltrans1")
        nulltrans1 .add_sources(getCurve) .add_destinations(getCurve)
        
        return self
