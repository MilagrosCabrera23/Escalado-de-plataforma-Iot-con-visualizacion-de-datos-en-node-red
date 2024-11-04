import network
import time
from umqtt.simple import MQTTClient
from machine import Pin
import dht

# Configuración WiFi
ssid = 'Wokwi-GUEST'
password = ''

# Configuración MQTT HiveMQ
mqtt_server = 'broker.hivemq.com'
mqtt_port = 1883
mqtt_topic = 'esp32/sensordata'
client_id = 'evidencia2'

# Conectar a WiFi
def connect_wifi():
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(ssid, password)

    while not station.isconnected():
        print('Conectando a WiFi...')
        time.sleep(1)
    print('Conexión WiFi establecida, IP:', station.ifconfig())

# Publicar datos del sensor
def publish_sensor_data(client):
    sensor = dht.DHT22(Pin(12)) # Pin conectado al DHT22
    sensor.measure()
    temp = sensor.temperature()
    humidity = sensor.humidity()
    payload = f'Temperatura:{temp}°C,Humedad:{humidity}%' # Enviar como string separado por comas


    try:
        client.publish(mqtt_topic, payload)
        print(f'Datos publicados: Temperatura: {temp}°C, Humedad:{humidity}%')

    except Exception as e:
        print(f'Error al publicar: {e}')

# Conectar a MQTT
def connect_mqtt():
    client = MQTTClient(client_id, mqtt_server, port=mqtt_port)
    client.connect()
    print('Conectado al broker MQTT')
    return client

# Iniciar conexión WiFi y MQTT
connect_wifi()
client = connect_mqtt()

# Bucle principal
while True:
    publish_sensor_data(client)
    time.sleep(3)
