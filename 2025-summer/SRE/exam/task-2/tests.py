from unittest import TestCase, main
from main import task_2


class TestTask2(TestCase):
	def test_1(self):
		self.assertTrue(task_2('WSEN'))

	def test_2(self):
		self.assertTrue(task_2('WEWWEW'))

	def test_3(self):
		self.assertFalse(task_2('WWSN'))

	def test_4(self):
		self.assertFalse(task_2('N'))

if __name__ == '__main__':
	main()
