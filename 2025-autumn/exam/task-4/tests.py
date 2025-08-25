import unittest
from main import task_4


class MyTestCase(unittest.TestCase):
	def test_1(self):
		input = [
			(0, 10, 5),
			(0, 10, 2),
			(0, 0, 1)
		]

		self.assertEqual(task_4(3, input), 8)

	def test_2(self):
		input = [
			(0, 2, 3),
			(4, 0, 4),
			(1, 0, 5)
		]

		self.assertEqual(task_4(3, input), 7)

if __name__ == '__main__':
	unittest.main()
