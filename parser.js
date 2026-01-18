const fs = require('fs');
const path = require('path');

class Parser {
  constructor(filePath) {
    this.filePath = filePath;
  }

  async readData() {
    try {
      const data = await fs.promises.readFile(this.filePath, 'utf8');
      return data;
    } catch (error) {
      throw new Error(`Failed to read file: ${error.message}`);
    }
  }

  parseData(data) {
    const parsedData = data.split('\n').map(line => line.split(','));
    return parsedData;
  }

  async parseFile() {
    const data = await this.readData();
    const parsedData = this.parseData(data);
    return parsedData;
  }
}

module.exports = Parser;