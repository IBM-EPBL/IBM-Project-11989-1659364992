import numpy as np
import flask
from flask import request,render_template,Flask,jsonify
import pickle

app=Flask(__name__)
model=pickle.load(open('phishing_website.pkl','rb'))
