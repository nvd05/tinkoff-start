import unittest
from main import task_5


class MyTestCase(unittest.TestCase):
	def test_1(self):
		self.assertEqual(task_5(3, 2), 10)

	def test_2(self):
		self.assertEqual(task_5(4, 3), 51)


if __name__ == '__main__':
	unittest.main()
