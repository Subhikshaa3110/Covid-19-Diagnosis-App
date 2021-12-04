import os
import pandas as pd 
import numpy as np 
import flask
import pickle
from flask import Flask, render_template, request, flash, redirect
from keras.preprocessing import image
from tensorflow.keras.models import load_model
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/predict',methods = ['POST'])
def result():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No image selected for uploading')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join("static/upload/", filename))
            print('upload_image filename: ' + filename)

            uploaded = 'static/upload/' + filename
            print(uploaded)
            img_path = uploaded
            img = image.load_img(img_path, target_size = (150, 150))
            images = image.img_to_array(img)
            images = np.expand_dims(images, axis = 0)
            loaded_model = load_model("model.h5")
            predictions = loaded_model.predict(images)
            print("================================")
            print(filename)
            if predictions == 0:
                print("Covid positive")
                prediction = "Covid positive"
            else:
                print("Your report is normal")
                prediction = "Covid Negative"
            name = request.form['pname']
            age =  request.form['age']
            gender = request.form['gender']
    return render_template("predict.html",name = name, age = age, gender = gender, prediction = prediction, img = uploaded)
if __name__ == "__main__":
    app.run(debug=True)