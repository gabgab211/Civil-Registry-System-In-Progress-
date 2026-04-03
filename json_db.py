import json
from record import Record


class BaseDatabase:
    def load(self):
        raise NotImplementedError

    def save(self, records):
        raise NotImplementedError


class JSONDatabase(BaseDatabase):

    def __init__(self, filepath):
        self.filepath = filepath

    def load(self):
        try:
            with open(self.filepath, "r") as f:
                content = f.read().strip()

                if not content:
                    return []
                data = json.loads(content)

        except FileNotFoundError:
            return []

        return [Record.create_from_dict(item) for item in data]

    def save(self, records):
        data = [record.to_dict() for record in records]

        with open(self.filepath, "w") as f:
            json.dump(data, f, indent=4)
