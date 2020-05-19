Тестовое задание от **Фитнес** **Кит** на позицию 

Python разработчик на backend
---

Задание:
Необходимо реализовать сервис на django, который будет выдавать json в следующем [формате:](https://sample.fitnesskit-admin.ru/schedule/get_group_lessons_v2/1/)

<details>
  <summary>Формат json ответа</summary>
  

  ```php
  [{
    "name": "Stretch", 
    "description": "Cистема упражнений, направленная на растяжку, развитие гибкости и улучшение осанки. ПРОДОЛЖИТЕЛЬНОСТЬ УРОКА 45 мин.", 
    "place": "Студия 1", 
    "teacher": "Smith Helen", 
    "startTime": "12.15", 
    "endTime": "13.00", 
    "weekDay": 2, 
    "appointment_id": "6928d4cd-6fef-4e38-b149-3f9f56a50b78", 
    "service_id": "e154f5fb-7ecd-11e8-8150-9c5c8e747603", 
    "pay": false, 
    "appointment": false, 
    "teacher_v2": {
		                  "short_name": "Helen", 
		                  "name": "Smith Helen", 
		                  "position": "Master-trainer of GP", 
		                  "imageUrl": "http://95.165.159.104:90/fitnes_t/hs/nfc_mobile/files/e639a68b-b34a-11e8-8155-9c5c8e747603.jpg"
		              }, 
    "color": "#FFC0CB", 
    "availability": 4 
  }]
  ```

</details>


Должна быть возможность править данные в админке
 
В решении тестового задания просим сразу прислать ссылку на GitHub для просмотра кода и ссылку на тестовый сервер для просмотра сервиса в собранном состоянии.

Результат:
==========

[Тестовый сервер](http://nine3man.pythonanywhere.com/api/courses/)

[Админка](http://nine3man.pythonanywhere.com/admin/)

Для модели Course реализован функционал CRUD через api.
