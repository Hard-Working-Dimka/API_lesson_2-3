# Обрезка ссылок при помощи ВКонтанте

Скрип позволяет сгенерировать сокращенную ссылку, а так же смотреть по ним количество переходов. 

Зачем это нужно? Чтобы превращать длинные и неуклюжие ссылки в короткие и аккуратные.

До:
>https://dvmn.org/encyclopedia/python_basic_level/what_are_methods/

После обрезки:
> https://vk.cc/cEYXxG

Такие ссылки радуют глаз и отлично вписываются в любой текст, а также позволяют отследить количество переходов по ним.

### Как установить

Для корректной работы необходимо получить сервисный токен приложения. Для этого создайте аккаунт [ВК](https://vk.com/). Далее создайте [приложение](https://id.vk.com/about/business/go/docs/ru/vkid/latest/vk-id/connection/create-application). После этого, перейдите во вкладку "Мои приложения" и нажмите на созданное Вами приложение. На главное странице найдите подзаголовок "Ключи доступа" и скопируйте сервисный ключ доступа.

В скрипте сервисный токен "спрятан" в виде переменной окружения. Для его использования создайте файл `.env` в папке с проектом. Откройте этот файл и вставьте в него следующий код:
```
VK_TOKEN = 'token'
```
Замените `token` на токен, который был получен ранее.

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Запуск

Для запуска скрипта используйте консоль. Обязательным аргументом консольной команды является ссылка (link), которую необходимо сократить, или короткая ссылка, по которой хотите посмотреть количество переходов.

Шаблон команды запуска:
```
python main.py link
```

При вводе неправильной ссылке на экране появится сообщение "Неправильная ссылка!"

Пример работы:
![image](https://github.com/user-attachments/assets/314baec6-1e2e-49a9-afdd-7750053de263)
![image](https://github.com/user-attachments/assets/fc536ece-06d0-40e3-ae21-b5a1fbad3952)

### Цель проекта

Код написан в образовательных целях.
