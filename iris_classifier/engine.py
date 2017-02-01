# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 15:14:47 2017

@author: hduser
"""

from pyspark.mllib.classification import SVMWithSGD, SVMModel
from pyspark.mllib.regression import LabeledPoint

import logging 
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Classifier:
    def __init__(self, sc):
        logger.info("Starting up the Classification Engine..")
        self.sc = sc
        
        #load data
        logger.info("Loading up data..")
        iris_data_raw_RDD = self.sc.textFile("/home/hduser/iris-data.txt")
        self.iris_data_parsed_RDD = iris_data_raw_RDD.map(self.parsePoint)
        #self.train_model()
        self.model = SVMModel.load(self.sc, "/home/hduser/pythonSVMWithSGDModel")        
        
    def parsePoint(self, line):
        values = [float(x) for x in line.split(' ')]
        return LabeledPoint(values[-1], values[:4])
        
    def train_model(self):
        logger.info("Training SVM model..")
        self.model = SVMWithSGD.train(self.iris_data_parsed_RDD, iterations=100)
        logger.info("SVM model built!")
        
    def predict(self, feature_vector):
        return self.model.predict(feature_vector)