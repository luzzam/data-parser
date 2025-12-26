import os
import argparse
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def parse_arguments():
    parser = argparse.ArgumentParser(description='Data Parser')
    parser.add_argument('--input', help='Input file path', required=True)
    parser.add_argument('--output', help='Output file path', required=True)
    return parser.parse_args()

def read_input_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        logging.error(f'File not found: {file_path}')
        return None

def parse_data(data):
    parsed_data = []
    for line in data:
        # assuming data is comma-separated
        parsed_line = line.strip().split(',')
        parsed_data.append(parsed_line)
    return parsed_data

def write_output_file(file_path, data):
    try:
        with open(file_path, 'w') as file:
            for line in data:
                file.write(','.join(line) + '\n')
    except Exception as e:
        logging.error(f'Error writing to file: {e}')

def main():
    args = parse_arguments()
    input_data = read_input_file(args.input)
    if input_data:
        parsed_data = parse_data(input_data)
        write_output_file(args.output, parsed_data)
        logging.info('Data parsed and written to output file successfully')

if __name__ == '__main__':
    main()