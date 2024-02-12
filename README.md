# urfu-sl-avatar

## Запуск демо приложения
Для запуска демо приложения работы metahuman на UE необходимо установить Unreal engine 5.0.3, Visual Studio 2022 и gstreamer. Cкачать [проект с гугл диска](https://drive.google.com/file/d/1rSip28lbabcmw2viCP_gLRTLFaeRihlV/view?usp=sharing). Разорхивируем проект и находим файл ```MetaHuman_M4U.uproject```, нажимаем правой кнопкой мыши и выбираем ```Generate Visual Studio project files```. Затем запускаем проект в VS ```MetaHuman_M4U.sln```, переходим в ```Обозреватель решений``` нажимаем правую кпопку мыши и выбираем ```Собрать решение```, после успешной сборки проект закрываем VS. Открываем проект в UE, находим папку ```MediaPipe``` и запускаем карту ```SimpleMap``` ![image](https://github.com/ds-hub-sochi/urfu-sl-generation/assets/63962317/5e418117-a396-4a65-a6f8-89b17f409094) 

Видим на экране проект с metahuman ![image](https://github.com/ds-hub-sochi/urfu-sl-generation/assets/63962317/c2fc88e9-5d2f-49e3-98eb-d4599a550453). Перед запуском проекта необходимо проверить срок истечения лицензии, это можно сделать нажав ```Edit >> Plugins >> MediaPipe4U``` ![image](https://github.com/ds-hub-sochi/urfu-sl-generation/assets/63962317/65eb3afc-281d-4c01-951b-c4776dffa1a2)

Если лицензию необходимо обновить, то свежую можно найти по [ссылке](https://github.com/endink/Mediapipe4u-plugin/discussions/82) и загрузить файл нажав на кнопку ```Upload License From File```

![image](https://github.com/ds-hub-sochi/urfu-sl-generation/assets/63962317/773eadc0-d8ab-4a0e-814f-075503413a06)



При нажатии зеленой кнопки play запуститься анимация metahuman с помощью веб-камеры.

