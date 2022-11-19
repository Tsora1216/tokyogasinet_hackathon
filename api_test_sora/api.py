import requests
money = 50
url = 'https://toukyogasinethackathon.azurewebsites.net/api/HttpTrigger2?code=7KI8PBRSyakmetbKcuBjAeZLmU2BArfCBJ3SEQBfMPJNAzFu6MOBJQ==&name='+str(money)
response = requests.get(url)
num= response.text
