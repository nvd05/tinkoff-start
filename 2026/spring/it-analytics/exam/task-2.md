
# 2 задание | 100 баллов

+ Ограничение времени: `1 секунда`
+ Ограничение памяти: `128 МБ`

Напишите запрос, который определит город с наибольшей суммарной "нагрузкой" по завершённым обучениям.
Eсли таких городов несколько, выберите тот, чьё название идёт первым по алфавиту.
"Нагрузка" — это сумма progress_pct по завершённым обучениям студентов данного города.

[Описание таблиц.docx](Описание%20таблиц.docx.md)

```sql
SELECT s.city
FROM students s
JOIN enrollments e ON s.student_id = e.student_id
WHERE e.status = 'completed'
GROUP BY s.city
ORDER BY SUM(e.progress_pct) DESC, s.city ASC
LIMIT 1;
```
