import logging
import argparse
from data_parser import DataParser

def main():
    parser = argparse.ArgumentParser(description='Data Parser')
    parser.add_argument('-f', '--file', help='Input file path', required=True)
    parser.add_argument('-o', '--output', help='Output file path', required=True)
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    try:
        data_parser = DataParser(args.file)
        data = data_parser.parse()
        data_parser.write_output(data, args.output)
        logging.info('Data parsing completed successfully')
    except Exception as e:
        logging.error(f'Error occurred: {str(e)}')

if __name__ == '__main__':
    main()