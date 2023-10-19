# RUS

Небольшая программа, которая за вас введёт все команды **базовой настройки** коммутатора Cisco. Заполните необходимые поля, нажмите кнопку "Начать" и переведите курсор на строку ввода консоли, на это будет 5 секунд, и программа мгновенно введёт все нужные команды. Если какой-то параметр настраивать не нужно, то можно оставить поле пустым и программа пропустит этот пункт. Параметры проверяются на валидность и если где-то будет допущена ошибка, то программа подсветит красным цветом нужный параметр. На данный момент интерфейс только на русском языке.

Параметры, которые можно настроить:

- Имя коммутатора
- Пароль на линию консоли
- Пароль на vty
- Создание пользователя с максимальной привилегией (на данный момент изменить привилегию нельзя). Можно выбрать имя и пароль
- Назначение IP и netmask на vlan 1 (на данный момент префикс не поддерживается)
- Пароль на привилегированный режим
- Приоритет в STP (своё значение, корневой или резервный)

---

---

# ENG

A small program that will enter all the commands for you **basic configuration** of the Cisco switch. Fill in the required fields, click the "Start" button and move the cursor to the console input line, it will take 5 seconds, and the program will instantly enter all the necessary commands. If some parameter does not need to be configured, then you can leave the field empty and the program will pass this item. The parameters are checked for validity and if an error is made somewhere, the program will highlight the desired parameter in red. At the moment, the interface is only in Russian.

Parameters that can be configured:

- Switch name
- Password for the console line
- Password for vty
- Creating a user with the maximum privilege (at the moment it is impossible to change the privilege). You can choose a name and password
- Assigning IP and netmask to vlan 1 (prefix is not supported at the moment)
- Password for enable mode
- Priority in STP (its own value, root or backup)
