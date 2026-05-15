from flask import Flask, render_template, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Get the port number from the environment variable
port = int(os.environ.get('PORT', 8080))

# Define a dictionary to store car model information
# This should be replaced with a database connection in a real application

car_models = {
    'tesla': {'name': 'Tesla', 'description': 'Electric car', 'image': 'tesla.jpg'},
    'toyota': {'name': 'Toyota', 'description': 'Gasoline car', 'image': 'toyota.jpg'},
    'honda': {'name': 'Honda', 'description': 'Gasoline car', 'image': 'honda.jpg'}
}

# Define a route for the homepage
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', car_models=car_models)

# Define a route for each car model page
@app.route('/<car_model>', methods=['GET'])
def car_model_page(car_model):
    if car_model in car_models:
        return render_template('car_model.html', car_model=car_models[car_model])
    else:
        return 'Car model not found', 404

# Run the app
if __name__ == '__main__':
    app.run(port=port)