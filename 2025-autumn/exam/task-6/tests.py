import unittest
from main import task_6


class MyTestCase(unittest.TestCase):
	def test_1(self):
		ribs = [
			(1, 2),
			(3, 1),
			(2, 4),
			(5, 2),
			(3, 4),
			(5, 3)
		]

		output = [
			(2, 1),
			(3, 1),
			(2, 4),
			(5, 2),
			(3, 4),
			(5, 3),
		]

		self.assertEqual(task_6(5, 6, ribs), output)

	def test_2(self):
		ribs = [
			(5, 5),
			(1, 2),
			(1, 3),
			(2, 4),
			(3, 4),
			(3, 5),
		]

		output = []

		self.assertEqual(task_6(5, 5, ribs), output)

if __name__ == '__main__':
	unittest.main()
