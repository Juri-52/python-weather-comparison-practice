from cities import CITIES
from weather import WeatherError, compare_temperatures, get_weather_data


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
            print("---比較する都市を選択---")
            for city in CITIES:
                print(city)

            first_city = None
            while first_city is None:
                selected_city = input("1つ目の都市名を入力：").strip()
                if not selected_city:
                    print("エラー：都市名が入力されていません。")
                elif selected_city not in CITIES:
                    print("エラー：一覧にない都市名です。もう一度入力してください。")
                else:
                    first_city = selected_city

            second_city = None
            while second_city is None:
                selected_city = input("2つ目の都市名を入力：").strip()
                if not selected_city:
                    print("エラー：都市名が入力されていません。")
                elif selected_city not in CITIES:
                    print("エラー：一覧にない都市名です。もう一度入力してください。")
                elif selected_city == first_city:
                    print("エラー：異なる都市を選んでください。")
                else:
                    second_city = selected_city

            try:
                first_latitude, first_longitude = CITIES[first_city]
                first_weather = get_weather_data(first_latitude, first_longitude)
                second_latitude, second_longitude = CITIES[second_city]
                second_weather = get_weather_data(second_latitude, second_longitude)
            except WeatherError as error:
                print(f"エラー：{error}")
                continue

            first_temperature = first_weather["temperature"]
            second_temperature = second_weather["temperature"]
            warmer_city, difference = compare_temperatures(
                first_temperature, second_temperature
            )
            print(
                f"{first_city}：{first_temperature:.1f} "
                f"{first_weather['temperature_unit']}"
            )
            print(
                f"{second_city}：{second_temperature:.1f} "
                f"{second_weather['temperature_unit']}"
            )
            if warmer_city == "same":
                print("両都市の気温は同じです。")
            else:
                city_name = first_city if warmer_city == "first" else second_city
                temperature_unit = first_weather["temperature_unit"]
                print(
                    f"{city_name}のほうが {difference:.1f} "
                    f"{temperature_unit} 暖かいです。"
                )
        elif choice in ("0", "０"):
            print("---アプリ終了---")
            break
        else:
            print("エラー：1、2、0のいずれかを入力してください。")

if __name__ == "__main__":
    main()