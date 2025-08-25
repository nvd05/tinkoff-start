## Задание 1

Укажите все возможные последовательности чисел, которые могут быть выведены на экран в результате выполнения следующего участка кода:

```csharp
public static void Main()
{
	for (int i = 0; i < 4; i++)
	{
		Random ran = new Random();
		int newInt = ran.Next(-20, 20);
		Console.Write(newInt + ", ");
	}
}
```

+ [ ] 3,-3,8,-21
+ [x] 1,-1,-10,-2
+ [x] 17,14,20,-1
+ [x] 4,4,4,4
+ [x] 20,20,20,20

## Задание 2

Что будет выведено на консоль?

```csharp
static int Foo(int n)
{
	if (n == 0)
	{
		return 0;
	}
	return Foo(n - 1);
}
static int Bar(int n)
{
	if (n == 0)
	{
		return 1;
	}
	else return n * n + Foo(n);
}
public static void Main()
{
	Console.WriteLine(Bar(9));
}
```

+ [ ] 0
+ [ ] 25
+ [x] 81
+ [ ] 82
+ [ ] 83

## Задание 3

Какой метод будет вызван при выполнении следующего кода?

```csharp
static double F(int a, int b) { return a + b; }       // 1
static double F(double a, double b) { return a + b; } // 2
static double F(short a, double b) { return a + b; }  // 3
static double F(short a, int b) { return a + b; }     // 4

public static void Main()
{
	int a = 2;
	Console.Write(F(a, 3.5));
}
```

+ [ ] 1
+ [x] 2
+ [ ] 3
+ [ ] 4
+ [ ] Ошибка компиляции

## Задание 4

В языке C# в статическом методе запрещено обращение к членам класса:

+ [x] НЕ имеющим модификатора static
+ [ ] имеющим модификатор static
+ [x] с использованием ключевого слова this
+ [ ] с модификатором public
+ [ ] с модификатором private

## Задание 5

Что будет выведено на консоль?

```csharp
class Task
{
	int [] a = { 1, 0 , 1, -1, 1, 0};
	public int this[int x, int y]
	{
		get { return this.a[x + y]; }
		set { this.a[x] = this.a[y] = value % 2; }
	}
}
public static void Main() {
	Task program = new Task();
	program[2,1] = 18;
	Console.Write(program[3,0]);
}
```

+ [ ] 1
+ [ ] 0
+ [x] -1
+ [ ] 2
+ [ ] Ошибка компиляции

## Задание 6

Что будет выведено на консоль?

```csharp
public abstract class A
{
	public abstract string Sign(int x)
	{
		if (x > 0)
		{
			return x.ToString();
		}
		else if (x == 0)
		{
			return "0";
		}
		return Math.Abs(x).ToString();
	}
}
public class B : A
{
	public override string Sign(int x)
	{
		if (x > 0)
		{
			return "1";
		}
		else if (x == 0)
		{
			return "0";
		}
		return "-1";
	}
}

public static void Main()
{
	A b = new B();
	Console.Write(b.Sign(-137));
}
```

+ [ ] -137
+ [ ] 137
+ [ ] 0
+ [ ] 1
+ [ ] -1
+ [x] Ошибка компиляции

## Задание 7

Выберите все строки кода, вставка которых вместо пропуска (---) в программу позволит произвести успешную компиляцию:

```csharp
class A {
	public int lord;
}
class B : A {
	public static double lord = 55.5;
}
public static void Main() {
	A obj = new B();
	B obj2 = new B();
	B.lord = 55;
	Console.WriteLine(---);
}
```

+ [x] obj.lord
+ [x] obj2.lord
+ [ ] A.lord
+ [x] B.lord
+ [x] (new B()).lord

## Задание 8

Что будет выведено на консоль?

```csharp
public static void Main()
{
	var numbers = new List<int>
	{
		1, 2, 3
	};
	var query = numbers.Where(n => n % 2 == 1);
	numbers.Add(5);
	Console.WriteLine(query.Count());
}
```

+ [ ] 2
+ [x] 3
+ [ ] 4
+ [ ] 5
+ [ ] Ошибка выполнения

## Задание 9

Что будет выведено на консоль?

```csharp
class A
{
	public virtual string Foo() => "A";
}
class B : A
{
	public new string Foo() => "B";
}
class A2
{
	public virtual string Bar() => "A";
}
class B2 : A2
{
	public override string Bar() => "B";
}
public static void Main()
{
	A objA = new A();
	A objB = new B();
	B objC = new B();
	Console.WriteLine($"{objA.Foo()} {objB.Foo()} {objC.Foo()}");

	A2 objA2 = new A2();
	A2 objB2 = new B2();
	B2 objC2 = new B2();
	Console.WriteLine($"{objA2.Bar()} {objB2.Bar()} {objC2.Bar()}");
}
```

+ [x] A A B A B B
+ [ ] A A B A B A
+ [ ] A A B B B B
+ [ ] A A B B B A
+ [ ] A A B A A B

## Задание 10

Что будет выведено на консоль?

```csharp
public static void Main()
{
	void Inc(ref object o)
	{
		o = (int)o + 1;
	}
	int x = 1;
	object box = x;
	Inc(ref box);
	Console.WriteLine($"{x} {box}");
}
```

+ [ ] 1 2
+ [x] 1 2
+ [ ] 2 2
+ [ ] 1 1
+ [ ] Ошибка компиляции

## Задание 11

Что будет выведено на консоль?

```csharp
public static void Main()
{
	var a = "a" + "b";
	var b = "ab";

	Console.WriteLine($"{a.Equals(b)} {object.ReferenceEquals(a, b)} {a == b}");
}
```

+ [x] True True True
+ [ ] True False True
+ [ ] True True False
+ [ ] False False False

## Задание 12

Что произойдет при вызове метода Change?

```csharp
class A
{
	public int V;
}
class B
{
	public readonly A Obj = new A();
	public void Change() => Obj.V = 42;
}
```

+ [ ] Ошибка компиляции
+ [ ] Ошибка выполнения
+ [x] Obj.V = 42;

## Задание 13

Что будет выведено на консоль?

```csharp
struct S
{
	public int N;
}
static void Mutate(S s)
{
	s.N++;
}
public static void Main()
{
	S val = new S
	{
		N = 5
	};
	Mutate(val);
	Console.WriteLine(val.N);
}
```

+ [x] 5
+ [ ] 6
+ [ ] Ошибка компиляции
+ [ ] Ошибка выполнения

## Задание 14

Что будет выведено на консоль?

```csharp
public static void Main() {
	object o = "text";
	var r1 = o is string;
	var r2 = o is string s && s.Length > 3;
	Console.WriteLine(r1 && r2);
}
```

+ [x] True
+ [ ] False
+ [ ] Ошибка компиляции
+ [ ] Ошибка выполнения

## Задание 15

Что будет выведено на консоль?

```csharp
[Flags]
enum UserRoles
{
	None = 0,
	Guest = 1,
	User = 2,
	Moderator = 4,
	Admin = 8
}
static void Main()
{
	UserRoles roles = UserRoles.User | UserRoles.Moderator;

	bool isAdmin = (roles & UserRoles.Admin) == UserRoles.Admin;
	bool isModerator = (roles & UserRoles.Moderator) == UserRoles.Moderator;
	bool isGuestOrUser = (roles & (UserRoles.Guest | UserRoles.User)) != 0;

	Console.WriteLine($"{isAdmin} {isModerator} {isGuestOrUser}");
}
```

+ [ ] True True False
+ [ ] True False True
+ [x] False True True
+ [ ] False False True
+ [ ] True True True

## Задание 16

Что произойдет при выполнении следующего кода?

```csharp
class PointClass(int x, int y)
{
	public int X = x;
	public int Y = y;
}
struct PointStruct(int x, int y)
{
	public int X = x;
	public int Y = y;
}
public static void Main()
{
	var dictC = new Dictionary<PointClass, int>();
	var dictS = new Dictionary<PointStruct, int>();

	var pointC = new PointClass(10, 20);
	dictC[pointC] = 42;
	pointC.X = 15;
	Console.WriteLine(dictC[pointC]);

	var pointS = new PointStruct(10, 20);
	dictS[pointS] = 43;
	pointS.X = 15;
	Console.WriteLine(dictS[pointS]);
}
```

+ [ ] Вывод: 42, 43
+ [x] Вывод: Exception, 43
+ [ ] Вывод: 42, Exception
+ [ ] Вывод: Exception, Exception

## Задание 17

Что будет выведено на консоль?

```csharp
class AsStatic
{
	static AStatic()
	{
		Console.WriteLine("Static A");
	}
	public AStatic()
	{
		Console.WriteLine("Instance A");
	}
}
class BStatic : AStatic
{
	static BStatic()
	{
		Console.WriteLine("Static B");
	}
	public BStatic()
	{
		Console.WriteLine("Instance B");
	}
}
public static void Main()
{
	var b = new BStatic();
}
```

+ [x] Static A Static B Instance A Instance B
+ [ ] Static B Static A Instance A Instance B
+ [ ] Instance A Instance B Static A Static B
+ [ ] Instance B Instance A Static A Static B

## Задание 18

Что будет выведено на консоль?

```csharp
public static void Main()
{
	var key = "Hello from ";
	int[] arr = new int[2];

	try
	{
		arr[2] = 3;
	}
	catch (IndexOutOfRangeException)
	{
		key += "IndexOutOfRangeException catch, ";
	}
	catch (Exception)
	{
		key += "Exception catch, ";
	}
	finally
	{
		key += "Finally, ";
	}

	Console.WriteLine(key);
}
```

+ [ ] Hello from Finally, IndexOutOfRangeException catch
+ [ ] Hello from Exception catch, Finally
+ [x] Hello from IndexOutOfRangeException catch, Finally
+ [ ] Hello from Finally, Exception catch

## Задание 19

Что будет выведено на консоль?

```csharp
public static void Main() {
	bool c = true;
	int n;
	int? m = null;

	n = c ? 1 : 2;
	m ??= 3;

	Console.WriteLine($"{n} {m}");
}
```

+ [ ] 2 3
+ [ ] 1 2
+ [x] 1 3
+ [ ] 2 2

## Задание 20

Что будет выведено на консоль?

```csharp
public static void Main()
{
	var actions = new List<Action>();
	for (var i = 0; i < 3; i++)
	{
		actions.Add(() => Console.Write(i));
	}

	actions[1]();
}
```

+ [ ] 0
+ [ ] 1
+ [x] 3
+ [ ] 2
+ [ ] Ошибка компиляции
