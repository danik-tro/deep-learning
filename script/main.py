import requests #импортируем модуль

files = {
	"districts_info.csv.gz": r"http://localhost:8888/files/data/Dnipro/districts_info.csv.gz?_xsrf=2%7Cd6e9e4ef%7Cd7e135b5f6f3923b5acce414981a2da0%7C1607176611",
	"Dnipro.geojson": r"http://localhost:8888/files/data/Dnipro/Dnipro.geojson?_xsrf=2%7Cd6e9e4ef%7Cd7e135b5f6f3923b5acce414981a2da0%7C1607176611",
	"user_routes_2019_2020.csv.gz": r"http://localhost:8888/files/data/Dnipro/user_routes_2019_2020.csv.gz?_xsrf=2%7Cd6e9e4ef%7Cd7e135b5f6f3923b5acce414981a2da0%7C1607176611",
	"user_routes_Dnipro.csv.gz" : r"http://localhost:8888/files/data/Dnipro/user_routes_Dnipro.csv.gz?_xsrf=2%7Cd6e9e4ef%7Cd7e135b5f6f3923b5acce414981a2da0%7C1607176611",
	"user_transactions_Dnipro.csv.gz": r"http://localhost:8888/files/data/Dnipro/user_transactions_Dnipro.csv.gz?_xsrf=2%7Cd6e9e4ef%7Cd7e135b5f6f3923b5acce414981a2da0%7C1607176611"
}


for name, link in files.items():
	f = open(name, 'wb')
	ufr = requests.get(link)
	f.write(ufr.content)
	f.close()
