import pandas as pd

def get_city_num(x):
	return int(int(x)/1827)+1
	
def getDate(x):
	return x.split(',')[2].split('T')[0]
url='' #forget right now, do it tomorrow
df=pd.read_csv('postime.csv')
#print(df)
df['areacode']=df['Unnamed: 0'].apply(get_city_num)
df['tggl']=df['0'].apply(getDate)
df['tggl']=pd.to_datetime(df['tggl'])
del df['Unnamed: 0']
df.columns=['latlngtime','areacode','tggl']
df.to_csv('postime2.csv')