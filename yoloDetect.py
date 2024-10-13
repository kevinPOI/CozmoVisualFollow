# Create a new YOLO model from scratch
from ultralytics import YOLO
from PIL import Image
import cv2
import time
import numpy as np

# model = YOLO("yolov8n.pt")
model = YOLO("cozmo419-3.pt")
# accepts all formats - image/dir/Path/URL/video/PIL/ndarray. 0 for webcam
class Target:
    name = ""
    xywh = []
    center = []
    height = 0
    width = 0
    area = 0
    def __init__(self, name, xywh):
        self.name = name
        self.xywh = xywh
        self.calcProp()
    def calcProp(self):
        self.center = self.xywh[0:2]
        self.height = self.xywh[3]
        self.width = self.xywh[2]
        self.area = self.height * self.width
print("Loaded!")
cam = cv2.VideoCapture(0)
def detect(img): 
    img = cv2.cvtColor(img.astype(np.uint8), cv2.COLOR_BGR2RGB) 
    w = img.shape[1]
    wo2 = w/2
    targets = []
        #cv2.imshow("original img", img)
    results = model.predict(img, show = True, verbose = False)
    b = results[0].boxes
    name_dict = results[0].names
    for j in range(len(b.cls)):
        name = name_dict[int(b.cls[j])]
        xywh = b.xywh[j]
        target = Target(name, xywh)
        if(name == "cozmo"):
            targets.append(target)
    targets.sort(key=lambda x: x.area, reverse=True)
    if(len(targets) > 0):
        t = targets[0]
        print("target x: ", t.center[0])
        # if(t.center[0] < 320):
        #     print("turn left")
        # else:
        #     print("turn right")
    else:
        print("target loss")
        return 233
    print("turning: ", ((t.center[0].item() - wo2) / wo2))
    return ((t.center[0].item() - wo2) / wo2)
    
    