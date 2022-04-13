import requests
import json

request = requests.get("https://www.dan.me.uk/torlist/?exit")
with open('lista_ips.txt', 'w') as file:
    file.writelines(request.text)
lista_ips = []
request = requests.get("https://onionoo.torproject.org/summary?limit=5000")
dict = json.loads(request.text)

with open('lista_ips.txt', 'a') as file:
    for i in range(len(dict ['relays'])):
        file.writelines(f"{dict['relays'] [i] ['a'] [0]}\n")

with open('lista_ips.txt', 'r') as file:
    linhas = [line.strip() for line in file]
    lista_ips.append(f"{linhas}\n")