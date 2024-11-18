from flask import Blueprint, request, jsonify
from util.hash import process_json  # Import process_json function

# Create a Blueprint for vendor routes
vendor_bp = Blueprint('vendor', __name__)

@vendor_bp.route('/process', methods=['POST'])
def process_vendor_data():
    # Get JSON data from the request
    data = request.get_json()

    if not data:
        return jsonify({"error": "No JSON data provided"}), 400

    # Process the JSON data
    result = process_json(data)

    # Return the result as JSON
    return jsonify(result)

