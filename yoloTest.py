# Create a new YOLO model from scratch
from ultralytics import YOLO
from PIL import Image
import cv2
import time

model = YOLO("yolov8n.pt")
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
# cam = cv2.VideoCapture(0)
for i in range(1):
    
    #s, img = cam.read()
    s = True
    img = cv2.imread("nhrl.png")
    targets = []
    if s:
        cv2.imshow("original img", img)
        results = model.predict(img, show = True, verbose = False, conf=0.1)
        b = results[0].boxes
        name_dict = results[0].names
        cv2.waitKey(0)
        # for j in range(len(b.cls)):
        #     name = name_dict[int(b.cls[j])]
        #     xywh = b.xywh[j]
        #     target = Target(name, xywh)
        #     if(name == "cell phone"):
        #         targets.append(target)
    targets.sort(key=lambda x: x.area, reverse=True)
    if(len(targets) > 0):
        t = targets[0]
        print("target x: ", t.center[0])
        if(t.center[0] < 320):
            print("turn left");
        else:
            print("turn right")
    else:
        print("target loss")
    