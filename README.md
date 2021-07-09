# MyChat app 

## Installation
```
git clone https://github.com/kalchenkod/mychat.git
cd mychat
```
- Create postgres database **chat_db**
- Substitute *your_username* and *your_password* in my_chat/setteings.py DATABASES with your username and password for postgres
```
pip3 install django //if not installed yet

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```
## Usage
- **homepage**: choose *sign up* button to register or *log in* if you already have one
- perform login/registration
- **menu**: press *Search* button to see all users --> **type full name of the user you want to chat with and press Enter**
- **chat**: type messages and press *Send* button / **reload your page to check for new incoming messages**
## Описание
В общем чат позволяет:
- регистрироваться новым пользователям и логиниться с уже существующего аккаунта (вся информация про пользователя хранится в базе данных), 
доступ далее без этих операций невозможен. 
- посмотреть список всех существующих пользователей и выбрать одного для личного чата
- отправить/получить сообщение с указанием даты и времени отправки
- сохранить всю историю переписки двух пользователей
---------------------
Технологии:
- Я уже был знаком с фреймворком Django, поэтому выбрал именно его для поднятия чата
- Также я имею опыт работы с postgreSQL, что помогло релизовать работу с базами данных
- Все HTML-шаблоны и статические файлы взяты с интернета и переделаны под необходимый интерфейс чата 
-------------------
Время:

Больше всего времени заняла работа с HTML/CSS файлами для создания удобного и корректного интерфейса пользователя. Back-end чатане был проблематичным, посколько я уже 
работал над похожими проектами. Общее время реализации проекта 3 дня.

