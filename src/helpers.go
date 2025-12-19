package helpers

import (
	"encoding/csv"
	"errors"
	"log"
	"os"
	"strconv"
	"strings"
)

func readCSVFile(filename string) ([][]string, error) {
	file, err := os.Open(filename)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	csvReader := csv.NewReader(file)
	records, err := csvReader.ReadAll()
	if err != nil {
		return nil, err
	}

	if len(records) == 0 {
		return nil, errors.New("no records found in the file")
	}

	return records, nil
}

func convertStringToInt(str string) (int, error) {
	value, err := strconv.Atoi(strings.TrimSpace(str))
	if err != nil {
		return 0, err
	}
	return value, nil
}

func convertStringToFloat(str string) (float64, error) {
	value, err := strconv.ParseFloat(strings.TrimSpace(str), 64)
	if err != nil {
		return 0, err
	}
	return value, nil
}

func logError(err error) {
	if err != nil {
		log.Printf("error: %v", err)
	}
}