import logging
import os
from datetime import datetime

def setup_logger(logger_name, log_file, level=logging.INFO):
    l = logging.getLogger(logger_name)
    formatter = logging.Formatter('%(asctime)s : %(name)s : %(levelname)s : %(message)s')
    fileHandler = logging.FileHandler(log_file, mode='w')
    fileHandler.setFormatter(formatter)
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)
    l.setLevel(level)
    l.addHandler(fileHandler)
    l.addHandler(streamHandler)
    return l

def get_current_timestamp():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def get_project_root() -> str:
    return os.path.dirname(os.path.abspath(__file__))

def load_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        logging.error(f"File {file_path} not found")
        return None

def save_file(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
    except Exception as e:
        logging.error(f"Failed to save file {file_path}: {str(e)}")

def is_valid_file(file_path):
    if not os.path.exists(file_path):
        return False
    if not os.path.isfile(file_path):
        return False
    return True

def get_file_extension(file_path):
    return os.path.splitext(file_path)[1]

def get_file_name(file_path):
    return os.path.basename(file_path)

def remove_file_extension(file_name):
    return os.path.splitext(file_name)[0]