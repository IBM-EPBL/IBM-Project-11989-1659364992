import numpy as np
from flask import Flask,request,render_template,jsonify
import pickle


app=Flask(__name__)
model=pickle.load(open('phishing_website.pkl','rb'))

@app.route('/')
def predict():
    return render_template('final.html')

@app.route('/',methods=['POST'])
def y_predict():
    url=request.form['url']
    checkprediction=model.predict(checkprediction)
    print(prediction)
    output=prediction
    if(output==1):
       pred='You are safe!!  This is a Legitimate Website.'
    else:
        pred='You are on the wrong site. Be cautious!'
    return render_template('final.html',prediction_text='{}'.format(pred),url=url)

@app.route('/',methods=['POST'])
def predict_api():
    data=request.get_json(force=True)
    prediction=model.y_predict([np.array(list(data.values()))])
    output=prediction[0]
    return jsonify(output)

if __name__=='__main__':
    app.run(debug=True)
