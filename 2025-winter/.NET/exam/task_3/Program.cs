using System;
using System.Linq;

class Program
{
	static void Main()
	{
		// Чтение входных данных
		string[] firstLine = Console.ReadLine().Split();
		int n = int.Parse(firstLine[0]); // Количество дней
		int m = int.Parse(firstLine[1]); // Необходимое количество хороших дней

		int[] a = Console.ReadLine()
			.Split()
			.Select(int.Parse)
			.ToArray(); // Массив километров для каждого дня

		// Вычисление минимального количества корректировок
		long result = MinimalAdjustments(n, m, a);

		// Вывод результата
		Console.WriteLine(result);
	}

	static long MinimalAdjustments(int n, int m, int[] a)
	{
		int a1 = a[0]; // Количество километров в первый день
		int a2 = a[1]; // Количество километров во второй день

		// Массив для хранения корректировок
		long[] adjustments = new long[n - 2];

		// Вычисление корректировок для каждого дня, начиная с третьего
		for (int i = 2; i < n; i++)
		{
			int ai = a[i];
			if (ai < a1)
			{
				adjustments[i - 2] = a1 - ai; // Увеличить до a1
			}
			else if (ai > a2)
			{
				adjustments[i - 2] = ai - a2; // Уменьшить до a2
			}
			else
			{
				adjustments[i - 2] = 0; // Корректировка не нужна
			}
		}

		// Сортировка корректировок по возрастанию
		Array.Sort(adjustments);

		// Сумма первых m корректировок
		long sum = 0;
		for (int i = 0; i < m; i++)
		{
			sum += adjustments[i];
		}

		return sum;
	}
}
