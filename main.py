import cv2
import os
from HandTrackingModule import handDetector
import random

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

class DragImg:
    def __init__(self, path, posOrigin):
        self.posOrigin = posOrigin
        self.originalPos = original_positions[os.path.basename(path)]
        self.path = path
        self.img = cv2.imread(self.path)
        if self.img is None:
            raise ValueError(f"Image not found at path: {self.path}")
        self.size = self.img.shape[:2]
        self.isDragging = False

    def update(self, cursor):
        ox, oy = self.posOrigin
        h, w = self.size
        if ox < cursor[1] < ox + w and oy < cursor[2] < oy + h:
            self.isDragging = True
            self.posOrigin = cursor[1] - w // 2, cursor[2] - h // 2
        else:
            self.isDragging = False

    def draw(self, img):
        ox, oy = self.posOrigin
        h, w = self.size
        try:
            img[oy:oy + h, ox:ox + w] = self.img
            if (abs(ox - self.originalPos[0]) < 10) and (abs(oy - self.originalPos[1]) < 10):
                cv2.rectangle(img, (ox, oy), (ox + w, oy + h), (0, 255, 0), 3)
        except:
            pass



detector = handDetector()

path = "images"
myList = os.listdir(path)

original_positions = {}
for pathimg in myList:
    name_parts = pathimg.split('_')
    row = int(name_parts[1])
    col = int(name_parts[2].split('.')[0])
    # Adjust positions based on the new grid lines
    posOrigin = [col * 110 + 255, row * 110 + 50]
    original_positions[pathimg] = posOrigin

initial_positions = list(original_positions.values())
random.shuffle(initial_positions)

listImg = []
for pathimg, posOrigin in zip(myList, initial_positions):
    listImg.append(DragImg(f'{path}/{pathimg}', posOrigin))

dragging_image = None

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    # Draw fixed gridlines around images
    for x in range(250, 672, 110):
        cv2.line(img, (x, 50), (x, 372), (0, 0, 0), 1)
    for y in range(45, 480, 110):
        cv2.line(img, (250, y), (572, y), (0, 0, 0), 1)

    if len(lmList) != 0:
        length, img, info = detector.findDistance(8, 12, img)
        if length < 30:
            cursor = lmList[8]
            for imgObject in listImg:
                if imgObject.isDragging or dragging_image is None:
                    imgObject.update(cursor)
                    if imgObject.isDragging:
                        dragging_image = imgObject
        if length >= 30:
            dragging_image = None

    for imgObject in listImg:
        imgObject.draw(img)
    
    

    cv2.imshow("image", img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
