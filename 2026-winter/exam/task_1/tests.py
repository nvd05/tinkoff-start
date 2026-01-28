import unittest
from task_1 import task_1


class TestTask1(unittest.TestCase):

	def test_example_1(self):
		self.assertEqual(task_1('682902'), '202689')

	def test_example_2(self):
		self.assertEqual(task_1('01'), '10')

	def test_single_digit(self):
		self.assertEqual(task_1('5'), '5')

	def test_all_zeros_except_one(self):
		self.assertEqual(task_1('0001'), '1000')

	def test_no_zeros(self):
		self.assertEqual(task_1('987654321'), '123456789')

	def test_already_minimal(self):
		self.assertEqual(task_1('123'), '123')

	def test_with_leading_zero_case(self):
		self.assertEqual(task_1('100'), '100')

	def test_complex_case(self):
		self.assertEqual(task_1('301'), '103')

	def test_all_zeros_but_one(self):
		self.assertEqual(task_1('0007'), '7000')

	def test_sorted_with_zeros_inside(self):
		self.assertEqual(task_1('10203'), '10023')

if __name__ == '__main__':
	unittest.main()
