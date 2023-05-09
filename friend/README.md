# Проект Friend_app

<i>Проект Django-сервиса друзей</i>

<i>Задача: написать бэкенд проекта и API для него так,
чтобы они полностью соответствовали ТЗ.</i>

<i><b>Ресурсы API Friend_app</i></b>
<blockquote>
☑ Ресурс users: пользователи; <br>
☑ Ресурс friends: друзья;  <br>
</blockquote>

<i><b>Технологии</i></b>
<blockquote>
☑ Python 3.11.0 <br>
☑ Django REST framework
</blockquote>

<i><b>Запуск проекта в dev-режиме:</i></b><br>
☑ Клонируйте проект с GitHub:</li>
    <blockquote>
      <https://github.com/Vende1337/Friends_app.git>
    </blockquote>  
☑ Создайте и активируйте виртуальное окружение:</li>
    <blockquote>
      python -m venv venv<br>
      source venv/Scripts/activate
    </blockquote>  
☑ Установите зависимости из файла requirements.txt (не забудьте предварительно обновить pip и перейти в папку Friends_app/friend):</li>
    <blockquote>
      pip install -r requirements.txt
    </blockquote>
☑ Выполните миграции:</li>
    <blockquote>
      python manage.py migrate
    </blockquote>
☑ При необходимости создайте суперпользователя для предоставления прав админинстраторам:</li>
    <blockquote>
      python manage.py createsuperuser
    </blockquote>
 ☑ Запустите сервер разработчика:</li>
    <blockquote>
      python manage.py runserver
    </blockquote>
</li>

<i><b>Просматривайте динамическую документацию API вместе с примерами запросов через redoc/swagger (напр., <http://127.0.0.1:8000/redoc/>)</i></b><br>
  
<i><b>Примеры использования API:</i></b><br>  
☑ Регистрация пользователя:</li>
    <blockquote>
     <http://localhost/api/users/>
    </blockquote>  
☑ Просмотр списка друзей:</li>
    <blockquote>
      <http://localhost/api/friends/>
    </blockquote>  
☑ Отправка запроса на добавление в друзья:</li>
    <blockquote>
      <http://localhost/api/friends/requests/send/><br>
      {<br>
     "friend": "Valera"<br>
      }<br>
    в поле friend укажите username пользователя которому хотите отправить запрос в друзья. 
    </blockquote>
☑ Получение входящих запросов на добавление в друзья:</li>
    <blockquote>
      http://localhost/api/friends/requests/incoming/
    </blockquote>    
☑ Принятие входящего запроса на добавление в друзья:</li>
    <blockquote>
      http://localhost/api/friends/requests/incoming/{id}/accept/
    </blockquote>
</li>

Авторы:
<b>Дмитрий Венде</b><br>
