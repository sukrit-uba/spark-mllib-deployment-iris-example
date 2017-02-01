# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 16:13:28 2017

@author: hduser
"""

from flask import Blueprint
main = Blueprint('main', __name__)

import json
from engine import Classifier

import logging 
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from flask import Flask, request, jsonify

@main.route("/api", methods=['POST'])
def predict():
    data = request.get_json(force=True)
    predict_request = [data['sl'], data['sw'], data['pl'], data['pw']]
    result = classification_engine.predict(predict_request)
    return jsonify(results=[result])
    
@main.route("/prediction/<string:features>", methods=["GET"])
def prediction(features):
    data = [float(x) for x in features.split(",")]
    output = classification_engine.predict(data)
    if output == 0:
        predict = "Iris-setosa"
    else:
        predict = "Iris-versicolor"
    return json.dumps(predict)
    
def create_app(spark_context):
    global classification_engine
    classification_engine = Classifier(spark_context)
    
    app = Flask(__name__)
    app.register_blueprint(main)
    return app
    