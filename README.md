### Дипломный проект с автотестами Sela, LiveJournal, Gigachat API


<img src="/media/demo.png">

### Используемые инструменты

| Python                                                            | Pycharm                                                            | GitHub                                                     | Selenium                                                     | Allure                                                     | Jenkins                                                     |                                                  
|:------------------------------------------------------------------|--------------------------------------------------------------------|------------------------------------------------------------|--------------------------------------------------------------|------------------------------------------------------------|-------------------------------------------------------------|
| <img height="50" src="media/icons/python.png" width="50"/> | <img height="50" src="media/icons/pycharm.png" width="50"/> | <img height="50" src="media/icons/github.png" width="50"/>  | <img height="50" src="media/icons/selenium.png" width="50"/> | <img height="50" src="media/icons/allure.png" width="50"/> | <img height="50" src="media/icons/jenkins.png" width="50"/> | 

### Автотесты

API:
* test_giga_api_models
* test_giga_api_text_generate
* test_giga_api_unauthorized

LiveJournal.UI:
* test_create_post
* test_update_post
* test_delete_post

Sela.UI:
* test_open_all_tabs
* test_open_babies_clothes
* test_open_favorites
* test_add_any_cloth_to_favorites

### Allure

Добавлен отчет о прохождении автотестов

<img src="/media/allurereport.png">

К тестам приложены артефакты: screenshot, video, page source

<img src="/media/allurereport2.png">

### Jenkins

Для запуска автотестов в Jenkins была настроена конфигурация

<img src="/media/config.png">

Для запуска автотестов в Jenkins нужно нажать на Build Now

<img src="/media/tests.png">

### Telegram

Отчет о пройденных тестах приходит в Telegram:

<img src="/media/tg.png">