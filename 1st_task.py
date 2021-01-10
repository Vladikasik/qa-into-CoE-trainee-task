import json


class FirstTask:

    def __init__(self):
        print('task init')

        # filenames
        self.testcase_filename = "TestcaseStructure.json"
        self.values_filename = "Values.json"

        self.error_filename = "error.json"

        self.result_filename = "result/StructureWithValues.json"

        # data variables
        self.json_from_testcase = None
        self.json_from_values = None
        self.values_dict = {}

        self.result = {}

    def _get_all_data(self):

        with open(self.testcase_filename, 'r', encoding='utf-8') as file:
            self.json_from_testcase = json.load(file)

        with open(self.values_filename, 'r', encoding='utf-8') as file:
            self.json_from_values = json.load(file)

    def transform(self):
        self._prepairing()

        for el in self.json_from_testcase["params"]:
            index_to_insert = self.json_from_testcase["params"].index(el)
            if "values" in el.keys():
                for val in el["values"]:
                    if self.values_dict[el["id"]] in list(val.values()):
                        value_to_insert = None
                        for title in el["values"]:
                            if title["id"] == self.values_dict[el["id"]]:
                                value_to_insert = title["title"]
                                break
                        self.result['params'][index_to_insert]["value"] = value_to_insert
            else:
                self.result["params"][index_to_insert]["value"] = self.values_dict[el['id']]

    def _prepairing(self):
        self._get_all_data()
        print('data_imported')
        self._values_to_dict()
        print('values to dict done')
        self.result = self.json_from_testcase

    def _values_to_dict(self):

        for i in self.json_from_values["values"]:
            self.values_dict[i['id']] = i['value']


test = FirstTask()
test.transform()
print(test.result)
