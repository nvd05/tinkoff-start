import unittest
from main import task_3


class MyTestCase(unittest.TestCase):
	def test_1(self):
		self.assertEqual(task_3([1, 2, 1, 4]), 11)


if __name__ == '__main__':
	unittest.main()
