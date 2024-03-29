# Step 1
## Разворачивание окружения
* Первая задача – развернуть проект в продакшен среде. Проект должен быть развернут на PaaS. Для нашего проекта будет достаточно бесплатных планов, которые включают в себя работу с базой данных PostgreSQL.

## Требования к проекту
* ✅ Проект должен быть реализован на poetry
* ✅ При инициализации пакета задайте имя hexlet-code
* ✅ Проект должен содержать приложение Django с именем task_manager, содержащее модуль settings. Другими словами, проект, который мы разрабатываем, можно использовать снаружи:

from task_manager import settings
* Названия полей форм (атрибут name), тексты кнопок, flash-сообщений и другие тексты должны точно соответствовать демонстрационному проекту. Дизайн может быть свой

* ✅ Список разрешенных хостов ALLOWED_HOSTS должен содержать запись webserver

## Задачи
* ✅ Убедитесь, что вы используете Python версии 3.8 или выше
* ✅ Настройте базовое окружение, которое после старта на http-запрос на главную страницу (/) выдаёт приветствие
* ✅ Заведите аккаунт на Railway
* Добавьте в README.md ссылку на задеплоенное приложение, по которой можно посмотреть то, что получилось
## Подсказки
* ✅ Управление настройками через пакет python-dotenv
* ✅ Секреты (любые доступы) должны передаваться через переменные окружения, по понятным причинам их нельзя хранить в репозитории
* ✅ Для подключения базы данных по ссылке используйте библиотеку dj-database-url


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

# Step 4
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
CRUD Статусов
Каждая задача в таск-менеджере обычно имеет статус. С его помощью можно понять, что происходит с задачей, сделана она или нет. Задачи могут быть в таких статусах: [новый, в работе, на тестировании, завершен]

## Роуты текущего шага
* GET /statuses/ — страница со списком всех статусов
* GET /statuses/create/ — страница создания статуса
* POST /statuses/create/ — создание нового статуса
* GET /statuses/<int:pk>/update/ — страница редактирования статуса
* POST /statuses/<int:pk>/update/ — обновление статуса
* GET /statuses/<int:pk>/delete/ — страница удаления статуса
* POST /statuses/<int:pk>/delete/ — удаление статуса
## Требования к проекту
* Имя поля формы в вашем проекте совпадает с именем в демонстрационном проекте
* Статус нельзя удалить, если он связан хотя бы с одной задачей (сущность следующего шага)
* Возможность просматривать, создавать, обновлять и удалять статусы доступна только залогиненным пользователям
* Названия статусов могу быть любыми
## Задачи
* Напишите тесты для CRUD статусов
* Реализуйте CRUD статусов (создание, обновление, удаление, отображение)
* Подключите flash-сообщения, как в демонстрационном проекте
* Добавьте ссылку на список статусов в основное меню
* Сделайте так, чтобы возможность добавлять, редактировать, просматривать и удалять статусы была доступна только залогиненным пользователям


# Step 5
## Роуты текущего шага
* GET /tasks/ — страница со списком всех задач
* GET /tasks/create/ — страница создания задачи
* POST /tasks/create/ — создание новой задачи
* GET /tasks/<int:pk>/update/ — страница редактирования задачи
* POST /tasks/<int:pk>/update/ — обновление задачи
* GET /tasks/<int:pk>/delete/ — страница удаления задачи
* POST /tasks/<int:pk>/delete/ — удаление задачи
* GET /tasks/<int:pk>/ — страница просмотра задачи
## Требования к проекту
* Связь между сущностями реализована внешними ключами
* Имена полей формы совпадают с демонстрационным проектом
* В проекте нельзя удалить пользователя, если он связан с задачами
* Фильтрация задач может быть реализована, но это необязательно
## Задачи
* Напишите тесты для CRUD задач
* Реализуйте CRUD задач
* Подключите flash-сообщения, как в демонстрационном проекте
* Добавьте в основное меню ссылку на список задач
* Сделайте так, чтобы добавлять, редактировать и просматривать задачи могли только залогиненные пользователи
* Сделайте так, чтобы удалять задачи мог только их создатель


# Step 6
## Роуты текущего шага:
* GET /labels/ — страница со списком всех меток
* GET /labels/create/ — страница создания метки
* POST /labels/create/ — создание новой метки
* GET /labels/<int:pk>/update/ — страница редактирования метки
* POST /labels/<int:pk>/update/ — обновление метки
* GET /labels/<int:pk>/delete/ — страница удаления метки
* POST /labels/<int:pk>/delete/ — удаление метки
## Требования к проекту
* Имена полей формы должны совпадать с демонстрационным проектом
* В проекте не должно быть возможности удалить метку, если она связана с задачей
* Названия меток могу быть любыми
## Задачи
* Напишите тесты для CRUD меток
* Реализуйте CRUD меток
* Организуйте связь «многие ко многим» с задачами
* Реализуйте возможность добавлять метки при создании и изменении задач
* Добавьте в основное меню ссылку на список меток
* Сделайте так, чтобы только залогиненные пользователи могли добавлять, редактировать и просматривать метки
* Сделайте так, чтобы пользователь не мог удалить метку, если она связана с задачами
## Подсказки
* Чтобы реализовать возможность выбора нескольких меток, используйте тег select с атрибутом multiple (смотрите пример в демонстрационном проекте)