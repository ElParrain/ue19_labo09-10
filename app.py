import requests

r = requests.get('https://punapi.rest/api/pun')
print(f'Word game: {r.json()["pun"]}')   
