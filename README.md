# TablesFromNikita
## RU
### Описание
**TablesFromNikita** – это модель, предназначенная для облегчения процесса проектирования баз данных.
Модель обучается на примерах **существующих** баз данных. Она **сохраняет** взаимосвязи между таблицами, между
реквизитами, их типами данных и таблицами, в которых они применяются. При проектировании таблиц, **учитывается**
частота использования реквизитов и их типов данных.
### Требования
Модель **не обладает** какими-либо важными требованиями. Она разрабатывается и тестируется на версии **Python 3.11.4**.
В её работе **не используются** сторонние библиотеки, при этом остаётся файл **requirements.txt**, в котором
прописаны **стандартные** библиотеки.
### Установка
Порядок действий:
```
  git clone https://github.com/NikitaE30/TablesFromNikita.git
  cd TablesFromNikita
  pip install -r requirements.txt
```
### Использование
Для проверки возможностей модели, возможно использовать **TestingModel.py**. 
```
py TestingModel.py
```
### В будущем
В ближайшей перспективе разработка модели продолжится. Будет добавлено следующее:
- генерация кода под SQL Server;
- натренерованная модель на 100 таблицах (или более);
- возможность указать необходимые реквизиты.
> Список нововведений будет изменяться/дополняться.
### Текущая версия
Текущая версия модели "TablesFromNikita" - 1.0.0. Это первая, полностью работоспособная версия. В ней были реализованы 
следующие функции:
- ручная тренеровка модели;
- автоматическая тренеровка модели (Посредством .txt файлов);
- просмотр названий натренерованных таблиц;
- использование модели постредством указания названий таблиц;
- модель, обученная на 38 таблицах;
- иные, мелкие возможности, недостойные Вашего внимания.
## EN
### Description
**TablesFromNikita** is a model designed to facilitate the database design process.
The model is trained on examples of **existing** databases. It **preserves** the relationships between tables, between
the details, their data types and the tables in which they are used. When designing tables, **takes into account**
the frequency of using the details and their data types.
### Requirements
The model **does not have** any important requirements. It is being developed and tested on version **Python 3.11.4**.
Its work **does not use** third-party libraries. File **remainsrequirements.txt** contains **standard** libraries.
### Installation
Procedure of actions:
```
  git clone https://github.com/NikitaE30/TablesFromNikita.git
  cd TablesFromNikita
  pip install -r requirements.txt
```
### Using
To test the capabilities of the model, it is possible to use **TestingModel.py**.
```
py TestingModel.py
```
### In the future
In the near future, the development of the model will continue. The following will be added:
- code generation for SQL Server;
- trained model on 100 tables (or more);
- the ability to specify the necessary details.
> The list of innovations will be changed/supplemented.
### Current version
The current version of the "TablesFromNikita" model is 1.0.0. This is the first fully functional version. The following
functions were implemented in it:
- manual training of the model;
- automatic training of the model (By means of .txt files);
- viewing the names of trained tables;
- using the model by specifying table names;
- a model trained on 38 tables;
- other, small opportunities unworthy of Your attention.