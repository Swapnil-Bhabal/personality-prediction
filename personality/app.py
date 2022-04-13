import numpy as np
from flask import Flask, render_template, request
from sklearn.preprocessing import StandardScaler
import joblib
import random
app = Flask(__name__)
model = joblib.load("train_mode.pkl")
scaler = StandardScaler()

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/info')
def information():
    return render_template('information.html')

@app.route('/form')
def form():
    return render_template('first-question.html')

@app.route('/submit',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
     
      openness = request.form['openness']
      neuroticism = request.form['neuroticism']
      conscientiousness = request.form['conscientiousness']
      agreeableness = request.form['agreeableness']
      extraversion = request.form['extraversion']
      result = [openness,neuroticism, conscientiousness, agreeableness, extraversion]
      s=model.predict([result])
     
      #personality=random.choice("Extraverted Serious Responsible Lively Dependable".split())
      #a=personality
      return render_template("submit.html",answer = s[0])

if __name__ == '__main__':
    app.run()