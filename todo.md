# Step 1
## Разворачивание окружения
* Первая задача – развернуть проект в продакшен среде. Проект должен быть развернут на PaaS. Для нашего проекта будет достаточно бесплатных планов, которые включают в себя работу с базой данных PostgreSQL.

## Требования к проекту
* Проект должен быть реализован на poetry
* При инициализации пакета задайте имя hexlet-code
* Проект должен содержать приложение Django с именем task_manager, содержащее модуль settings. Другими словами, проект, который мы разрабатываем, можно использовать снаружи:

from task_manager import settings
* Названия полей форм (атрибут name), тексты кнопок, flash-сообщений и другие тексты должны точно соответствовать демонстрационному проекту. Дизайн может быть свой

* Список разрешенных хостов ALLOWED_HOSTS должен содержать запись webserver

## Задачи
* Убедитесь, что вы используете Python версии 3.8 или выше
* Настройте базовое окружение, которое после старта на http-запрос на главную страницу (/) выдаёт приветствие
* Заведите аккаунт на Railway. Если вы из РФ, вам необходимо подключить VPN и указать другую страну
* Задеплойте то, что получилось. Этот пункт крайне важно выполнить, как можно раньше. Нет ничего важнее, чем быстрая доставка (читаем "Цель" и знакомимся с DevOps)
* Добавьте в README.md ссылку на задеплоенное приложение, по которой можно посмотреть то, что получилось
* Подсказки
* Управление настройками через пакет python-dotenv
* Секреты (любые доступы) должны передаваться через переменные окружения, по понятным причинам их нельзя хранить в репозитории
* Для подключения базы данных по ссылке используйте библиотеку dj-database-url


# Step 2
## Серверный рендеринг
Чтобы пользователи смогли пользоваться нашим сервисом, необходимо предоставить им удобный, адаптивный, красивый, современный интерфейс. В проекте для этой задачи мы будем использовать фреймворк Bootstrap. Благодаря Bootstrap такие вопросы решаются на раз-два. В этом шаге мы поработаем над подключением интерфейса сайта и обеспечим удобную работу с текстами.

## Роуты текущего шага:
/ - главная страница с меню, в котором есть кнопки: вход, регистрация, пользователи
## Требования к проекту
* Отсутствие своих стилей. Только бутстрап и его возможности
* Фронтенд рендерится на бэкенде. Это значит, что страница собирается бэкендом DjangoTemplates, который возвращает подготовленный HTML. И этот HTML отдаётся сервером
* Все тексты должны хранится в i18n
## Задачи
* Установите пакет django-bootstrap4 в проект
* Выберите из Bootstrap Examples дизайн для своего приложения
* Подключите этот дизайн в проект, используя шаблон, и настройте проект так, чтобы он отдавал этот шаблон при запросе на главную (роут /)
* Организуйте хранение текстов в i18n и их подстановку в шаблоне
* Задеплойте результат и убедитесь, что всё работает

# Step 3
## Пользователи и аутентификация
* По сравнению с большими системами, наша будет содержать только самый минимум: пользователей, задачи, статусы и метки. Если вам понравится процесс, то не останавливайте себя и допилите проект после окончания официального времени.

* Для аутентификации пользователей в проекте используются стандартные средства Django. В нашей системе пользователи будут авторизированны на все действия, то есть всем доступно всё.

## Роуты текущего шага
* GET /users/ – страница со списком всех пользователей
* GET /users/create/ – страница регистрации нового пользователя (создание)
* POST /users/create/ – создание пользователя
* GET /users/<int:pk>/update/ – страница редактирования пользователя
* POST /users/<int:pk>/update/ – обновление пользователя
* GET /users/<int:pk>/delete/ – страница удаления пользователя
* POST /users/<int:pk>/delete/ – удаление пользователя
* GET /login/ – страница входа
* POST /login/ – аутентификация (вход)
* POST /logout/ – завершение сессии (выход)
## Требования к проекту
* Используйте встроенные в Django представления на основе классов
* Имена полей формы оставляйте стандартными, они должны выглядеть таким образом: name="username" и id формата id="id_username". Образец можно посмотреть в демонстрационном проекте
* Редактировать и обновлять себя может только сам пользователь
* Task Management
* MVC
* URL dispatcher
* Создание форм из моделей
* Встроенный API представлений на основе классов
* Аутентификация пользователей в Django
* Написание и запуск тестов
* Django test client
* Flash message
## Задачи
* Подключите поставляемые с Django middleware, относящиеся к работе с пользователями
* Включите встроенную в Django админку
* Реализуйте отображения списка пользователей с удобными ссылками для редактирования и удаления каждого из них. Проверьте, что на странице пользователей, выводится список пользователей, он должен быть доступен без авторизации
* Реализуйте создание пользователей, редактирование и удаление
* Реализуйте аутентификацию
* После регистрации нового пользователя должен происходить редирект на страницу входа
* После успешного входа, должен происходить редирект на главную
* После успешного изменения пользователя, должен происходить редирект на страницу со списком пользователей
* В случае ошибок аутентификации пользователю должно отображаться дружелюбное флэш-сообщение об ошибке. После успешного выполнения операции, также должно показываться флэш-сообщение
* Напишите тесты для CRUD пользователей, где C – это регистрация, U – обновление и D – удаление