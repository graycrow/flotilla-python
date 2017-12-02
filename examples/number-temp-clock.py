#!/usr/bin/env python

import time
import flotilla


print("""
This example will display temperature and current time on the Number display
""")

dock = flotilla.Client()

while not dock.ready:
    pass

first_light_sensor = dock.first(flotilla.Light)
first_number_display = dock.first(flotilla.Number)
first_weather_sensor = dock.first(flotilla.Weather)

first_number_display.set_brightness(10)

try:
    while True:
        light = first_light_sensor.light
        brightness = light /4

        if brightness > 255:
            brightness = 255
        if brightness < 1:
            brightness = 1

        first_number_display.set_brightness(brightness)

        first_number_display.set_temp(first_weather_sensor.temperature)
        first_number_display.update()
        time.sleep(5)

        first_number_display.set_current_time()
        first_number_display.update()
        time.sleep(15)

        pressure = first_weather_sensor.pressure

        if pressure > 9999:
             pressure = pressure / 10

        first_number_display.set_string("BAR ")
        first_number_display.update()
        time.sleep(2)

        first_number_display.set_number(pressure)
        first_number_display.update()
        time.sleep(5)

except KeyboardInterrupt:
    dock.stop()
