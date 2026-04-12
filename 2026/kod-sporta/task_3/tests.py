import unittest
from task_3.task_3 import task_3

class Task2Tests(unittest.TestCase):
	def test_1(self):
		n = 4
		m = 5
		refs = [
			[ 1, 2 ],
			[ 2, 3 ],
			[ 3, 4 ],
			[ 4, 1 ],
			[ 4, 3 ],
		]

		res = task_3(n, m, refs)

		self.assertEqual(res, [
			'1 2',
			'2 3', # 3 2
			'3 4', # 4 3
			'1 4',
			'3 4', # 4 3
		])

if __name__ == '__main__':
	unittest.main()
