# telegram_bot_1

# О проекте
---
Проект сделан по ТЗ найденному на "Хабр Фриланс".\
Данный проект не выполнял, было описанно ТЗ, скопировал его и сделал по нему данный проект.\
Данный проект делал для себя, так как было интересно разобраться с ботом телеграм, и по практиваться с django.\
Возможно проект немного отличается от ТЗ.
# Само ТЗ (описание изменно)
---
##### Сокращения
---
МП - Маркетплейс

Реализовать бота для телеграм
Python: Django / Django Admin
При покупке товара на нем будет QR код, который ведет к запуску телеграм бота
Данный алгоритм со стороны пользователя:
- Покупаем товар на МП
- Сканируем QR код. В коде зашифрована ссылка на бот телеграмм и ID товара
- После запуска бота пользователь должен выбрать с какого маркетплейса куплен товар.
- После появляются кнопки для оценки товара (например от 1 до 5)
- Если пользователь вводит от (1 до 3) то просим пользователя ввести озыв о товаре
- Если от 4 до 5 то пользователю отправляется сообщение с просьбой оценить товар на МП
Админка
- Создать товар
- Редактировать товар
- Список всех товаров
- Просмотр всех коментариев пользователей с плохими оценками
- Фильтр для коментариев просмотренно/не просмотренно
- Список всех маркетинговых сообщений
- Создание маркетингового сообщения.
И при сохранении бот телеграмм должен просто отправить его всем пользователям бота как простое соообщение, и должна быть возможность прикрепить картинку.\
Так же все текстовые строки для бота и конфигурацию бота нужно вынести в константы.

# Развертывание

---
## Ubuntu server 24.04
1. Установка python 3.10
```
sudo apt update && sudo apt upgrade
```
```
sudo add-apt-repository ppa:deadsnakes/ppa -y
```
```
sudo apt update
```
```
sudo apt install python3.10
```
  2. Установка дополнения для создание виртуального окружения
```
 ~/project$ sudo apt install -y python3-venv
```
  3. Создание виртуального окружения в папке с проектом
```
~/project$ python3.10 -m venv venv3_10  
```
4. Установка пакетов в виртуальное окружение
```
~/project$ venv3_10/bin/pip install -r requirements.txt
```
5. Делаем миграцию 
```
~/project$ venv3_10/bin/python backend/manage.py migrate
```
6. Собираем staticfiles
```
~/project$ venv3_10/bin/python backend/manage.py collectstatic
```
7.  Создаем .env файл
```
~/project$ touch .env
```
8. Заполняем .env файл
```
DEBUG=
SECRET_KEY=
T_BOT_TOKEN=
ALLOWED_HOSTS=
```
8. Установка NGINX
```
sudo apt install nginx
```
9. Файл конфигурации NGINX
```

sudo nano /etc/nginx/sites-available/productsite
```
```
server {
	listen 80:
	server_name <domain_name>;

	location /static/ {
		alias <path_to_static_folder>
	}

	location / {
		proxy_set_header Host $host;
		proxy_pass http://127.0.0.1:8000
	}

}
```
```

```

10. asd
```
~/project$ venv3_10/bin/gunicorn backend.backend.wsgi:application
```









11. Файловая структура проекта на сервере
```
project/
├── backend
├── db.drawio
├── example.env
├── .env
├── README.md
├── requirements.txt
├── static
├── tests
└── venv3_10
```



# Команды

---

# Тесты

## Запуск тестов
1. Создание виртуального окружения
```
python3.10 -m venv vnev
```
2. Активация окружения
```
source venv/bin/activate
```
3. Установка зависимостей
```
pip install -r requirements.txt
```
4. Запуск тестов с выводом отчета в allure
```
pytest backend --alluredir allure-results
```
5. Просмотр отчета в allure
```
allure serve allure-results
```