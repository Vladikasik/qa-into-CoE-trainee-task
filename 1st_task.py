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

	def _get_all_data(self):

		with open(self.testcase_filename, 'r') as file:
			self.json_from_testcase = json.load(file)

		with open(self.values_filename, 'r') as file:
			self.json_from_values = json.load(file)




test = First_task()
test._get_all_data()