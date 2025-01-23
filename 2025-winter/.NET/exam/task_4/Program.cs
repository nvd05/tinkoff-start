using System;
using System.Linq;

class Program
{
	static void Main()
	{
		// Чтение входных данных
		var input = Console.ReadLine().Split();
		int n = int.Parse(input[0]);
		int x = int.Parse(input[1]);
		int y = int.Parse(input[2]);
		int z = int.Parse(input[3]);

		var a = Console.ReadLine().Split().Select(long.Parse).ToArray();

		// Вычисление минимального количества операций
		long minOps = long.MaxValue;

		// Перебираем все возможные комбинации элементов для выполнения условий
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				for (int k = 0; k < n; k++)
				{
					// Вычисляем количество операций для каждого элемента
					long opsX = (x - a[i] % x) % x;
					long opsY = (y - a[j] % y) % y;
					long opsZ = (z - a[k] % z) % z;

					// Суммируем операции, если элементы разные
					long totalOps = opsX + opsY + opsZ;

					// Если элементы совпадают, учитываем это
					if (i == j) totalOps -= Math.Min(opsX, opsY);
					if (i == k) totalOps -= Math.Min(opsX, opsZ);
					if (j == k) totalOps -= Math.Min(opsY, opsZ);

					// Обновляем минимальное количество операций
					minOps = Math.Min(minOps, totalOps);
				}
			}
		}

		// Вывод результата
		Console.WriteLine(minOps);
	}
}
