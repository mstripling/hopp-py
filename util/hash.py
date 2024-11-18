import hashlib
import json

def hash_string(input_string):
    # Hash and format as hex
    sha256_hash = hashlib.sha256()
    sha256_hash.update(input_string.encode('utf-8'))
    return sha256_hash.hexdigest()

def process_json(input_json):
    # Initialize the result dictionary
    result = {}

    # Previous wasy of adding plain data directly to the result. Test which is better
    # result.update(input_json['plain'])

    for key, value in input_json['plain'].items():
        result[key] = value

    # Iterate through the hash sub-object, hash the values and add them to the result
    for key, value in input_json['hash'].items():
        result[key] = hash_string(value)
    
    return result
