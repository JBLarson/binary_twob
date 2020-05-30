from pandas import DataFrame
import pandas as pd
import numpy as np

#the event the two options relate to
contract = "USD/JPY>17"

#buy/sell side strike prices
bstr = float(0.70)
bavgp = 77
bsize = 10

sstr = float(0.82)
savgp = 30.75
ssize = -12




bcost = bavgp * bsize
bwin = 100*bsize - (bcost)
scost = abs(ssize) * (100-savgp)
swin = (abs(ssize)*savgp)

ww = round((bwin+swin),ndigits=2)
wL = round((bwin-scost),ndigits=2)
Lw = round((swin-bcost),ndigits=2)






print()
print(contract + str(bstr) + " | size: " + str(bsize) + " | risk: $" + str(bcost) + " | net: $" + str(bwin))

print(contract + str(sstr) + " | size: " + str(ssize) + " | risk: $" + str(scost) + " | net: $" + str(swin))

print()

print("win-win: $" + str(ww) + " o: " + str(bstr) + " u: " + str(sstr))
print("win-loss: $" + str(wL) + " o: " + str(bstr) + " o: " + str(sstr))
print("loss-win: $" + str(Lw) + " u: " + str(bstr) + " u: " + str(sstr))

print()













scn = [ww, wL, Lw]
scnavg = sum(scn)/len(scn)



scnp = np.array(scn)


analysis = pd.DataFrame({'scn': scnp}, index=['ww', 'wL', 'Lw'])

analysis['d'] = analysis['scn'] - scnavg
analysis['dm'] = analysis['d'] / scnavg



dmnp = np.array(analysis['dm'])

scnnp = np.array(analysis['scn'])

key = ['ww', 'wL', 'Lw']

scndf = pd.DataFrame({'key': key, 'scn': scn, 'dm': dmnp})






print(scndf)

print()


