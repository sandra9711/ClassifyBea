from flask import Flask, render_template,request
from keras.models import load_model


app = Flask(__name__)

categories = {0:'Jackfriut',1:'Mango'}

models = load_model('model.h5')

@app.route('/',methods=['GET', 'POST'])
def landing_page():
    return render_template('index.html')