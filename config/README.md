# data-parser/README.md

"""
Data Parser
-----------

A Python library for parsing and processing large datasets.

Installation
------------

To install, use pip:

    pip install -r requirements.txt

Usage
-----

To use the parser, import the `Parser` class and create an instance:

    from data_parser import Parser

    parser = Parser('path/to/data.csv')
    parser.parse()

    # Access parsed data as a DataFrame
    data = parser.data

    # Export data to CSV
    parser.export('output.csv')

Requirements
------------

- Python >= 3.8
- pandas
- numpy

Contributing
------------

Contributions are welcome! Please see the `CONTRIBUTING.md` file for guidelines.

License
-------

MIT License

Copyright (c) 2023 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import pathlib
import re

__all__ = ['Parser']

class Parser:
    def __init__(self, path):
        self.path = pathlib.Path(path)
        self.data = None

    def parse(self):
        import pandas as pd
        self.data = pd.read_csv(self.path)

    def export(self, path):
        self.data.to_csv(path, index=False)

if __name__ == '__main__':
    parser = Parser('data.csv')
    parser.parse()
    parser.export('output.csv')