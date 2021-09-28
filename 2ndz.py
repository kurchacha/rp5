import RPi.GPIO as GPIO
import time


dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)
levels = 2**bits
maxVoltage = 3.3

def decimal2binary(decimal):
    return [int(bit) for bit in bin(decimal)[2:].zfill(bits)]
def bin2dac(value):
    signal = decimal2binary(value)
    GPIO.output(dac, signal)
    return signal
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)

try:
    while True:
        for value in range(0, 255):
            bin2dac(value)
            time.sleep(0.005)
            signal = bin2dac(value)
            voltage = value / levels * maxVoltage
            print("Введенное число = {:^3} -> {}, выходное напряжение = {:.2f}". format(value, signal, voltage))
        for value in range (255, -1, -1):
            bin2dac(value)
            time.sleep(0.005)
            signal = bin2dac(value)
            voltage = value / levels * maxVoltage
            print("введенное число = {:^3} -> {}, выходное напряжение = {:.2f}".format(value, signal, voltage))

except KeyboardInterrupt:
    print("Программа остановлена с клавиатуры")
    pass
else:
    print("No exceptions")
    pass
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)
    print("cleanup comlited")
