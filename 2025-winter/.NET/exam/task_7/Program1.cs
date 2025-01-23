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
 * 26 <= ans 110
 * 684
 */
class Program1
{
    const int MOD = 998244353;

    static void Main1()
    {
        // Чтение входных данных
        var input = Console.ReadLine().Split();
        int n = int.Parse(input[0]);
        int k = int.Parse(input[1]);
        var a = Console.ReadLine().Split().Select(long.Parse).ToArray();

        // Вычисление суммы всех элементов и суммы квадратов
        long sumA = a.Sum();
        long sumA2 = a.Sum(x => x * x);

        // Вычисление f(p) для каждого p от 1 до k
        for (int p = 1; p <= k; p++)
        {
            // Сумма всех (a_i + a_j)^p для i < j
            // Используем формулу: sum_{i<j} (a_i + a_j)^p = (sumA^p - sumA2^(p/2)) / 2
            // Но для p=1 и p=2 это работает, для p>2 нужно использовать биномиальное разложение
            // Для упрощения, будем использовать прямое вычисление для p=1 и p=2, а для p>2 - биномиальное разложение

            if (p == 1)
            {
                // Для p=1: sum_{i<j} (a_i + a_j) = (sumA * (n-1)) / 2
                long f = (sumA * (n - 1)) % MOD;
                Console.WriteLine(f);
            }
            else if (p == 2)
            {
                // Для p=2: sum_{i<j} (a_i + a_j)^2 = (sumA^2 - sumA2) / 2
                long f = ((sumA * sumA - sumA2) / 2) % MOD;
                Console.WriteLine(f);
            }
            else
            {
                // Для p>2 используем биномиальное разложение
                long f = 0;
                for (int i = 0; i < n; i++)
                {
                    for (int j = i + 1; j < n; j++)
                    {
                        long sum = (a[i] + a[j]) % MOD;
                        f = (f + Pow(sum, p)) % MOD;
                    }
                }
                Console.WriteLine(f);
            }
        }
    }

    // Функция для быстрого возведения в степень по модулю
    static long Pow(long x, int p)
    {
        long result = 1;
        while (p > 0)
        {
            if ((p & 1) == 1)
                result = (result * x) % MOD;
            x = (x * x) % MOD;
            p >>= 1;
        }
        return result;
    }
}
