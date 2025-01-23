using System;
using System.Linq;

/*
 * deepseek AI
 *
 * input:
 * 3 3
 * 2 3 4
 *
 * result:
 * 18
 * 110
 * 684
 */
class Program
{
	const int MOD = 998244353;

	static void Main()
	{
		string[] input = Console.ReadLine().Split();
		int n = int.Parse(input[0]);
		int k = int.Parse(input[1]);

		long[] a = Console.ReadLine().Split().Select(long.Parse).ToArray();

		// Предварительно вычисляем суммы степеней
		long[] sumPowers = new long[k + 1];
		for (int p = 1; p <= k; p++)
		{
			long sum = 0;
			for (int i = 0; i < n; i++)
			{
				for (int j = i + 1; j < n; j++)
				{
					long sumPair = (a[i] + a[j]) % MOD;
					long powered = Pow(sumPair, p, MOD);
					sum = (sum + powered) % MOD;
				}
			}
			sumPowers[p] = sum;
		}

		// Выводим результаты
		for (int p = 1; p <= k; p++)
		{
			Console.WriteLine(sumPowers[p]);
		}
	}

	static long Pow(long x, int p, int mod)
	{
		long result = 1;
		while (p > 0)
		{
			if (p % 2 == 1)
			{
				result = (result * x) % mod;
			}
			x = (x * x) % mod;
			p /= 2;
		}
		return result;
	}
}
