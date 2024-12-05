# Django-Telegram-auth
Django проект с авторизацией через Telegram-бота



# Требования к реализации:
- [x] Создать веб-страницу с кнопкой "Войти через Telegram"  
- [x] При нажатии на кнопку происходит перенаправление в Telegram-бота, где ссылка содержит команду /start с уникальным токеном  
- [x] После отправки команды пользователем Django получает токен и связывает Telegram-аккаунт с пользователем веб-сайта  
- [x] Веб-страница автоматически обновляется, отображая имя или никнейм пользователя из Telegram. Пользователь авторизуется через стандартные механизмы Django.  

# Реализация
- Django проект с приложением app
- Расширенная модель User: дополнена полями tlg_name, tlg_id 
- 2 views (index и user)
- template index.html с блоком if в зависимости от полученного на входе user
- telegram-bot в DTAproject\app\management\commands\runbot.py

# Переменные окружения
- SECRET_KEY
- BOT_NAME
- BOT_TOKEN
- DOMAIN

# Установка
```bash
$ git clone https://github.com/belyashnikovatn/Django-Telegram-auth.git
$ python -m venv venv  
$ source venv/Scripts/activate  
$ python -m pip install --upgrade pip  
$ pip install -r requirements.txt  
$ cd DTAproject/
$ python manage.py migrate  
$ python manage.py runserver

(another terminal)
$ source venv/Scripts/activate  
$ cd DTAproject/
$ python manage.py runbot
```

Перейти по http://127.0.0.1:8000/homepage/

