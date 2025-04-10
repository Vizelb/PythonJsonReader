import serial
import time

# Подключение
ser = serial.Serial('COM4', 115200, timeout=2)

# Чтение JSON-файла
with open('data.json', 'rb') as f:
    data = f.read()

chunk_size = 512  # размер одного чанка (можно изменить)
total_chunks = (len(data) + chunk_size - 1) // chunk_size

for i in range(total_chunks):
    chunk = data[i*chunk_size:(i+1)*chunk_size]
    ser.write(chunk)
    
    # Ждём подтверждение от модуля (например, "ACK\n")
    ack = ser.readline()
    if b'ACK' not in ack:
        print(f'Ошибка при отправке чанка {i}')
        break
    time.sleep(0.1)

ser.close()
print("Передача завершена.")
