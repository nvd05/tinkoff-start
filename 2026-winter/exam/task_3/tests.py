import unittest
from task_3 import task_3

class TestTask3(unittest.TestCase):
	def test_example_1(self):
		input_data = '5\n0\n1\n011\n11011\n01101\n'
		expected = '0\n1\n2\n6\n2'
		result = task_3(input_data)
		self.assertEqual(result, expected)

	def test_single_zero(self):
		input_data = '1\n0\n'
		expected = '0'
		result = task_3(input_data)
		self.assertEqual(result, expected)

	def test_single_one(self):
		input_data = '1\n1\n'
		expected = '1'
		result = task_3(input_data)
		self.assertEqual(result, expected)

	def test_all_ones(self):
		input_data = '1\n111\n'
		expected = '9' # 3*3 = 9
		result = task_3(input_data)
		self.assertEqual(result, expected)

	def test_all_zeros(self):
		input_data = '1\n0000\n'
		expected = '0'
		result = task_3(input_data)
		self.assertEqual(result, expected)

	def test_mixed_1(self):
		input_data = '1\n010\n'
		expected = '1'
		result = task_3(input_data)
		self.assertEqual(result, expected)

	def test_mixed_2(self):
		input_data = '1\n1010\n'
		expected = '1'
		result = task_3(input_data)
		self.assertEqual(result, expected)

	def test_large_gap(self):
		input_data = '1\n10001\n'
		expected = '1'
		result = task_3(input_data)
		self.assertEqual(result, expected)

	def test_wrap_around(self):
		input_data = '1\n110011\n'
		# Максимальная длина единиц: 2 (первые две) и 2 (последние две) -> циклически 2+2=4
		# (4+1)*(4+1)//4 = 25//4 = 6
		expected = '6'
		result = task_3(input_data)
		self.assertEqual(result, expected)

	def test_multiple_test_cases(self):
		input_data = '''3
00
111
0101
'''
		expected = '0\n9\n1'
		result = task_3(input_data)
		self.assertEqual(result, expected)

	def test_empty_string(self):
		# По условию длина строки >=1, но проверим на случай
		input_data = '1\n\n'
		expected = '0'  # Пустая строка -> длина 0 -> площадь 0
		result = task_3(input_data)
		self.assertEqual(result, expected)

	def test_long_consecutive_ones(self):
		input_data = '1\n' + '1' * 100 + '\n'
		expected = str(100 * 100)  # n*n
		result = task_3(input_data)
		self.assertEqual(result, expected)

	def test_alternating(self):
		input_data = '1\n10101\n'
		expected = '1'
		result = task_3(input_data)
		self.assertEqual(result, expected)

	def test_edge_case_1(self):
		input_data = '1\n110110\n'
		# Максимальная длина: внутренние 2, или префикс+суффикс 2+1=3 -> M=3
		# (3+1)*(3+1)//4 = 16//4 = 4
		expected = '4'
		result = task_3(input_data)
		self.assertEqual(result, expected)

	def test_edge_case_2(self):
		input_data = '1\n01110\n'
		# Все единицы подряд: длина 3 -> M=3
		# (3+1)*(3+1)//4 = 16//4 = 4
		expected = '4'
		result = task_3(input_data)
		self.assertEqual(result, expected)

if __name__ == '__main__':
	unittest.main()
