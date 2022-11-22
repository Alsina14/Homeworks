import urllib.request
import json
import argparse

parser = argparse.ArgumentParser(description = "the exact time of the city")
parser.add_argument('region', type = str, help = 'Input region')
parser.add_argument('city', type = str, help = 'Input city')
args = parser.parse_args()

link0 = 'http://worldtimeapi.org/api/timezone/'
link = link0 + args.region + '/' + args.city

#открываю и читаю по ссылке и перевожу в строку
time = urllib.request.urlopen(link)
file = time.read().decode('utf-8')

#перевожу в словарь
f = json.loads(file)

#беру из словаря время
time0 = f["datetime"][11:19]
print(time0)