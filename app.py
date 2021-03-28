from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from tensorflow.keras.preprocessing import image

import cv2
import pytesseract
import re
from aadhar import *
from pan import *
from classify import *
from display_aadhar import *
from display_pan import *

app = Flask(__name__)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

@app.route('/')
def upload_file1():
       return render_template('main.html')


@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():

    name = request.form['a']
    addr = request.form['b']
    dob  = request.form['c']

    passed_values = {
            'Name' : name,
            'Address' : addr,
            'DOB' : dob
    }

    print(name)

    if request.method == 'POST':
      f1 = request.files['file1']
      f1.save(secure_filename('input1.jpg'))
      #f2 = request.files['file2']
      #f2.save(secure_filename('input2.jpg'))

      #f2 = request.files['file2']
      #f2.save(secure_filename('input2.jpg'))


      img1 = cv2.imread('input1.jpg')
      img2 = cv2.imread('input2.jpeg')
      img_aadhar = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
      img_pan = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
      img_classify1 = image.load_img('input1.jpg', target_size=(224, 224))
      img_classify2 = image.load_img('input2.jpeg', target_size=(224, 224))
      class1 = str(classify(img_classify1))
      class2 = str(classify(img_classify2))

      if(class1=='Aadhar Card'):
          get_aadhar = aadhar_check(img_aadhar)
          display_aadhar(passed_values, get_aadhar)
      elif(class1=='PAN Card'):
          get_pan = pan_check(img_pan)
          display_pan(passed_values, get_pan)

      if(class2=='Aadhar Card'):
         get_aadhar = aadhar_check(img_aadhar)
         display_aadhar(passed_values, get_aadhar)
      elif(class2=='PAN Card'):
         get_pan = pan_check(img_pan)
         display_pan(passed_values, get_pan)

      return 'Done'


'''
@app.route("/upload", methods=["POST"])
def upload():
    uploaded_files = flask.request.files.getlist("file[]")
    print uploaded_files
    return ""
'''

if __name__ == '__main__':
   app.run(debug = True)
