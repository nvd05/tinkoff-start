import unittest
from task_2.task_2 import task_2

class Task2Tests(unittest.TestCase):
	def test_2(self):
		self.assertEqual(task_2('2'), 6)

	def test_3(self):
		self.assertEqual(task_2('3'), 28)
		
	def test_4(self):
		self.assertEqual(task_2('4'), 96)

	def test_20000(self):
		self.assertEqual(task_2('20000'), 79999998200239992)

if __name__ == '__main__':
	unittest.main()
