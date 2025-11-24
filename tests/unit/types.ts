// types.ts
export type Severity = 'INFO' | 'WARNING' | 'ERROR';

export type Parser = {
  name: string;
  description: string;
};

export type Option = {
  name: string;
  description: string;
  value: string | number | boolean;
  required: boolean;
};

export type Rule = {
  id: string;
  description: string;
  severity: Severity;
  options: Option[];
};

export type Data = {
  source: string;
  data: string;
  rules: Rule[];
};

export type ParserConfig = {
  [key: string]: any;
};

export type ParserResponse = {
  data: Data;
};