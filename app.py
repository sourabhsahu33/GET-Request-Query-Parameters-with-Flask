# Python program for Get Data Recevied in Flsk requests.
from flask import Flask, request
app = Flask(__name__)    # flask application module name.

# Accesses the Query string using URL parameters
@app.route('/query_example')    # create the route for query.
def query_example():
    language =  request.args.get('language')  # request object through args.get
    framework = request.args['framework']
    website = request.args.get('website')
    return '''<h1> The Language is : {} </h1>
              <h1> The framework is : {} </h1>
              <h1> The website is : {}  </h1>'''.format(language,framework, website)