import json
from pathlib import Path


class JsonReader:
    def __init__(self, file_path):
        self.file_path = Path(file_path)
        self.data = self.load_json()

    def load_json(self):
        try:
            with self.file_path.open('r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"File {self.file_path} not found.")
            return None
        except json.JSONDecodeError:
            print(f"Error decoding JSON from file {self.file_path}.")
            return None

    def get_data(self):
        return self.data
