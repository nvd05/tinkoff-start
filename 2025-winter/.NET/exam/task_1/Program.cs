using System;

class Program
{
	static void Main()
	{
		// Считываем строку
		string s = Console.ReadLine().Trim();

		// Находим индексы символов R и M
		int indexR = s.IndexOf('R');
		int indexM = s.IndexOf('M');

		// Проверяем, находится ли R раньше M
		if (indexR < indexM)
		{
			Console.WriteLine("Yes");
		}
		else
		{
			Console.WriteLine("No");
		}
	}
}
