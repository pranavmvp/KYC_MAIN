import cv2
import pytesseract
import re
from aadhar import *
from pan import *

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = cv2.imread('test_images/AADHAR_SIZE/testimage4.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

img2 = cv2.imread('test_images/PAN_SIZE/PAN_size6.jpeg')
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

aadhar_check(img)
pan_check(img2)
