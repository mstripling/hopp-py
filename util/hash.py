import hashlib
import json

def hash_string(input_string):
    """Hash a string using SHA-256."""
    sha256_hash = hashlib.sha256()
    sha256_hash.update(input_string.encode('utf-8'))
    return sha256_hash.hexdigest()

def process_json(input_json):
    """Merge plain data and hash data, hashing values in the 'hash' sub-object."""
    # Initialize the result dictionary
    result = {}

    # Add the plain data directly to the result
    result.update(input_json['plain'])

    # Iterate through the 'hash' sub-object, hash the values and add them to the result
    for key, value in input_json['hash'].items():
        result[key] = hash_string(value)
    
    return result
"""
if __name__ == "__main__":
    # Sample input JSON string (can be replaced with input from file or API)
    input_data = '''{
        "plain": {
            "name": "Alice",
            "email": "alice@example.com"
        },
        "hash": {
            "password": "mypassword123",
            "credit_card": "1234567812345678"
        }
    }'''

    # Parse the input JSON
    input_json = json.loads(input_data)

    # Process the JSON to combine plain and hashed data
    processed_json = process_json(input_json)

    # Print the resulting combined JSON
    print(json.dumps(processed_json, indent=4))
"""
