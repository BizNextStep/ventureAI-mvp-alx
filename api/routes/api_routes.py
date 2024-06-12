# Import necessary libraries
from flask import Flask, request, jsonify
from flask_cors import CORS

# Create a new Flask application
app = Flask(__name__)

# Enable cross-origin resource sharing (CORS) for the application
CORS(app)

# Define a route for handling business ideas
@app.route('/api/business_ideas', methods=['GET', 'POST'])
def business_ideas():
    # Check if the request method is GET
    if request.method == 'GET':
        # Fetch business ideas (replace with actual data)
        return jsonify([])  # Replace with actual data
    # Check if the request method is POST
    elif request.method == 'POST':
        # Process and save new business idea
        data = request.json
        # Return the new business idea with a 201 status code
        return jsonify(data), 201

# Define a route for handling user information
@app.route('/api/user', methods=['GET', 'POST'])
def user():
    # Check if the request method is GET
    if request.method == 'GET':
        # Fetch user information (replace with actual data)
        return jsonify({"user": "test user"})  # Replace with actual data
    # Check if the request method is POST
    elif request.method == 'POST':
        # Create new user
        data = request.json
        # Return the new user with a 201 status code
        return jsonify(data), 201

# Run the application in debug mode if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
