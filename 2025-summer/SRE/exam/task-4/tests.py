import unittest
from DeepSeek import task_4


class MyTestCase(unittest.TestCase):

	def test_example_1(self):
		self.assertEqual(task_4(1, 1), 2)

	def test_example_2(self):
		self.assertEqual(task_4(2, 4), 7)

	def test_example_3(self):
		self.assertEqual(task_4(3, 7), 14)

if __name__ == '__main__':
	unittest.main()
