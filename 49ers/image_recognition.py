import cv2
import cv2.cv as cv
from SimpleCV import Image

logo = Image('/Users/hackreactor/code/sheltowt/PIXLEE/coke_recognition/red_back.jpg')

machine = Image('/Users/hackreactor/code/sheltowt/PIXLEE/coke_recognition/coke_photos/93.png')

matches = machine.findTemplate(logo)

matches.draw(width=3)

machine.show()
cv.WaitKey(5000)

count = 0

for match in matches:
  count = count + 1

print(matches)

print(count)