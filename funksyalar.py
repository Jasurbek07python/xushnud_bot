import json
import requests
def lakatsyani_aniqlash(shahar):
	url = "https://geocoding-by-api-ninjas.p.rapidapi.com/v1/geocoding"

	querystring = {"city": f"{shahar}"}

	headers = {
		"x-rapidapi-key": "7fccb5c328msh61e064a9bb9af66p1f7553jsn518d251a8cb3",
		"x-rapidapi-host": "geocoding-by-api-ninjas.p.rapidapi.com"
	}

	response = requests.request("GET", url, headers=headers, params=querystring)
	if response.status_code==200:
		data=json.loads(response.text)
		lati=data[0]['latitude']
		long=data[0]['longitude']
		loc=[lati,long]
		return loc
	else:
		return  "Error"
def obhavo(shahar):
	url = "https://weatherapi-com.p.rapidapi.com/current.json"

	querystring = {"q": f"{shahar[0]},{shahar[1]}"}

	headers = {
		"x-rapidapi-key": "7fccb5c328msh61e064a9bb9af66p1f7553jsn518d251a8cb3",
		"x-rapidapi-host": "weatherapi-com.p.rapidapi.com"
	}

	response = requests.request("GET",url, headers=headers, params=querystring)
	if response.status_code==200:
		data=json.loads(response.text)
		info=(
			f"🏙shahar:{data['location']['name']}\n"
			f"🌆davlat:{data['location']['country']}\n"
			f"vaqt mintaqasi:{data['location']['tz_id']}\n"
			f"havo harorati {data['current'] ['last_updated']} holatida "
			f"{data['current']['temp_c']}℃\n"
		)
		return info
