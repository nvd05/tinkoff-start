import unittest
from task_4 import task_4


class TestMinCycleLength(unittest.TestCase):

	def test_example_1(self):
		# Пример 1 из условия
		n = 3
		m = 3
		edges = [(1, 2), (2, 3), (1, 3)]
		self.assertEqual(task_4(n, m, edges), 3)
	
	def test_example_2(self):
		# Пример 2 из условия
		n = 6
		m = 7
		edges = [(1, 6), (6, 4), (4, 2), (2, 5), (5, 6), (2, 3), (3, 5)]
		self.assertEqual(task_4(n, m, edges), 3)
	
	def test_cycle_length_5(self):
		# Цикл длины 5
		n = 5
		m = 5
		edges = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)]
		self.assertEqual(task_4(n, m, edges), 5)
	
	def test_two_cycles(self):
		# Граф с двумя циклами: 3 и 4
		n = 5
		m = 6
		edges = [(1, 2), (2, 3), (3, 1), (3, 4), (4, 5), (5, 3)]
		self.assertEqual(task_4(n, m, edges), 3)
	
	def test_disconnected_graph_with_cycle(self):
		# Несвязный граф, но с циклом в одной компоненте
		n = 6
		m = 5
		edges = [(1, 2), (2, 3), (3, 1), (4, 5), (5, 6), (6, 4)]
		# В первой компоненте цикл длины 3, во второй цикл длины 3
		self.assertEqual(task_4(n, m, edges), 3)
	
	def test_star_graph(self):
		# Звезда (нет циклов)
		n = 5
		m = 4
		edges = [(1, 2), (1, 3), (1, 4), (1, 5)]
		self.assertEqual(task_4(n, m, edges), -1)
	
	def test_smallest_possible_cycle(self):
		# Минимально возможный цикл (треугольник)
		n = 3
		m = 3
		edges = [(1, 2), (2, 3), (3, 1)]
		self.assertEqual(task_4(n, m, edges), 3)

if __name__ == '__main__':
	unittest.main()

