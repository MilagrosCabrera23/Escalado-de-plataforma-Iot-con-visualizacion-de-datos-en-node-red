
# Escalado de la plataforma Iot con visualizacion de-datos en un dashboard usando NODE-RED


 Este proyecto se centra en la creación de un dashboard web que permita la visualización en tiempo real de
los datos recolectados por dispositivos IoT basados en ESP32, utilizando herramientas en este caso Node-RED.

El sistema garantizará una integración eficiente con una base de datos
MySQL, permitiendo el monitoreo continuo y la generación de alertas
automáticas. Además, se busca optimizar la escalabilidad del sistema para
permitir la adición de nuevos sensores y dispositivos sin comprometer el
rendimiento.



## Authors

- [@milagrosCabrera23]https://github.com/MilagrosCabrera23)


## Features

- Objetivos del proyecto:
Desarrollar un sistema de visualización de datos en tiempo real a través de un
dashboard web, que permita monitorear y analizar los datos recolectados por
los sensores de dispositivos ESP32, utilizando herramientas como Grafana o
NODE-RED.

En el desarrollo y  y diseño del sistema utilizamos: 

- Hardware: El sistema estará basado en microcontroladores ESP32 que capturan datos sensorizados como temperatura, humedad, presión, entre otros. Estos dispositivos IoT enviarán los datos a través de una capa de transporte basada en WiFi o MQTT, para ser almacenados en una base de datos MySQL.

- Base de Datos: La base de datos MySQL funcionará como el repositorio central para los datos sensorizados. Esta base de datos será optimizada para soportar consultas en tiempo real y escalabilidad, garantizando un acceso rápido a los datos históricos.

- Dashboard Web: Utilizamos para la creación del mismo a Node-RED, el cual será utilizado para flujos de trabajo dinámicos y visualización en tiempo
real, permitiendo la automatización de tareas basadas en eventos de los sensores.

- Alertas Visuales en el Dashboard: Donde los usuarios recibirán notificaciones visuales
inmediatas en caso de que la temperatura o la humedad superan o están por debajo de los valores definidos, lo que garantiza una respuesta rápida.

- Pruebas: 
● Prueba de umbrales: Se simularon valores extremos de temperatura y humedad para verificar que el sistema genera las alertas correctas cuando los valores están fuera de los límites.

● Prueba de notificaciones: Se probó la efectividad del envío de notificaciones tanto en el dashboard o, asegurando que el tiempo de respuesta es adecuado y los usuarios reciben la alerta en tiempo real.

- Posibles mejoras:
En un futuro, podríamos implementar estás mejoras en el sistema:
● Añadir más métricas; Junto con nuevos sensores para poder monitorear las variables como la calidad del aire o los niveles de luz.

● Ampliar los tipos de notificación: Integrar notificaciones en las aplicaciones móviles o servicios de mensajería como Telegram o Slack,etc.

● Inteligencia artificial: Implementar modelos de predicción para anticiparse a condiciones críticas y emitir alertas antes de que se presenten valores peligrosos.
## 🔗 Links
Wokwi: https://wokwi.com/projects/412636720033069057 


