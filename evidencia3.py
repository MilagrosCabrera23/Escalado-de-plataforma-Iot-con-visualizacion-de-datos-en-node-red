import mysql.connector
import paho.mqtt.client as mqtt
import json
import time  # para los reintentos

# CONFIGURACIÓN DE LA BASE DE DATOS MySQL
db_config = {
    'user': 'root',
    'password': '34215876a.',
    'host': 'localhost',  # o la IP del servidor MySQL  
    'database': 'evidencia2'
}
# Función que se ejecuta cuando se conecta al broker MQTT   
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado al broker MQTT exitosamente")
        client.subscribe("esp32/sensordata")  # Suscripción al tema
    else:
        print(f"Error al conectar con código: {rc}")


# Función que se ejecuta cuando se recibe un mensaje desde el broker MQTT
def on_message(client, userdata, msg):
    # print(f"Mensaje recibido: {msg.payload.decode()}")
    message = msg.payload.decode()
    try:
        data = message.split(",")  # Separar en comas cada string
        temp = float(data[0].split(":")[1].strip().replace("°C", ""))
        hum = float(data[1].split(":")[1].strip().replace("%", ""))
        save_to_database(temp, hum)
    except Exception as e:
        print(f"Error procesando el mensaje: {e}")

# Función para guardar los datos en la base de datos
def save_to_database(temp, hum, retries=3):
    for attempt in range(retries):
        try:
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()
            query = "INSERT INTO datos_sensor (temperature, humidity) VALUES (%s, %s)"
            cursor.execute(query, (temp, hum))
            connection.commit()
            print(f"Datos guardados: Temperatura={temp}, Humedad={hum}")
            break
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            time.sleep(3)
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

# Configuración del cliente MQTT
client = mqtt.Client()

# Vincular las funciones de conexión y recepción de mensajes
client.on_connect = on_connect
client.on_message = on_message

# Conectar al broker MQTT.
client.connect("broker.hivemq.com", 1883, 60)

# Mantener la conexión y esperar los mensajes
client.loop_forever()
