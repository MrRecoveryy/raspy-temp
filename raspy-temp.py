#Pequeño Script para ver la Temperatura de la CPU de tu Raspberyy
# Se requiere instalar 3 Modulos | Leer "requirements"

from gpiozero import CPUTemperature
import time

cpu = CPUTemperature()

while True:
	print("Temperatura CPU: "+str(cpu.temperature)+" ºC")
	time.sleep(1)
