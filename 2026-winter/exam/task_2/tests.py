import unittest
from task_2 import task_2


class TestTask2(unittest.TestCase):

	def test_already_good(self):
		'''Тест из условия примера 1'''

		s = 'tbankstudy'
		result = task_2(s)
		self.assertEqual(result, 0, f'Для строки \'{s}\' ожидалось 0, получено {result}')

	def test_example2(self):
		'''Тест из условия примера 2'''

		s = 'studtbankk'
		result = task_2(s)
		self.assertEqual(result, 5, f'Для строки \'{s}\' ожидалось 5, получено {result}')

	def test_good_reverse_order(self):
		'''Тест, когда подстроки в обратном порядке'''

		s = 'studytbank'
		result = task_2(s)
		self.assertEqual(result, 0)

	def test_no_common_part(self):
		'''Тест, когда подстроки не пересекаются и нет общих частей'''

		s = 'aaaaabbbbb'
		result = task_2(s)
		# Нужно заменить 5 символов на tbank и 5 на study = 10
		# Но можно сделать пересечение
		expected = 8  # Например: tbankstudy (0+8) или studytbank (8+0)
		self.assertEqual(result, expected)

	def test_partial_overlap(self):
		'''Тест с частичным пересечением'''
		s = 'tbanystudy'
		result = task_2(s)
		# 'tbanystudy': tbank (заменить 'y' на 'k') = 1
		#                study (уже есть) = 0
		# Итого: 1
		self.assertEqual(result, 1)

	def test_full_overlap(self):
		'''Тест с полным пересечением (невозможным)'''
		s = 'tbannk'
		# Длина 6, подстроки длиной 5 не могут одновременно существовать без пересечения
		# Но можем сделать одну из них с изменениями
		result = task_2(s)
		# Минимум: либо сделать tbank (заменить последние 2 символа) = 2
		# Либо сделать study (заменить все) = 5
		# Итого: 2
		self.assertEqual(result, 2)

	def test_minimal_length(self):
		'''Тест минимальной длины строки (10 символов)'''
		s = 'tbankstudy'  # Ровно 10 символов, уже хорошая
		result = task_2(s)
		self.assertEqual(result, 0)

		s = 'xxxxxxxxxx'  # Все неправильные
		result = task_2(s)
		# Можно сделать tbankstudy с 10 заменами
		# Или studytbank с 10 заменами
		# Или с пересечением: tbanstudy (10 заменами)
		self.assertEqual(result, 10)

	def test_with_overlap_possible(self):
		'''Тест, когда можно использовать пересечение для экономии'''
		s = 'tbanestudy'
		# 'tbanestudy': 
		# - сделать tbank на позиции 0: заменить 'e' на 'k' = 1
		# - сделать study на позиции 5: уже есть = 0
		# Итого: 1
		result = task_2(s)
		self.assertEqual(result, 1)

	def test_complex_case(self):
		'''Сложный тест'''
		s = 'studytbankextrastudy'
		# Уже есть обе подстроки
		result = task_2(s)
		self.assertEqual(result, 0)

	def test_only_tbank(self):
		'''Тест, когда есть только tbank'''
		s = 'tbankxxxxx'
		result = task_2(s)
		# Нужно добавить study: минимально 5 замен
		self.assertEqual(result, 5)

	def test_only_study(self):
		'''Тест, когда есть только study'''
		s = 'studyyyyyy'
		result = task_2(s)
		# Нужно добавить tbank: минимально 5 замен
		self.assertEqual(result, 5)

	def test_large_random(self):
		'''Тест с большой строкой (проверка производительности)'''
		import random
		random.seed(42)
		s = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') 
				   for _ in range(10000))
		# Просто проверяем, что функция работает без ошибок
		result = task_2(s)
		self.assertIsInstance(result, int)
		self.assertTrue(0 <= result <= 10000)

	def test_edge_cases(self):
		'''Граничные случаи'''
		# Строка состоит из повторяющихся паттернов
		s = 'tbank' * 2 + 'study' * 2
		result = task_2(s)
		self.assertEqual(result, 0)

		# Почти хорошая строка
		s = 'tbanksstudy'  # Лишняя 's' между
		result = task_2(s)
		# Можно сделать tbank на позиции 0 и study на позиции 6
		self.assertEqual(result, 1)

def run_tests():
	'''Запуск всех тестов'''
	loader = unittest.TestLoader()
	suite = loader.loadTestsFromTestCase(TestTask2)
	runner = unittest.TextTestRunner(verbosity=2)
	result = runner.run(suite)
	return result


if __name__ == '__main__':
	run_tests()
