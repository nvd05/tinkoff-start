using System;
using System.Collections.Generic;

class Program
{
	static void Main()
	{
		int n = int.Parse(Console.ReadLine());
		List<(long x, long y)> points = new List<(long x, long y)>();
		for (int i = 0; i < n; i++)
		{
			string[] input = Console.ReadLine().Split();
			long x = long.Parse(input[0]);
			long y = long.Parse(input[1]);
			points.Add((x, y));
		}

		int maxTriples = 0;
		bool[] used = new bool[n]; // Массив для отметки использованных точек

		for (int i = 0; i < n; i++)
		{
			if (used[i]) continue; // Если точка уже использована, пропускаем её

			for (int j = i + 1; j < n; j++)
			{
				if (used[j]) continue; // Если точка уже использована, пропускаем её

				for (int k = j + 1; k < n; k++)
				{
					if (used[k]) continue; // Если точка уже использована, пропускаем её

					if (!AreCollinear(points[i], points[j], points[k]))
					{
						// Если тройка не коллинеарна, отмечаем точки как использованные
						used[i] = true;
						used[j] = true;
						used[k] = true;
						maxTriples++;
						break; // Переходим к следующей тройке
					}
				}

				if (used[i]) break; // Если точка i уже использована, переходим к следующей i
			}
		}

		Console.WriteLine(maxTriples);
	}

	static bool AreCollinear((long x, long y) p1, (long x, long y) p2, (long x, long y) p3)
	{
		return (p2.y - p1.y) * (p3.x - p1.x) == (p3.y - p1.y) * (p2.x - p1.x);
	}
}
