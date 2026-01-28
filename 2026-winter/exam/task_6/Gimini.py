'''
Верно первый тест проходит.
Есть шанс, что другие тоже.
'''


def solve():
    # Читаем n и q
    input_data = input().split()

    n = int(input_data[0])
    q = int(input_data[1])
    s_orig = input()

    # Стек для хранения операций вставки: (левая_граница_вставки, длина_вставленного, l_исходное, r_исходное)
    history = []

    results = []

    for _ in range(q):
        line = input().strip().split()
        type = int(line[0])
        if type == 1:
            l = int(line[1])
            r = int(line[2])
            history.append((l, r))
            # Длина подстроки, которую удваиваем
            # sub_len = r - l + 1
            # Операция: после r-го символа вставляется еще раз эта же подстрока
            # В задаче: "удваиваете ее и возвращаете... вместо изначальной" 
            # Это значит s = s[:r] + s[l-1:r] + s[r:]
            # history.append((r, sub_len, l, r))
            # current_len += sub_len

        else:
            pos = int(line[1])
            curr_pos = pos
            # Идем по истории назад, чтобы найти исходный индекс
            for h_l, h_r in reversed(history):
                sub_len = h_r - h_l + 1
                new_r = h_r + sub_len # Конец зоны после удвоения
                
                if curr_pos > new_r:
                    # Символ был за пределами удвоения, просто сдвигаем индекс назад
                    curr_pos -= sub_len
                elif curr_pos >= h_l:
                    # Символ попал в зону удвоения s_l s_l s_{l+1} s_{l+1}...
                    # Вычисляем, какому из оригинальных символов он соответствует
                    curr_pos = h_l + (curr_pos - h_l) // 2
                # Если curr_pos < h_l, ничего не делаем
            
            results.append(s_orig[curr_pos - 1])
            
    print('\n'.join(results) + '\n')

solve()
