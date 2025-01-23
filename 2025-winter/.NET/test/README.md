
# 1 задание

Что будет выведено в консоль?

```csharp
string first = "ab";
string second = "a" + "b";

Console.WriteLine(first == second);
Console.WriteLine((object)first == (object)second);
```

+ True, False
+ True, True (+)
+ False, False
+ False, True

# 2 задание

Какой результат выполнения кода?

```csharp
Dictionary<Key, string> dictionary = new Dictionary<Key, string>();
Key firstKey = new Key(1);
dictionary.Add(firstKey, "First");
Key secondKey = new Key(2);
dictionary.Add(secondKey, "Second");

Console.WriteLine(dictionary[firstKey]);

public class Key
{
	public int Marker { get; }
	public Key(int marker) => Marker = marker;
	public override int GetHashCode() => Marker / 10;
	public override bool Equals(object? other) =>
		other is Key ? other.GetHashCode() == GetHashCode() : base.Equals(other);
}
```

+ В консоль выведено: First
+ В консоль выведено: Second
+ Исключение ArgumentException (+)

# 3 задание

Какое значение переменной `key` в результате выполнения кода?

```csharp
string key = "a";

try
{
	throw new ArgumentException();
}
catch (ArgumentException)
{
	key += "b";
}
catch (Exception)
{
	key += "c";
}
finally
{
	key += "d";
}
```

+ "ab"
+ "ad"
+ "abd" (+)
+ "abcd"

# 4 задание

Какой результат выполнения кода?

```csharp
try
{
	using (Robot robot = new Robot())
	{
		robot.Dispose();
		throw new InvalidOperationException();
	}
}
catch (InvalidOperationException)
{
	Console.WriteLine("Exception handled");
}

public class Robot : IDisposable
{
	public Robot() => Console.WriteLine("Constructed");
	public void Dispose() => Console.WriteLine("Disposed");
}
```

+ В консоль выведены: Constructed, Disposed, Disposed, Exception handled (+)
+ В консоль выведены: Constructed, Disposed, Exception handled
+ В консоль выведены: Constructed, Disposed
+ Исключение ArgumentNullException

# 5 задание

Какой результат выполнения кода?

```csharp
int first = 0;
object second = (object)first;
Increment(ref first);
Console.WriteLine(first == (int)second);

public static void Increment(ref int source)
{
	source++;
}
```

+ В консоль выведено: True
+ В консоль выведено: False (+)

# 6 задание

Что будет выведено в консоль?

```csharp
Ultrabot ultrabot = new Ultrabot();
Robot robot = new Robot();

public class Robot
{
	static Robot() { Console.WriteLine("Static"); }
	public Robot() { Console.WriteLine("Robot"); }
}

public class Ultrabot : Robot
{
	public Ultrabot() : base() { Console.WriteLine("Ultrabot"); }
}
```

+ Static, Robot, Ultrabot, Robot (+)
+ Robot, Ultrabot, Robot
+ Static, Robot, Ultrabot, Static, Robot
+ Static, Ultrabot, Robot

# 7 задание

Что будет выведено в консоль?

```csharp
Fuzzbot bot = new Fuzzbot();		
Console.WriteLine(bot is Robot);
Console.WriteLine(bot is Fuzzbot);
Console.WriteLine(bot is Buzzbot);

public class Robot {}
public class Fuzzbot : Robot {}
public class Buzzbot : Robot {}
```

+ False, True, False
+ True, True, False (+)
+ True, True, True

# 8 задание

Какой результат выполнения кода?

```csharp
Human human = new Human();
Robot robot = new Robot(human);
robot.HumanOperator.Name = "Masha";
Console.WriteLine(robot.HumanOperator.Name);

public class Robot
{
	public readonly Human HumanOperator;
	public Robot(Human humanOperator) => HumanOperator = humanOperator;
}

public class Human
{
	public string Name;
}
```

+ В консоль выведено: Masha (+)
+ Исключение InvalidOperationException
+ Ошибка во время компиляции кода

# 9 задание

Что будет выведено в консоль?

```csharp
Robot robot = new Robot();
robot.Print();
(robot as Robot).Print();
(robot as BaseRobot).Print();

public abstract class BaseRobot
{
	public virtual void Print() => Console.WriteLine("BaseRobot");
}

public class Robot : BaseRobot
{
	public override void Print() => Console.WriteLine("Robot");
}
```

+ Robot, Robot, Robot (+)
+ Robot, Robot, BaseRobot
+ BaseRobot, Robot, BaseRobot

# 10 задание

Что будет выведено в консоль?

```csharp
Robot robot = new Robot();
robot.Print();
(robot as Robot).Print();		
(robot as BaseRobot).Print();

public abstract class BaseRobot
{
	public void Print() => Console.WriteLine("BaseRobot");
}

public class Robot : BaseRobot
{
	public new void Print() => Console.WriteLine("Robot");
}
```

+ Robot, Robot, Robot
+ Robot, Robot, BaseRobot (+)
+ Robot, BaseRobot, BaseRobot

# 11 задание

Какой результат выполнения кода?

```csharp
Queue<string> queue = new Queue<string>();
queue.Enqueue("1");
queue.Enqueue("2");
queue.Dequeue();
queue.Enqueue("3");

foreach(string item in (IEnumerable<string>)queue)
{
	Console.WriteLine(item);
}
```

+ В консоль выведено: 1, 3
+ В консоль выведено: 2, 3 (+)
+ Исключение InvalidCastException

# 12 задание

Что будет выведено в консоль?

```csharp
Container container = new Container() { Value = 1 };
Container.Nullify(container);
Console.WriteLine(container.Value);

public struct Container
{
	public int Value;
	public static void Nullify(Container container) => container.Value = 0;
}
```

+ 0
+ 1 (+)

# 13 задание

Что будет выведено в консоль?

```csharp
List<int> numbers = new List<int> { 1, 2, 3, 4 };
IEnumerable<int> squares = numbers
	.Where(x => x % 2 == 0)
	.Select(x => x * 2);

foreach(var square in squares)
{
	Console.WriteLine(square);
}
```

+ 1, 4, 9, 16
+ 4, 8 (+)
+ 4, 16
+ 1, 4, 3, 8
