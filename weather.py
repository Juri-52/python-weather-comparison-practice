import requests

# TODO: 選んだ都市の座標を使い、現在の気温・湿度・対象時刻を取得する。
def get_weather_data(latitude, longitude):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m",
        "timezone": "Asia/Tokyo"
    }
    data = requests.get(url, params=params).json()
    print(f"気温: {data['current']['temperature_2m']}°C")
    print(f"湿度: {data['current']['relative_humidity_2m']}%")
    print(f"対象時刻: {data['current']['time']}")

# TODO: 取得済みの2都市の気温を比較する関数を作る。
