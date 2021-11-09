import csv
import googlemaps

gmaps = googlemaps.Client(key='api_key')

# Geocoding an address
# geocode_result = gmaps.geocode('住所')
# print(geocode_result)
# if not len(geocode_result):
#     print("no data")

# Look up an address with reverse geocoding
# reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))


csv_file = "参照元ファイルパス"
new_file = "出力ファイル"
header = ["店名", "住所", "緯度経度", "精度"]

with open(new_file, "w") as new_file:
    writer = csv.writer(new_file)
    writer.writerow(header)

    with open(csv_file) as f:
        reader = csv.reader(f)
        for index, column in enumerate(reader):
            if index in [0, 1]:  # ヘッダー行はスキップ
                continue
            store_name = column[0]
            address = column[1]
            print(f"{index}: {address}")
            geocode_result = gmaps.geocode(address)
            print(geocode_result)
            if not len(geocode_result):  # geocoding apiから値が返却されなければ空文字列を挿入
                geometry = ""
                location = ""
                location_type = "no data"
            else:
                geometry = geocode_result[0]["geometry"]
                lat = geometry["location"]["lat"]
                lng = geometry["location"]["lng"]
                location = f"{lat}, {lng}"
                location_type = geometry["location_type"]
            row = [store_name, address, location, location_type]
            writer.writerow(row)

