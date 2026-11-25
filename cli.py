from cities import CITIES
from weather import get_weather_data

# TODO: メニューと都市一覧を表示し、都市名の入力を受け付ける。
def main():
    while True:
        print("===天気アプリ===")
        print("1　天気を調べる")
        print("2　気温を比較する")
        print("3　終了")
        choice = input("番号を入力： ")
        if choice == "1" or choice == "１":
            # TODO: 天気を調べる処理
            print("---都市を選択---")
            for city in CITIES:
                print(city)
            while True:
                search_city = input("都市名を入力：")
                if search_city in CITIES:
                    latitude, longitude = CITIES[search_city]
                    get_weather_data(latitude, longitude)
                    break
                else:
                    print("エラー：無効な都市名")
        elif choice == "2" or choice == "２":
            # TODO: 気温を比較する処理
            pass
        elif choice == "3" or choice == "３":
            print("---アプリ終了---")
            break
        else:
            print("エラー：無効なコマンド")
# TODO: weather.pyを使って、天気または気温差を表示する。
# TODO: 入力ミスと通信エラーの後も、次の操作ができるようにする。

if __name__ == "__main__":
    main()