import logging
import os
from typing import List, Dict

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def parse_file(file_path: str) -> List[Dict]:
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            parsed_data = []
            for line in lines:
                data = line.strip().split(',')
                parsed_data.append({'id': data[0], 'name': data[1], 'value': data[2]})
            return parsed_data
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        return []
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        return []

def write_to_file(file_path: str, data: List[Dict]) -> None:
    try:
        with open(file_path, 'w') as file:
            for item in data:
                file.write(f"{item['id']},{item['name']},{item['value']}\n")
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")

def get_file_size(file_path: str) -> int:
    try:
        return os.path.getsize(file_path)
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        return 0
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        return 0