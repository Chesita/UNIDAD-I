from machine import Pin
import utime

# Definir pines
RED_PIN = 17
GREEN_PIN = 27
BLUE_PIN = 22
BUTTON_PIN = 23

# Configurar pines
red = Pin(RED_PIN, Pin.OUT)
green = Pin(GREEN_PIN, Pin.OUT)
blue = Pin(BLUE_PIN, Pin.OUT)
button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)  # Activar resistencia pull-up

# Lista de colores (combinaciones de RGB)
colors = [
    (1, 0, 0),  # Rojo
    (0, 1, 0),  # Verde
    (0, 0, 1),  # Azul
    (1, 1, 0),  # Amarillo
    (1, 0, 1),  # Magenta
    (0, 1, 1),  # Cyan
    (1, 1, 1)   # Blanco
]

color_index = 0  # Índice del color actual

def set_color(color):
    """Establece el color del LED RGB."""
    red.value(color[0])
    green.value(color[1])
    blue.value(color[2])

# Establecer color inicial
set_color(colors[color_index])

try:
    while True:
        if button.value() == 0:  # Si el botón es presionado
            utime.sleep(0.2)  # Antirrebote
            color_index = (color_index + 1) % len(colors)  # Cambiar al siguiente color
            set_color(colors[color_index])
except KeyboardInterrupt:
    print("Programa detenido.")
