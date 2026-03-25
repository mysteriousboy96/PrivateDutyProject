# utils/data_reader_utli.py
import json

def read_json_data(file_path):
    """
    Read JSON file and return as list of dictionaries
    """
    try:
        with open(file_path, 'r') as file:
            json_data = json.load(file)
            # Return as-is (list of dictionaries) - NO CONVERSION TO TUPLES
            return json_data
    except Exception as e:
        print(f"Error reading JSON data: {e}")
        raise

# If you need both versions, create separate functions
def read_json_as_dicts(file_path):
    """Return JSON as list of dictionaries"""
    with open(file_path, 'r') as file:
        return json.load(file)

def read_json_as_tuples(file_path):
    """Return JSON as list of tuples (for parameterization)"""
    with open(file_path, 'r') as file:
        json_data = json.load(file)
        return [tuple(record.values()) for record in json_data]