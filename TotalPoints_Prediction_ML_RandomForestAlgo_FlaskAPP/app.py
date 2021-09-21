from flask import Flask, render_template, request
import requests
import pickle
import numpy as np
import sklearn

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        gen = int(request.form['gen'])
        height = int(request.form['height'])
        weight = int(request.form['weight'])
        abil = int(request.form['abilities'])
        hp = int(request.form['hp'])
        attack = int(request.form['attack'])
        defense = int(request.form['defense'])
        spatt = int(request.form['sp_attack'])
        spdef = int(request.form['sp_defense'])
        speed = int(request.form['speed'])
        base = int(request.form['basexp'])
        growth = request.form['growth']

        legendary = 0
        sublegendary = 0
        mythical = 0
        ptype = request.form['type']
        if(ptype == 'normal'):
            legendary = 0
            sublegendary = 0
            mythical = 0
        elif(ptype == 'is_legendary'):
            legendary = 1
            sublegendary = 0
            mythical = 0
        elif(ptype == 'is_sub_legendary'):
            legendary = 0
            sublegendary = 1
            mythical = 0
        elif(ptype == 'is_mythical'):
            legendary = 0
            sublegendary = 0
            mythical = 1

        prediction=model.predict([[gen,height,weight,abil,hp,attack,defense,spatt,spdef,speed,base,growth,legendary,sublegendary,mythical]])
        output=round(prediction[0],2)
        return render_template('index.html',prediction_text='Total Points! = {}'.format(output))

    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
