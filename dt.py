from datetime import date,timedelta
import pandas

a=date(2016,12,31)
b=date(2012,01,01)
delta=a-b
dt=[]
latlng=[]
latlng.append((33.772075,-117.301693))
latlng.append((33.814950,-117.410128))
latlng.append((33.646022,-117.022423))
latlng.append((33.630516,-116.724520))
latlng.append((33.421856,-117.060749))
latlng.append((33.817085,-117.352568))
latlng.append((33.857526,-117.645040))
latlng.append((33.795914,-117.548616))
latlng.append((33.947397,-117.645247))
latlng.append((34.073197,-118.124811))
latlng.append((33.829637,-117.275557))
latlng.append((33.860361,-117.889261))
latlng.append((33.835541,-117.664297))
latlng.append((33.518854,-116.799979))
latlng.append((33.869040,-117.334131))
latlng.append((33.978369,-116.443634))
latlng.append((33.970143,-117.567584))
latlng.append((33.714613,-117.482912))
latlng.append((34.028453,-117.664164))
latlng.append((33.925934,-117.836481))
latlng.append((33.959510,-117.789654))
for j in latlng:
    for i in range(0,delta.days + 1):
        dt.append(str(j[0])+','+str(j[1])+','+str(b+timedelta(days=i))+'T12:00:00')

pd=pandas.DataFrame(dt)
pd.to_csv('postime.csv')
