from flask import Flask, render_template, request, url_for, jsonify
import numpy as np
import pickle
import nltk
import os
nltk.download("vader_lexicon")

app = Flask(__name__)

#picFolder=os.path.join('static','plots')
#app.config['UPLOAD_FOLDER']=picFolder

from nltk.sentiment.vader import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

@app.route('/index.html')
def home():
    imagelist=os.listdir('static/plots')
    imagelist=['plots/'+ image for image in imagelist]
    return render_template("index.html", imagelist=imagelist)

@app.route('/')
def home2():
    imagelist=os.listdir('static/plots')
    imagelist=['plots/'+ image for image in imagelist]
    return render_template("index.html",imagelist=imagelist)

@app.route('/analyze.html')
def analysis():
    imagelist=os.listdir('static/plots')
    imagelist=['plots/'+ image for image in imagelist]
    return render_template("analyze.html",imagelist=imagelist)

@app.route('/analyze.html', methods=['GET', 'POST'])
def predict():
    imagelist=os.listdir('static/plots')
    imagelist=['plots/'+ image for image in imagelist]
    if request.method == "POST":
        name=request.form['name']
        date=request.form['date']
        prodtype=request.form['prodtype']
        rating=request.form['rating']
        message = request.form['message']
        ps = sia.polarity_scores(message)
        if ps['compound']  > 0:
            result = 'Positive'
            res='1'
        elif ps['compound'] == 0:
            result = 'Neutral'
            res='0'
        else:
            result = 'Negative'
            res='-1'
        prob = ps['compound']

        file=open("data.csv","a")
        file.write("\n"+name+","+date+","+prodtype+","+rating+","+message+","+str(result)+","+str(res)+"\n")
        file.close()
        return render_template('/analyze.html', predictions=result, name=name, proba=prob, mes = message, imagelist=imagelist)
        

if __name__ =="__main__":
    app.run(debug=True)