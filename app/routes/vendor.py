from flask import Blueprint, request, jsonify
from util.hash import process_json  # Import the process_json function

# Create a Blueprint for vendor routes
vendor_bp = Blueprint('vendor', __name__)

@vendor_bp.route('/process', methods=['POST'])
def process_vendor_data():
    # Get JSON data from the request
    data = request.get_json()

    if not data:
        return jsonify({"error": "No JSON data provided"}), 400

    # Process the JSON data using the process_json function
    result = process_json(data)

    # Return the result as a JSON response
    return jsonify(result)

