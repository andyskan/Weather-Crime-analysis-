from requests import get
import pandas as pd
keys=[]
keysnum=0
keyscount=0
url='https://api.darksky.net/forecast/'
def get_weather(latlngtime):
	global url
	global keysnum
	global keyscount
	req=get(url+keys[keysnum]+'/'+latlngtime)
	keyscount+=1
	if keyscount==980:
		keysnum+=1
		keyscount=0
	a=req.json()
	return a['daily']['data'][0]['summary']

with open('key.txt','r') as f:
    for lines in f:
        keys.append(lines)
pt=pd.read_csv('postime2.csv')
pt['weather']=pt['latlngtime'].apply(get_weather)
pt.to_csv('withweather.csv')