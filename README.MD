

Бот позволяет получать данные о курсах валют и погоде.

Запуск бота вынесен в отдельный файл - теперь логика лежит отдельно, а управление отдельно.
Добавлена обработка Exceptions

Команды:

```bash
/start 
/country rb или uk 
/курс <аббревиатура валюты> 
например
/курс usd
/weather <city>
например
/weather Lviv

```

### Подготовка и запуск
pip install requests

```bash
python telegram_bot.py

```
или

```bash
python3 telegram_bot.py
```
