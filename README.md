## VKBottle bot architecture example

Пример приемлемой на мой взгляд архитектуры проекта с использованием VKBottle 3.0

Поскольку это всего лишь пример, а не реальный проект, местами я использую громоздкие конструкции для маленьких вещей (use_cases, repositories). 
В реальных проектах в этих местах будет значительно больше кода, так что применение именно такого стиля будет оправдано. 

---

### Навигация:

В пакете src основной код проекта. Его содержимое:

- \__main\__.py - точка входа. Содержит только экземпляр бота и его запуск.
- app.py - модуль, в котором происходит сборка приложения. 
- config.py - конфигурация проекта, которая берется из переменных окружения. В src нужно обязательно создать .env-файл с перечнем необходимых констант.
- models - пакет с моделями и всем, что относится к работе с базой данных.
- blueprints - разделение кода на логические части.
- repositories - реализация паттерна Repository.
- use_cases - бизнес-логика.
- initialize.py - подготовка БД к первому запуску проекта.

В tests содержатся тесты. В этом примере они больше формальные, у меня не было цели что-то и правда протестировать.
Мне хотелось показать как в принципе в подобном проекте должны выглядеть тесты и где они должны лежать.
Про архитектуру самих тестов можно прочитать в "Python Testing with Pytest: Simple, Rapid, Effective, and Scalable".

### Запуск:

1. Запуск бота вместе с БД через `docker-compose` 
```bash
# Сборка и запуск контейнеров
docker-compose up --build
# Сборка и запуск контейнеров в фоновом режиме
docker-compose up --build -d
# Остановить контейнеры поле запуска в фоновом режиме
docker-compose down
```
2. Сборка и запуск контейнера через Docker
```bash
docker build -t vkbottle-example .
docker run vkbottle-example
# Или
docker run -d vkbottle-example
# Для запуска в фоновом режиме
```
3. Ручной запуск через `python -m src`

PR, код-ревью и любая критика приветствуются.
