from sensor import Sensor


temperature_sensor = Sensor(
    "Temperature",
    "°C",
    22.5,
)
Trump_Intelligence = Sensor(
    "Intelligence de Trump",
    "braincells",
    2,
)

print(temperature_sensor.name,temperature_sensor.value,temperature_sensor.unit)

print(Trump_Intelligence.name,Trump_Intelligence.value,Trump_Intelligence.unit)

Trump_Intelligence.set_value(1)

print(temperature_sensor.name,temperature_sensor.value,temperature_sensor.unit)

print(Trump_Intelligence.name,Trump_Intelligence.value,Trump_Intelligence.unit)