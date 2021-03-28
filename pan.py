import pytesseract
import datefinder
from datetime import datetime
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
def pan_check(img2):

    img2 = cv2.imread('input2.jpeg')
    text = pytesseract.image_to_string(img2)
    i=0

    MAIN_LINES=[]
    name_found = False
    dates = []

    for line in text.splitlines() :

        if ((line=='') or (line==' ') or (line=='  ') or (line=='   ')):
            continue
        else:
            MAIN_LINES.append(line)
            #print(i,' ',line)
        i+=1

    for i in range(len(MAIN_LINES)):

        if ('Name' in MAIN_LINES[i] and name_found==False):
            name_index = i+1
            dad_index = i+3
            #date_index = i+5
            name_found = True

        matches = datefinder.find_dates(MAIN_LINES[i])
        for x in matches:
            date_a = (str(x))
            #print(date_a)
            date_a = date_a[:10]
            date_list = date_a.split('-')
            #print(date_list)
            Main_Dob = (str(date_list[1]+'/'+date_list[2]+'/'+date_list[0]))


    #print('\n')
    #print('Name', MAIN_LINES[name_index])
    #print('Daddy Name' ,MAIN_LINES[dad_index])
    #print('DOB:',Main_Dob)


    pan_values = {
            'Name' : MAIN_LINES[name_index],
            'Daddy' : MAIN_LINES[dad_index],
            'DOB' : Main_Dob
    }

    return pan_values
