import io
import json                    
import base64                  
import logging             
import numpy as np
import os
from PIL import Image
from engine import OCR
import numpy as np
import cv2
from flask import Flask, request, jsonify, abort
from flask_cors import CORS, cross_origin

app = Flask(__name__)          
app.logger.setLevel(logging.DEBUG)

CORS(app)

ocr = OCR()
  
@app.route("/License_predict", methods=['POST'])
@cross_origin()
def License_prediction():         
    # print(request.json)      
    if not request.json or 'image' not in request.json: 
        abort(400)
             
    # get the base64 encoded string
    im_b64 = request.json['image']

    # convert it into bytes  
    img_bytes = base64.b64decode(im_b64.encode('utf-8'))

    # convert bytes data to PIL Image object
    img = Image.open(io.BytesIO(img_bytes))

    # PIL image object to numpy array
    frame = np.asarray(img)      
    #print('img shape', frame.shape)

    # process your img_arr here    
    name_address, text = ocr.License_read_img(frame)
    # access other keys of json
    # print(request.json['other_key'])
    #print(text)

    result_dict = {'Body output': text, 'name_address': name_address}
    return jsonify(result_dict)
  
@app.route("/ID_predict", methods=['POST'])
@cross_origin()
def ID_prediction():         
    # print(request.json)      
    if not request.json or 'image' not in request.json: 
        abort(400)
             
    # get the base64 encoded string
    im_b64 = request.json['image']

    # convert it into bytes  
    img_bytes = base64.b64decode(im_b64.encode('utf-8'))

    # convert bytes data to PIL Image object
    img = Image.open(io.BytesIO(img_bytes))

    # PIL image object to numpy array
    frame = np.asarray(img)      
    #print('img shape', frame.shape)

    # process your img_arr here    
    text = ocr.ID_read_img(frame)
    # access other keys of json
    # print(request.json['other_key'])
    #print(text)

    result_dict = {'Body output': text}
    return jsonify(result_dict)

@app.route("/passport_predict", methods=['POST'])
@cross_origin()
def passport_prediction():         
    # print(request.json)      
    if not request.json or 'image' not in request.json: 
        abort(400)
             
    # get the base64 encoded string
    im_b64 = request.json['image']

    # convert it into bytes  
    img_bytes = base64.b64decode(im_b64.encode('utf-8'))

    # convert bytes data to PIL Image object
    img = Image.open(io.BytesIO(img_bytes))

    # PIL image object to numpy array
    frame = np.asarray(img)      
    #print('img shape', frame.shape)

    # process your img_arr here    
    text = ocr.passport_read_img(frame)
    # access other keys of json
    # print(request.json['other_key'])
    #print(text)

    result_dict = {'Body output': text}
    return jsonify(result_dict)

@app.route("/AOI_predict", methods=['POST'])
@cross_origin()
def AOI_prediction():         
    # print(request.json)      
    if not request.json or 'image' not in request.json: 
        abort(400)
             
    # get the base64 encoded string
    im_b64 = request.json['image']

    # convert it into bytes  
    img_bytes = base64.b64decode(im_b64.encode('utf-8'))

    # convert bytes data to PIL Image object
    img = Image.open(io.BytesIO(img_bytes))

    # PIL image object to numpy array
    frame = np.asarray(img)      
    #print('img shape', frame.shape)

    # process your img_arr here    
    text = ocr.AOI_read_img(frame)
    # access other keys of json
    # print(request.json['other_key'])
    #print(text)

    result_dict = {'Body output': text}
    return jsonify(result_dict)

  
#def run_server_api():
    
  
  
if __name__ == "__main__":     
    app.run(host='0.0.0.0', port=5000)