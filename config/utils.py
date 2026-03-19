import os
import json

def load_config():
    """Loads configuration from a JSON file."""
    with open('config.json') as config_file:
        return json.load(config_file)

def get_config_value(key, default=None):
    """Gets the value of a configuration key, with a default value."""
    config = load_config()
    return config.get(key, default)

def get_data_file_path(file_name):
    """Gets the full path to a data file."""
    return os.path.join('data', file_name)

def read_data_file(file_name):
    """Reads the contents of a data file."""
    data_file_path = get_data_file_path(file_name)
    with open(data_file_path, 'r') as data_file:
        return data_file.read()

def write_data_file(file_name, data):
    """Writes data to a file."""
    data_file_path = get_data_file_path(file_name)
    with open(data_file_path, 'w') as data_file:
        data_file.write(data)

def load_json_data(file_name):
    """Loads data from a JSON file."""
    data = read_data_file(file_name)
    return json.loads(data)

def save_json_data(file_name, data):
    """Saves data to a JSON file."""
    write_data_file(file_name, json.dumps(data, indent=4))