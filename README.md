<h1 align="center">Проект по тестированию онлайн-магазина 
<p align="center">
<a href="https://online.metro-cc.ru/" target="_blank">
<img src="https://upload.wikimedia.org/wikipedia/commons/5/53/Logo_METRO.svg" 
alt="METRO" width="128" height="64"> </a> 
</p></h1>

#### Список реализованных автотестов
- Добавление товара в корзину
- Переход по разделам онлайн-магазина
- Оформление доставки заказа по выбранному адресу
- Оформление самовывоза заказа по выбранному адресу

## Структура проекта
### Проект реализован с использованием
|                                   Python                                    |                                   Pytest                                    |                                              PyCharm                                              |                                            Selene                                            |                                    Jenkins                                    |                           Allure Report                            |                                Telegram                                 |
|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|:------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| <img src="/Images/python-original.svg" alt="Python" width="45" height="45"> | <img src="/Images/pytest-original.svg" alt="Pytest" width="45" height="45"> |             <img src="/Images/PyCharm_Icon.svg" alt="Pycharm" width="45" height="45"> |             <img src="/Images/selenoid.png" alt="Selene" width="45" height="45"> | <img src="/Images/jenkins-original.svg" alt="Jenkins" width="45" height="45"> | <img src="/Images/allure.png" alt="Allure" width="45" height="45"> | <img src="/Images/telegram.svg" alt="Telegram" width="45" height="45">  |

## Запуск автотестов выполняется на сервере Jenkins
> <a target="_blank" href="LINK">Ссылка на проект в Jenkins</a>

### Для запуска автотестов в Jenkins
1. Открыть проект

![This is an image](/Images/Screenshots/Jenkins_main.png)

2. Выбрать пункт "Собрать с параметрами"

![This is an image](/Images/Screenshots/Jenkins_main.png)

3. В случае необходимости изменить параметры, выбрав значения из выпадающих списков

![This is an image](/Images/Screenshots/Jenkins_main.png)

4. Нажать "Собрать"

![This is an image](/Images/Screenshots/Jenkins_main.png)

5. Результат запуска сборки можно посмотреть в отчёте Allure

![This is an image](/Images/Screenshots/allure_report.png)

### Локальный запуск автотестов
1. Клонируйте репозиторий
2. Создайте и активируйте виртуальное окружение
  ```bash
  python -m venv .venv
  source .venv/bin/activate
  ```
3. Установите зависимости с помощью pip
  ```bash
  pip install -r requirements.txt
  ```
4. Для запусков тестов локально используйте команду 
  ```bash
  pytest -sv
  ```
5. Для запусков тестов удаленно используйте команду 
  ```bash
  environment='remote' pytest -sv
  ```

Получение отчёта allure:
```bash
allure serve allure-results
``` 

### Пример видеозаписи прохождения теста
![This is an image](/Images/Screenshots/test_gif.gif)

### Настроено автоматическое оповещение о результатах сборки Jenkins в Telegram-бот
![This is an image](/Images/Screenshots/bot.png)
