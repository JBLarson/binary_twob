from pandas import DataFrame
import pandas as pd
import numpy as np

#bstr: strike price for the option you bought
bstr = float(132)
bavgp = 40
bsize = 10
bcost = bavgp * bsize

bwin = 100*bsize - (bcost)

#print(bwin)

sstr = float(134)
savgp = 66
ssize = -15
scost = abs(ssize) * 100 - (abs(ssize))*savgp
swin = (abs(ssize)*100 - scost)

#print(swin)

bs = round((bwin+swin),ndigits=2)
bb = round((bwin-scost),ndigits=2)
ss = round((swin-bcost),ndigits=2)

scn = [bs, bb, ss]
scnavg = sum(scn)/len(scn)



scnp = np.array(scn)


scndm = []

for val in scnp:
	scndm.append((val - scnavg)/scnavg)

#analysis = pd.DataFrame({'bs': bs, 'bb': bb, 'ss': ss}, index=['scn'])

analysis = pd.DataFrame({'scn': scnp}, index=['bs', 'bb', 'ss'])



analysis['d'] = analysis['scn'] - scnavg

analysis['dm'] = analysis['d'] / scnavg

analysis.drop(["d"], axis=1)
print()
print(analysis)

#scndf = pd.DataFrame({analysis['scn'], analysis['dm']})

scndf = analysis['scn']
dmdf = analysis['dm']
dmnp = np.array(dmdf)

scnnp = np.array(scndf)

key = ['bs', 'bb', 'ss']

anal = pd.DataFrame({'key': key, 'scn': scnnp, 'dm': dmnp})
print()



print(anal)

#analysis['dm']
print()

#scndf = pd.DataFrame({'scn': scndf}, index=['val'])





