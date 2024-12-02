# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, request

from db.CreateUpdate import create_item, update_item
from db.MariaDbConnector import connect
from db.Search import search_by_field_name_pattern, search_by_field_name_and_value, retrieve_all

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

@app.route('/search/pattern/<field_name>/<pattern>')
def search(field_name, pattern):
    return search_by_field_name_pattern(field_name, pattern)

@app.route('/search/strict/<field_name>/<value>')
def search_strict(field_name, value):
    return search_by_field_name_and_value(field_name, value)

@app.route('/storage/get-all')
def get_all():
    return retrieve_all()

@app.route('/storage/add', methods=['PUT'])
def add():
    # wrap return value in a dictionary
    return create_item(request.json)

@app.route('/storage/update', methods=['POST'])
def update():
    # wrap return value in a dictionary
    return update_item(request.json)



# main driver function
if __name__ == '__main__':

    connect()

    # run() method of Flask class runs the application
    # on the local development server.
    app.run(port=3390)