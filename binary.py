from pandas import DataFrame
import pandas as pd
import numpy as np

#bstr: strike price for the option you bought
bstr = float(107.78)
bavgp = 47.75
bsize = 10
bcost = bavgp * bsize

bwin = 100*bsize - (bcost)

#print(bwin)

sstr = float(107.82)
savgp = 17
ssize = -18
scost = abs(ssize) * (100-savgp)
swin = (abs(ssize)*savgp)

ww = round((bwin+swin),ndigits=2)
wL = round((bwin-scost),ndigits=2)
Lw = round((swin-bcost),ndigits=2)

print()

print("USD/JPY>" + str(bstr) + " size: " + str(bsize) + " risk: $" + str(bcost) + " net: $" + str(bwin))

print("USD/JPY>" + str(sstr) + " size: " + str(ssize) + " risk: $" + str(scost) + " net: $" + str(swin))

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

scndf = pd.DataFrame({'key': key, 'scn': scnnp, 'dm': dmnp})


print(scn)


print()



print(scndf)

print()






