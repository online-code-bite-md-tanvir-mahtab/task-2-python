import requests

RUL_ENDPOINT = 'https://gorest.co.in/public/v1/users'
params = {
  'token': 'd7c01847de4c083cb154e9a533294301e9f05f93dbae7d589e42ece63226c0a3',
}

response = requests.get(url=f"{RUL_ENDPOINT}?{params}")
# raise an error
response.raise_for_status()
data = response.json()['data']
print(len(data))
for items in data:
  id = items['id']
  name = items['name']
  email = items['email']
  gender = items['gender']
  status = items['status']
  print(f"Name:{name}\n Id:{id}\n Email:{email}\n Gender:{gender}\n Status:{status}\n\n\n")