import unittest
from main import task_3


class TestTask3(unittest.TestCase):
	def test_no_people(self):
		self.assertEqual(task_3(0, [], []), 0)

	def test_single_person_no_links(self):
		self.assertEqual(task_3(1, [10], []), 10)

	def test_two_people_direct_link(self):
		peoples = 2
		energies = [5, 3]
		links = [[1, 2]]
		self.assertEqual(task_3(peoples, energies, links), 3)

	def test_disconnected_components(self):
		peoples = 4
		energies = [2, 5, 3, 1]
		links = [[1, 2], [3, 4]]
		self.assertEqual(task_3(peoples, energies, links), 3)  # min(2,5) + min(3,1) = 2 + 1 = 3

	def test_star_topology(self):
		peoples = 4
		energies = [1, 10, 10, 10]
		links = [[1, 2], [1, 3], [1, 4]]
		self.assertEqual(task_3(peoples, energies, links), 1)

	def test_linear_chain(self):
		peoples = 3
		energies = [3, 2, 1]
		links = [[1, 2], [2, 3]]
		self.assertEqual(task_3(peoples, energies, links), 1)

	def test_all_same_energy(self):
		peoples = 3
		energies = [5, 5, 5]
		links = [[1, 2], [2, 3]]
		self.assertEqual(task_3(peoples, energies, links), 5)

	def test_no_links_multiple_people(self):
		peoples = 3
		energies = [1, 2, 3]
		links = []
		self.assertEqual(task_3(peoples, energies, links), 6)  # 1 + 2 + 3

if __name__ == '__main__':
	unittest.main()
