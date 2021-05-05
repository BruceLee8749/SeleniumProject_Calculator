import json


class readJson:
    def readJson(self):
        with open("../data/data.json", 'r', encoding="UTF-8") as f:
            self.dict_data = json.load(f)
            self.list1 = list(self.dict_data.values())
            # print(self.list1)
        return self.list1



