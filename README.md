# TablesFromNikita
## RU
### Описание
**TablesFromNikita** – это модель, предназначенная для облегчения процесса проектирования баз данных.
Модель обучается на примерах **существующих** баз данных. Она **сохраняет** взаимосвязи между таблицами, между
реквизитами, их типами данных и таблицами, в которых они применяются. При проектировании таблиц, **учитывается**
частота использования реквизитов и их типов данных.
### Требования
Модель **не обладает** какими-либо важными требованиями. Она разрабатывается и тестируется на версии **Python 3.12**.
В её работе **не используются** сторонние библиотеки. Весь код был написан на чистом **Python**.
### Установка
Порядок действий:
```
  git clone https://github.com/NikitaE30/TablesFromNikita.git
```
### Использование
Для проверки возможностей модели, возможно использовать **TestingModel.py**. 
```
py TestingModel.py
```
### В будущем
В ближайшей перспективе разработка модели продолжится. Будет добавлено следующее:
- генерация кода под SQL Server;
- отдельные версии на Английском и Русском языках;
- интеграция с моим [вторым проектом](https://github.com/NikitaE30/TranslatorFromNikita.git);
- натренерованная модель на 200 таблицах (или более).
> Список нововведений будет изменяться/дополняться.
### Текущая версия
Текущая версия модели "TablesFromNikita" - 1.2.4. Это вторая версия модели, со значительными изменениями. В ней были реализованы и
доработаны следующие функции и моменты:
- исправлены мелкие недочёты;
- добавлена модель, натренерованная на 117 таблицах;
- добавлена очистка консоли перед запуском;
- переработано тестирование модели;
- удален requirements.txt (отсутствует его необходимость);
- добавлена поддержка Python версии 3.12;
- добавлена возможность указать желаемые реквизиты в таблицах.
## EN
### Description
**TablesFromNikita** is a model designed to facilitate the database design process.
The model is trained on examples of **existing** databases. It **preserves** the relationships between tables, between
the details, their data types and the tables in which they are used. When designing tables, **takes into account**
the frequency of using the details and their data types.
### Requirements
The model **does not have** any important requirements. It is being developed and tested on version **Python 3.12**.
Her work **does not use** third-party libraries. All the code was written in pure **Python**.
### Installation
Procedure of actions:
```
  git clone https://github.com/NikitaE30/TablesFromNikita.git
```
### Using
To test the capabilities of the model, it is possible to use **TestingModel.py**.
```
py TestingModel.py
```
### In the future
In the near future, the development of the model will continue. The following will be added:
- code generation for SQL Server;
- trained model on 200 tables (or more);
- integration with my [second project](https://github.com/NikitaE30/TranslatorFromNikita.git);
- separate versions in English and Russian.
> The list of innovations will be changed/supplemented.
### Current version
The current version of the "TablesFromNikita" model is 1.2.4. This is the second version of the model, with significant changes. 
The following functions and points were implemented and refined in it:
- minor bugs have been fixed;
- added a model trained on 117 tables;
- added console cleanup before launch;
- redesigned model testing;
- deleted requirements.txt (there is no need for it);
- added support for Python version 3.12;
- added the ability to specify the desired details in the tables.