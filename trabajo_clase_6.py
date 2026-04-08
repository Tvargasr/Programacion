import json
import csv

class FileConverter:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(FileConverter, cls).__new__(cls)
        return cls._instance

    def convertFromJson(self, jsonFileStr):
        try:
            with open(jsonFileStr, 'r') as file:
                data = json.load(file)
            return data
        except Exception as e:
            raise Exception(f"Error leyendo JSON: {e}")

    def convertFromCSV(self, csvFileStr):
        try:
            result = []
            with open(csvFileStr, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    result.append(dict(row))
            return {"data": result}
        except Exception as e:
            raise Exception(f"Error leyendo CSV: {e}")


if __name__ == "__main__":
    converter1 = FileConverter()
    converter2 = FileConverter()

    print("Singleton working:", converter1 is converter2)
