'''
Этот использовал для tbank.
DeekSeek (task_2) - он запутанный и не понятный, а тут коротко.
'''

def solve():
    s = input().strip()
    n = len(s)
    t1 = "tbank"
    t2 = "study"
    m = 5 # длина обеих строк
    
    def get_cost(sub, target):
        return sum(1 for i in range(m) if sub[i] != target[i])

    # Считаем стоимость замены для каждой возможной позиции
    cost_t1 = [get_cost(s[i:i+m], t1) for i in range(n - m + 1)]
    cost_t2 = [get_cost(s[i:i+m], t2) for i in range(n - m + 1)]
    
    # pref_t1[i] - мин. стоимость t1 на отрезке [0, i+m-1]
    pref_t1 = [10] * len(cost_t1)
    pref_t2 = [10] * len(cost_t2)
    
    curr_min1 = 10
    curr_min2 = 10
    for i in range(len(cost_t1)):
        curr_min1 = min(curr_min1, cost_t1[i])
        curr_min2 = min(curr_min2, cost_t2[i])
        pref_t1[i] = curr_min1
        pref_t2[i] = curr_min2

    ans = 10 # Максимально возможный ответ (5+5)
    
    # Ищем оптимальную пару (одна левее, другая правее)
    # i - начало правой строки, она должна начинаться как минимум через m символов после левой
    for i in range(m, n - m + 1):
        # Случай 1: t1 слева, t2 справа
        ans = min(ans, pref_t1[i - m] + cost_t2[i])
        # Случай 2: t2 слева, t1 справа
        ans = min(ans, pref_t2[i - m] + cost_t1[i])
        
    print(ans)

solve()
