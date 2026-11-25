from cities import CITIES
from weather import WeatherError, get_weather_data

def main():
    while True:
        print("=== 天気アプリ ===")
        print("1　天気を調べる")
        print("2　気温を比較する")
        print("0　終了")
        choice = input("番号を入力：").strip()
        if choice in ("1", "１"):
            print("---都市を選択---")
            for city in CITIES:
                print(city)
            while True:
                search_city = input("都市名を入力：").strip()
                if not search_city:
                    print("エラー：都市名が入力されていません。")
                    continue
                if search_city not in CITIES:
                    print("エラー：一覧にない都市名です。もう一度入力してください。")
                    continue

                latitude, longitude = CITIES[search_city]
                try:
                    weather = get_weather_data(latitude, longitude)
                except WeatherError as error:
                    print(f"エラー：{error}")
                    break

                print(f"{search_city}の天気")
                print(f"気温：{weather['temperature']} {weather['temperature_unit']}")
                print(f"湿度：{weather['humidity']} {weather['humidity_unit']}")
                print(f"対象時刻：{weather['time']}（日本時間）")
                print("データ提供元：Open-Meteo")
                break
        elif choice in ("2", "２"):
            print("気温比較はまだ実装されていません。")
        elif choice in ("0", "０"):
            print("---アプリ終了---")
            break
        else:
            print("エラー：1、2、0のいずれかを入力してください。")

if __name__ == "__main__":
    main()