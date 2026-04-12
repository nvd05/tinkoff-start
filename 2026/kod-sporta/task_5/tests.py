import unittest
from task_5.task_5 import task_5

class Task2Tests(unittest.TestCase):
	def test_1(self):
		n, m = 4, 5
		v_costs = [0, 1, 1, 1] # Чтение стоимостей вертикальных дорог V
		h_costs = [1, 1, 0, 1, 1] # Чтение стоимостей горизонтальных дорог H

		res = task_5(n, m, v_costs, h_costs)
		self.assertEqual(res, 2)

if __name__ == '__main__':
	unittest.main()
