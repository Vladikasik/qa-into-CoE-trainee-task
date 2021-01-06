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

	def _get_all_data(self):

		self._read_json(self.testcase_filename, self.json_from_testcase)

		print(self.json_from_testcase)

	def _read_json(self, filename, var_to_write):

		with open(filename, 'r') as file:

			print(json.load(file))
			#var_to_write = json.load(file)



test = First_task()
test._get_all_data()