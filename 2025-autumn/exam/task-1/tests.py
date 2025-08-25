import unittest
from main import task_1


class MyTestCase(unittest.TestCase):
	def test_1(self):
		self.assertEqual(task_1('7331'), '1337')

	def test_2(self):
		self.assertEqual(task_1('2017'), '1027')

if __name__ == '__main__':
	unittest.main()
