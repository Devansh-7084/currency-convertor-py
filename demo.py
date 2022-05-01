import requests
import json

url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"


currency_1="INR"
currency_2="USD"
amount="1000"
querystring = {"from":currency_1,"to":currency_2,"amount":amount}

headers = {
	"X-RapidAPI-Host": "currency-converter18.p.rapidapi.com",
	"X-RapidAPI-Key": "0312f6a735msha51914dcaa39c69p154fbajsn5dc7b8f5f52b"
}

response = requests.request("GET", url, headers=headers, params=querystring)
data = json.loads(response.text)
converted_amount = data["result"]["convertedAmount"]
formatted = "{:,.2f}".format(converted_amount)
print(converted_amount, formatted)