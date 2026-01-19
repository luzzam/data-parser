import logging
import os
import argparse
from data_parser import parser

def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    parser_instance = parser.DataParser()
    arg_parser = argparse.ArgumentParser(description='Data Parser')
    arg_parser.add_argument('--input', type=str, required=True, help='Input file path')
    arg_parser.add_argument('--output', type=str, required=True, help='Output file path')
    args = arg_parser.parse_args()
    try:
        parser_instance.parse_data(args.input, args.output)
        logging.info('Data parsed successfully')
    except Exception as e:
        logging.error('Error occurred: %s', str(e))

if __name__ == '__main__':
    main()