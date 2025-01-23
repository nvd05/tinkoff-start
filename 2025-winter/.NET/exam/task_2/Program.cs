using System;
using System.Collections.Generic;

class Program
{
	static void Main()
	{
		int n = int.Parse(Console.ReadLine());
		long[] a = new long[n];
		for (int i = 0; i < n; i++)
		{
			a[i] = long.Parse(Console.ReadLine());
		}

		for (int i = 0; i < n; i++)
		{
			long maxSum = GetMaxBouquetCost(a[i]);
			Console.WriteLine(maxSum);
		}
	}

	static long GetMaxBouquetCost(long a)
	{
		if (a < 7) // Минимальная сумма для трех цветков: 2^0 + 2^1 + 2^2 = 1 + 2 + 4 = 7
		{
			return -1;
		}

		long k = (long)Math.Log(a, 2);
		long sum = (1L << (int)k) + (1L << (int)(k - 1)) + (1L << (int)(k - 2));

		if (sum <= a)
		{
			return sum;
		}

		// Если сумма больше a, ищем комбинацию из трех цветков
		long maxSum = 0;
		for (long i = k; i >= 0; i--)
		{
			for (long j = i - 1; j >= 0; j--)
			{
				for (long l = j - 1; l >= 0; l--)
				{
					long currentSum = (1L << (int)i) + (1L << (int)j) + (1L << (int)l);
					if (currentSum <= a && currentSum > maxSum)
					{
						maxSum = currentSum;
					}
				}
			}
		}

		return maxSum > 0 ? maxSum : -1;
	}
}
