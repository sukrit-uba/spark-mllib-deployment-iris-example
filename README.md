# spark-mllib-deployment-iris-example

engine.py contains the main prediction engine which builds a SVM model for iris flower classification. The model has already been trained and saved in directory pythonSVMWithSGDModel. For further use the model is just loaded from the directory. 

app.py builds a flask app build on top of the sparkmllib model accepting post and get requests.

server.py initializes a spark context and runs a server on port 5000 combining app.py and engine.py. Python module named cherrypy is used to run the server. 

Running server.py using spark-submit runs the whole app. 

Origional tutorial is here: <br>
https://www.codementor.io/spark/tutorial/building-a-recommender-with-apache-spark-python-example-app-part1<br>
https://www.codementor.io/spark/tutorial/building-a-web-service-with-apache-spark-flask-example-app-part2<br>

Code repo<br>
https://github.com/jadianes/spark-movie-lens
