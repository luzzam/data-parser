// types.ts
export interface ParsedData {
  id: number;
  name: string;
  values: number[];
}

export interface ParseOptions {
  delimiter: string;
  skipRows: number;
}

export type ParseResult = ParsedData[] | Error;

export enum ParseErrorType {
  FILE_NOT_FOUND,
  INVALID_DELIMITER,
  PARSE_ERROR,
}

export class ParseError extends Error {
  type: ParseErrorType;
  constructor(type: ParseErrorType, message: string) {
    super(message);
    this.type = type;
  }
}