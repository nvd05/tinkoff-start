
# tinkoff start

> Попытки решить задачи вступительного экзамена на стажировку Тинькофф Старт.

+ это попытки решить задачи собственными силами.
+ сборник ссылок на другие репозитории решений.
+ предпочитаемый язык: Python 3.8

## Скопировать текст задания

+ Автоматический скрипт|расширение: `Tampermonkey.js`.
+ Ручное копирование содержимого:

```javascript
let buffer = document.createElement('textarea');
buffer.value = $0.innerText;

document.body.appendChild(buffer);
buffer.select();

console.log(document.execCommand('copy') ? 'COPIED' : 'FAILED TO SEND TO CLIPBOARD');

document.body.removeChild(buffer);
delete buffer;
```
