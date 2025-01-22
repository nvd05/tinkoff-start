// See https://aka.ms/new-console-template for more information

using System;
using System.Runtime;

namespace TestTasks
{
	public static class Program
	{
		private static int Task1(string data)
		{
			var args = data.Split(' ');

			var a = Convert.ToInt32(args[0]); // Абонентская плата
			var b = Convert.ToInt32(args[1]); // мегабайт интернет-трафика
			var c = Convert.ToInt32(args[2]); // каждый следующий мегабайт
			var d = Convert.ToInt32(args[3]); // планирует потратить мегабайт интернет-трафика

			var additional = d - b;

			return additional > 0
				? a + (additional * c)
				: a;
		}

		public static void Main()
		{
			// Console.WriteLine(Task1("100 10 12 15")); // 160
			// Console.WriteLine(Task1("100 10 12 1")); // 100
			Console.WriteLine(Task1(Console.ReadLine()));
		}
	}
}
