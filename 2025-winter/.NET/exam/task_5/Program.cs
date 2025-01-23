using System;
using System.Linq;

class Program
{
	static void Main()
	{
		string[] input = Console.ReadLine().Split();
		int n = int.Parse(input[0]);
		long s = long.Parse(input[1]);
		long[] a = Console.ReadLine().Split().Select(long.Parse).ToArray();

		// Вычисляем префиксные суммы
		long[] prefixSum = new long[n + 1];
		for (int i = 1; i <= n; i++)
		{
			prefixSum[i] = prefixSum[i - 1] + a[i - 1];
		}

		long total = 0;

		// Перебираем все возможные подотрезки
		for (int l = 1; l <= n; l++)
		{
			for (int r = l; r <= n; r++)
			{
				long sum = prefixSum[r] - prefixSum[l - 1];
				if (sum <= s)
				{
					total += 1;
				}
				else
				{
					total += CalculateCuts(l, r, prefixSum, s);
				}
			}
		}

		Console.WriteLine(total);
	}

	static long CalculateCuts(int l, int r, long[] prefixSum, long s)
	{
		long sum = prefixSum[r] - prefixSum[l - 1];
		if (sum <= s)
		{
			return 1;
		}

		long cuts = 0;
		long currentSum = 0;
		for (int i = l; i <= r; i++)
		{
			currentSum += prefixSum[i] - prefixSum[i - 1];
			if (currentSum > s)
			{
				cuts++;
				currentSum = prefixSum[i] - prefixSum[i - 1];
			}
		}

		return cuts + 1;
	}
}
