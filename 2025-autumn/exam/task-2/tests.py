import unittest
from main import task_2


class MyTestCase(unittest.TestCase):
	def test_1(self):
		input = [
			(4, [1, 2, 3, 3]),
			(4, [1, 1, 3, 3]),
			(5, [1, 2, 2, 1, 5]),
			(3, [2, 2, 3])
		]

		output = [
			'First',
			'Second',
			'Second',
			'Second',
		]

		self.assertEqual(task_2(input), output)


if __name__ == '__main__':
	unittest.main()
