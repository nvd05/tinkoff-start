
# 4 задание | 100 баллов

+ Ограничение времени: `1 секунда`
+ Ограничение памяти: `128 МБ`

Напишите запрос, который определит курс с наибольшим числом повторных студентов.
Повторный студент — это студент, у которого по данному курсу есть как минимум 2 завершённых обучения.

При равенстве числа повторных студентов:

+ выбирайте курс с большим количеством завершённых обучений;
+ при новом равенстве — курс с названием, идущим раньше по алфавиту.

[Описание таблиц.docx](Описание%20таблиц.docx.md)

```sql
WITH completed_enrollments AS (
    -- Выбираем все завершённые обучения
    SELECT 
        student_id, 
        course
    FROM 
        enrollments
    WHERE 
        status = 'completed'
),
student_course_repeats AS (
    -- Находим пары (курс, студент), где у студента >= 2 завершённых обучения по этому курсу
    SELECT 
        course, 
        student_id
    FROM 
        completed_enrollments
    GROUP BY 
        course, 
        student_id
    HAVING 
        COUNT(*) >= 2
),
repeat_student_counts AS (
    -- Считаем количество повторных студентов для каждого курса
    SELECT 
        course, 
        COUNT(*) AS repeat_students
    FROM 
        student_course_repeats
    GROUP BY 
        course
),
total_completed_counts AS (
    -- Считаем общее количество завершённых обучений для каждого курса
    SELECT 
        course, 
        COUNT(*) AS total_completed
    FROM 
        completed_enrollments
    GROUP BY 
        course
)
SELECT 
    t.course
FROM 
    total_completed_counts t
LEFT JOIN 
    repeat_student_counts r ON t.course = r.course
ORDER BY 
    COALESCE(r.repeat_students, 0) DESC,  -- Сначала по убыванию числа повторных студентов
    t.total_completed DESC,               -- Затем по убыванию числа завершённых обучений
    t.course ASC                          -- Затем по алфавиту названия курса
LIMIT 1;
```
