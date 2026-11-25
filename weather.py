import math
from numbers import Real

import requests


class WeatherError(Exception):
    """天気データを取得・検証できなかった場合のエラー。"""


def get_weather_data(latitude, longitude):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m",
        "timezone": "Asia/Tokyo",
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
    except requests.exceptions.Timeout as error:
        raise WeatherError("天気情報の取得がタイムアウトしました。") from error
    except requests.exceptions.RequestException as error:
        raise WeatherError("天気情報を取得できませんでした。通信状態を確認してください。") from error

    try:
        data = response.json()
    except requests.exceptions.JSONDecodeError as error:
        raise WeatherError("天気サービスから正しい形式の応答がありませんでした。") from error

    if not isinstance(data, dict):
        raise WeatherError("天気サービスから正しい形式の応答がありませんでした。")

    current = data.get("current")
    current_units = data.get("current_units")
    if not isinstance(current, dict) or not isinstance(current_units, dict):
        raise WeatherError("天気サービスの応答に必要なデータがありません。")

    temperature = current.get("temperature_2m")
    humidity = current.get("relative_humidity_2m")
    observation_time = current.get("time")
    temperature_unit = current_units.get("temperature_2m")
    humidity_unit = current_units.get("relative_humidity_2m")

    if (
        isinstance(temperature, bool)
        or not isinstance(temperature, Real)
        or not math.isfinite(temperature)
        or isinstance(humidity, bool)
        or not isinstance(humidity, Real)
        or not math.isfinite(humidity)
        or not isinstance(observation_time, str)
        or not observation_time
        or not isinstance(temperature_unit, str)
        or not temperature_unit
        or not isinstance(humidity_unit, str)
        or not humidity_unit
    ):
        raise WeatherError("天気サービスの応答に有効な気温・湿度・時刻がありません。")

    return {
        "temperature": temperature,
        "temperature_unit": temperature_unit,
        "humidity": humidity,
        "humidity_unit": humidity_unit,
        "time": observation_time,
    }


def compare_temperatures(first_temperature, second_temperature):
    difference = abs(first_temperature - second_temperature)
    if first_temperature > second_temperature:
        return "first", difference
    if second_temperature > first_temperature:
        return "second", difference
    return "same", difference
