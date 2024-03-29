# 1. Цель проекта

Цель проекта - разработать веб-сервис для организации, хранения, публикации проектов конкретного человека (далее - Сервис). Пользователь сможет с помощью Сервиса создать профиль, создать портфолио, добавить в портфолио свои проекты. 

Сервис для работы с портфолио будет реализован только для программистов и дизайнеров.

# 2. Описание сервиса

Портфолио — это набор работ, проектов, достижений за всю историю деятельности человека в той или иной сфере. Это набор из лучших работ, которые позволят оценить профессионализм и навыки человека.

Digital Portfolio - это веб-сервис для организации, хранения, публикации проектов конкретного человека (студента).

Сервис состоит из следующих основных функциональных блоков:

1. Регистрация, аутентификация и авторизация
2. Функционал профиля
3. Функционал портфолио
4. Функционал каталога пользователей
5. Система оценки проектов

# 2.1.1 Регистрация пользователя в системе

Процесс регистрации пользователей должен быть реализован в интерфейсах Сервиса. При регистрации пользователя должны быть запрошены следующие поля:

* email — обязательное поле
* имя — обязательное поле
* фамилия — опциональное поле
* пароль — обязательное поле
* подтверждение пароля — обязательное поле

После отправки формы регистрации пользователя ему на email приходит письмо с одноразовым кодом для подтверждения регистрации на сайте.

# 2.1.2 Аутентификация

Аутентификация пользователя осуществляется по email и паролю, указанному при регистрации. На странице входа в систему должна быть кнопка "Забыли пароль?", при нажатии на которую пользователь переходит на страницу восстановления пароля, на которой есть поле "Введите почту". Если в системе существует аккаунт, привязанный к этой почте, то на нее приходит письмо со ссылкой, ведущей на страницу смены пароля, на которой есть поля "введите новый пароль" и "подтвердите новый пароль". После нажатия на кнопку "Сменить пароль", появляется уведомление "Пароль успешно изменён", и пользователь переходит на страницу авторизации.

# 2.2 Функционал профиля

Пользователь после аутентификации (ввода логина и пароля) получает доступ к функционалу профиля. Этот функционал состоит из следующих блоков:

1. Редактирование данных профиля
2. Функционал работы с портфолио (описывается в пункте 2.3)

# 2.2.1 Редактирование профиля

В этом разделе у пользователя есть возможность редактированя данных своего профиля. Пользователю предлагаются для редактирования/заполнения следующие поля:

* Имя - обязательное поле (Строка)
* Отображаемое имя (Username) - обязательное поле (уникальное значение) (Строка)
* Род деятельности - обязательное поле
* Фамилия - опциональное поле (Строка)
* О себе - опциональное поле (Длинная строка)
* Используемые технологии - опциональное поле (Строка)
* Возраст - опциональное поле (Число от нуля до 100)
* Мобильный телефон - опциональное поле (есть возможность указывать или не указывать его она странице профиля) (Число)
* Образование - опциональное поле (Длинная строка)
* Социальные сети - опциональное поле (Пополняемый список)

На сайте есть только два варианта Рода деятельности - "Программист" и "Дизайнер". Пользователь выбирает один вариант в выпадающем списке при редактировании своего профиля.

Поля, в которые была введена информация, будут отображаться на публичной странице профиля пользователя. 

Должна быть возможность добавления фотографии профиля и обложки для страницы профиля.

На странице профиля должна быть вкладка "Портфолио", при переходе на которую пользователь получает доступ к функционалу работы с портфолио.

Также в профиле должна быть реализована возможность смены пароля. Смена пароля происходит следующим образом - при нажатии кнопки "Смена пароля" пользователь переходит на страницу восстановления пароля, на которой есть следующие поля: "введите старый пароль", "введите новый пароль", "подтвердите новый пароль", также должна быть кнопка сброса пароля, при нажатии на которую пользователю на почту приходит письмо со ссылкой, которая ведет на страницу смены пароля, в которой нет поля "старый пароль", а есть только "введите новый пароль" и "подтвердите новый пароль" (переход по ссылке из письма является способом аутентификации пользователя).

# 2.2.2 Профиль

На странице профиля должны быть указаны все поля, указанные пользователем при его редактировании. Должны отображаться фотография и обложка профиля, имя/username пользователя.

Если у пользователя не добавлено портфолио - показывать надпись "*имя* еще не добавил ни одного проекта в портфолио".

Если добавлено портфолио - в профиле сразу отображать список проектов из этого портфолио.

На странице есть кнопка "Редактировать портфолио", при нажатии на которую пользователь переходит на страницу редактирования портфолио. Под редактированием портфолио понимается добавление новых проектов в портфолио, удаление одного или нескольких проектов из портфолио, возможность редактировать отдельные проекты.

Если пользователь еще не добавил ни одного проекта, вместо кнопки "Редактировать портфолио", должна быть кнопка "Добавить первый проект в портфолио".

# 2.3 Функционал работы с портфолио

В этом разделе у пользователя есть возможность создания и редактирования своего портфолио.

Портфолио состоит из проектов. Каждый проект в портфолио добавляется отдельно. Проекты можно добавлять, удалять и редактировать.

Портфолио считается добавленным (созданным), если пользователь добавил хотя бы один проект

На странице редактирования портфолио пользователь может добавить или удалить проект в портфолио, также имеет доступ к редактированию проекта.

# 2.3.1 Проект

Проект - продукт, разработанный пользователем или при его участии. Состоит из следующих составных частей:

* Тизер (карточка проекта)
* Обложка
* Материалы (фотографии, видео)
* Описание проекта
* Дополнительные материалы 
* Ссылка на открытый github репозиторий (для программистов)

Тизер(карточка проекта) - то, что видит человек, просматривающий портфолио. По клику на тизер открывается страница проекта. тизер состоит из названия проекта, краткого описания, обложки. *Возможно на тизере будет указано количество лайков*.

Материалы проекта могут содержать в себе фотографии, gif, и видео.

В описание проекта можно добавить форматированный текст (с заголовками разного размера, жирным/подчеркнутым/перечеркнутым текстом, курсивом, списками).

Дополнительные материалы представляют собой набор ссылок (не более пяти), которые может добавить пользователь к своему проекту. Это могут быть ссылки на скачивание материалов проекта, ссылка на сайт и тому подобное.

Автор (создатель) проекта должен иметь доступ к редактированию проекта со страницы проекта.

# 2.4 Каталог пользователей

На главной странице сайте должен быть реализован каталог пользователей. Каталог пользователей - список пользователей, создавших свое портфолио на сайте. Каждый пользователь отображается в виде карточки, на которой указано его Имя (Фамилия), род деятельности, описание из профиля, обложка карточки.

При нажатии на карточку открывается профиль пользователя. Просмотр каталога и страниц пользователей доступен авторизованным и неавторизованным пользователям.

По каталогу будет доступен поиск по имени, username. Фильтр по роду деятельности.

# 2.5 Система оценки проектов

На сайте должна быть реализована Система оценки проектов (далее - Система). Система состоит из следующих функциональных блоков:

1. Функционал оценки проекта
2. Функционал комментирования проекта

# 2.5.1 Оценка проекта

Любой зарегистрированный пользователь может поставить лайк любому проекту любого пользователя. Лайк - положительная оценка проекта. Есть возможность убрать поставленный лайк. На тизере и на странице проекта есть счётчик лайков. Один пользователь может поставить не более одного лайка на проект.

# 2.5.2 Комментирование проекта

Система позволяет пользователям оставлять комментарии под любым проектом другого пользователя. Комментировать проекты могут только зарегистрированные пользователи. Если незарегистрированный пользователь пытается прокомментировать проект, ему предлагается пройти регистрацию, после этого он получит доступ к оценке и комментированию проектов.

Под каждым проектом есть блок "Комментарии", где расположены все комментарии (от старых к новым, каждый новый комментарий добавляется в конец списка). Комментарий содержит имя пользователя, оставившего комментарий, сам текст комментария. Пользователь должен иметь возможность редактировать комментарии, которые он оставил.

# 2.5.3 Понравившиеся проекты

Проект, на который пользователь поставил лайк, добавляется в его личный список "Понравившиеся проекты". При убирании лайка с проекта, проект удаляется из списка. Понравившиеся проекты видит только создатель списка (пользователь, который ставит лайки). Порядок проектов в списке - сначала "старые", потом "новые" (т.е. первым в списке идет тот проект, на который лайк был поставлен первым).

# 3. Предлагаемый стек технологий

* Бэкенд:
    - Язык Python
    - Фреймворк Flask
    - База данных PostgreSQL

* Фронтенд:
    - Vue.js
    - JavaScript

# 4. Требования к дизайну

Минимализм, лаконичность, акцент на контент. Белый фон. Должен присутствовать
логотип Сервиса где-то на странице. Логотип надо разработать в рамках
этого проекта.

В нижней части страницы (в подвале) должно быть написано:

«Работает на Open Source» со ссылкой на GitHub проекта.
