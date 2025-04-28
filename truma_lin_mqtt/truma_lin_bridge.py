import time
import serial
import paho.mqtt.client as mqtt

MQTT_BROKER = "192.168.8.166"
MQTT_PORT = 1883
MQTT_TOPIC_PREFIX = "truma/lin"

def main():
    ser = serial.Serial('/dev/ttyUSB0', 19200, timeout=1)
    client = mqtt.Client()
    client.connect(MQTT_BROKER, MQTT_PORT, 60)

    while True:
        if ser.in_waiting:
            line = ser.readline().decode(errors='ignore').strip()
            if line:
                print("Empfangen:", line)
                client.publish(f"{MQTT_TOPIC_PREFIX}/raw", line)
        time.sleep(0.1)

if __name__ == "__main__":
    main()
