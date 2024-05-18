from fastapi import FastAPI
from rpi_backlight import Backlight

app = FastAPI()
backlight = Backlight()


# get brightness
@app.get("/brightness")
async def get_brightness():
    return {"brightness": backlight.brightness}


# set brightness
@app.post("/brightness")
async def set_brightness(brightness: int):
    backlight.brightness = brightness
    return {"brightness": backlight.brightness}


# get fade duration
@app.get("/fade_duration")
async def get_fade_duration():
    return {"fade_duration": backlight.fade_duration}


# set fade duration
@app.post("/fade_duration")
async def set_fade_duration(fade_duration: int):
    backlight.fade_duration = fade_duration
    return {"fade_duration": backlight.fade_duration}


# get power
@app.get("/power")
async def get_power():
    return {"power": backlight.power}


# set power
@app.post("/power")
async def set_power(power: bool):
    backlight.power = power
    return {"power": backlight.power}


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

