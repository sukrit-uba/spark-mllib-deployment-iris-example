# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 16:26:23 2017

@author: hduser
"""

import time, sys, cherrypy, os
from paste.translogger import TransLogger
from app import create_app
from pyspark import SparkContext, SparkConf

def init_spark_context():
    conf = SparkConf().setAppName("Iris_classifier")
    sc = SparkContext(conf=conf, pyFiles=['/home/hduser/iris_classifier/engine.py', '/home/hduser/iris_classifier/app.py'])
    return sc
    
def run_server(app):
    app_logged = TransLogger(app)
    cherrypy.tree.graft(app_logged, '/')
    
    cherrypy.config.update({
        'engine.autoreload.on': True,
        'log.screen': True,
        'server.socket_port': 5000, 
        'server.socket_host': '127.0.0.1'
    })
    
    cherrypy.engine.start()
    cherrypy.engine.block()
    
if __name__ == "__main__":
    sc = init_spark_context()
    app = create_app(sc)
    run_server(app)