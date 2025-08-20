from main import task_1
from unittest import TestCase, main


class TestTask1(TestCase):

	def test_example_1(self):
		"""Тест из первого примера: 1 2 3 4 5 1 2 3"""
		numbers = [1, 2, 3, 4, 5, 1, 2, 3]
		result = task_1(numbers)
		self.assertEqual(result, ['5', '3'])
		self.assertEqual(len(result), 2)

	def test_example_2(self):
		"""Тест из второго примера: 1 1 2 3 4 1 2 3 1 2"""
		numbers = [1, 1, 2, 3, 4, 1, 2, 3, 1, 2]
		result = task_1(numbers)
		self.assertEqual(result, ['1', '4', '3', '2'])
		self.assertEqual(len(result), 4)

	def test_single_approach(self):
		"""Тест с одним подходом"""
		numbers = [1, 2, 3, 4, 5]
		result = task_1(numbers)
		self.assertEqual(result, ['5'])
		self.assertEqual(len(result), 1)

	def test_multiple_ones_only(self):
		"""Тест только с единицами"""
		numbers = [1, 1, 1, 1]
		result = task_1(numbers)
		self.assertEqual(result, ['1', '1', '1', '1'])
		self.assertEqual(len(result), 4)

	def test_ones_at_beginning_and_end(self):
		"""Тест с единицами в начале и конце"""
		numbers = [1, 2, 3, 1, 4, 5, 1]
		result = task_1(numbers)
		self.assertEqual(result, ['3', '3', '1'])
		self.assertEqual(len(result), 3)

	def test_no_ones(self):
		"""Тест без единиц (один длинный подход)"""
		numbers = [2, 3, 4, 5]
		result = task_1(numbers)
		self.assertEqual(result, ['4'])
		self.assertEqual(len(result), 1)

	def test_single_element_one(self):
		"""Тест с одной единицей"""
		numbers = [1]
		result = task_1(numbers)
		self.assertEqual(result, ['1'])
		self.assertEqual(len(result), 1)

	def test_single_element_not_one(self):
		"""Тест с одним элементом не единицей"""
		numbers = [5]
		result = task_1(numbers)
		self.assertEqual(result, ['1'])
		self.assertEqual(len(result), 1)

	def test_custom_case(self):
		"""Кастомный тест: любое число, 1 2 3 1 2 1"""
		numbers = [5, 1, 2, 3, 1, 2, 1]
		result = task_1(numbers)
		self.assertEqual(result, ['1', '3', '2', '1'])
		self.assertEqual(len(result), 4)

	def test_large_numbers(self):
		"""Тест с большими числами"""
		numbers = [1, 100, 200, 1, 50, 1, 999]
		result = task_1(numbers)
		self.assertEqual(result, ['3', '2', '2'])
		self.assertEqual(len(result), 3)


if __name__ == '__main__':
	main()
