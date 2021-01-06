import json

class First_task:

	def __init__(self):

		# filenames
		self.testcase_filename = "TestcaseStructure.json"
		self.values_filename = "Values.json"

		self.error_filename = "error.json"

		self.result_filename = "result/StructureWithValues.json"

		# data variables
		self.json_from_testcase = None
		self.json_from_values = None
		self.values_dict = {}

	def _get_all_data(self):

		with open(self.testcase_filename, 'r') as file:
			self.json_from_testcase = json.load(file)

		with open(self.values_filename, 'r') as file:
			self.json_from_values = json.load(file)

	def transform(self):
		self._prepairing()

		for i in self.json_from_testcase["params"]:
			# print(i)
			print()

	def _prepairing(self):
		self._get_all_data()
		print('data_imported')
		self._values_to_dict()
		print('values to dict done')

	def _values_to_dict(self):
		for i in self.json_from_values["values"]:
			self.values_dict[i['id']] = i['value']

		print()



test = First_task()
test.transform()