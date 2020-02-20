import json

class Dict:
    def __init__(self):
        self.mapEntity = {}

    def load(self):
        self.mapEntity = json.load(open("mapEntity.json"))

    def get_identifier(self,identifier):
            return self.mapEntity[identifier]

    def save_id(self,identifier,id):
        self.mapEntity[identifier] = str(id)
        json.dump(self.mapEntity, open("mapEntity.json", 'w'))

    def contains_identifier(self,identifier):
        return identifier in self.mapEntity
