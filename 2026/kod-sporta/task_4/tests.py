import unittest
from task_4.task_4 import task_4

class Task2Tests(unittest.TestCase):
	def test_1(self):
		n = 2
		k = 1
		res = task_4(n, k)

		self.assertEqual(res, 8)

	def test_2(self):
		n = 1337
		k = 228
		res = task_4(n, k)

		self.assertEqual(res, 341)

if __name__ == '__main__':
	unittest.main()
