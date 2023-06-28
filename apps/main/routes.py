from flask import Flask, request, render_template, Blueprint, redirect, url_for, Response, jsonify
from apps.main.form import RegistrationForm, ImageForm
from werkzeug.utils import secure_filename
import os
import cv2
from apps.facerecognition import Face_Recognition
import matplotlib.image as matimg
import base64
import numpy as np



main = Blueprint('main', __name__)
UPLOAD_FOLDER = 'apps/static/upload'
@main.route('/thanks', methods=['GET', 'POST'])
def thanks():
    return render_template('Thanks.html', title='Thanks')

@main.route('/subscribe', methods=['GET', 'POST'])
def subscribe():
    return render_template('Subscribed.html', title='Subscribe')

@main.route('/', methods=['GET', 'POST'])
def home():
    form = RegistrationForm()
    if form.validate_on_submit():
        return redirect(url_for('main.thanks'))
    return render_template('index.html', form=form, title='Home')

@main.route('/contact', methods=['GET', 'POST'])
def contact():
    form = RegistrationForm()
    if form.validate_on_submit():
        return redirect(url_for('main.thanks'))
    return render_template('index.html', form=form, title='Contact')

@main.route('/gender', methods=['GET', 'POST'])
def upload():
    form = ImageForm()
    if request.method == 'POST' and form.validate_on_submit():
        f = form.image.data
        filename = secure_filename(f.filename)
        f.save(os.path.join(UPLOAD_FOLDER, filename))
        pred_image , prediction = Face_Recognition(os.path.join(UPLOAD_FOLDER, filename))
        pred_filename = 'pred_'+filename
        cv2.imwrite(f'apps/static/predict/{pred_filename}', pred_image)
        #print(prediction)
        #generate report
        report = []
        for i,obj in enumerate(prediction):
            gray_image = obj['roi']
            eigen_image = obj['eig_img']
            gender_name = obj['prediction_name']
            score = round(obj['score']*100,2)

            #Save grayscale and eigen image in predict folder
            gray_image_name = f'roi_{i}_{filename}'
            eig_image_name = f'eigen_{i}_{filename}'
            matimg.imsave(f'apps/static/predict/{gray_image_name}', gray_image,cmap='gray')
            matimg.imsave(f'apps/static/predict/{eig_image_name}', eigen_image,cmap='gray')

            #Save report
            report.append([gray_image_name,eig_image_name,gender_name,score])

        return render_template('Gender.html',title = 'Gender Detection',form = form,fileupload = True,report=report,pred_image = pred_filename)


    return render_template('Gender.html',form = form, title = 'Gender Detection',fileuplpad = False)






