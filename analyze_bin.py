from pandas import DataFrame
import pandas as pd

import binput as bi

#was named analyze_scn_binary3 before analyze_bin

contract, b1c, b1w, s1c, s1w = bi.contract, bi.b1c, bi.b1w, bi.s1c, bi.s1w
b1str, b1avgp, b1size, s1str, s1avgp, s1size = bi.b1str, bi.b1avgp, bi.b1size, bi.s1str, bi.s1avgp, bi.s1size
b2p, b2c, b2w, s2p, s2c, s2w = bi.b2p, bi.b2c, bi.b2w, bi.s2p, bi.s2c, bi.s2w
b2str, b2avgp, b2size, s2str, s2avgp, s2size = bi.b2str, bi.b2avgp, bi.b2size, bi.s2str, bi.s2avgp, bi.s2size

#df resources
key = []
key.append("strike")
key.append("size")
key.append("price")
key.append("cost")
key.append("win")
b1x, b2x, s1x, s2x = [], [], [], []

#risk sum for og buy / sell side orders
tcost, tcost1, tcost2 = b1c + s1c, b1c + b2c + s1c, b1c + s1c + s2c

def positionDf():
	if b2p == True and s2p == False:
		www, wwL, Lww = b1w + s1w + b2w, b1w + s1w - b2c, -b1c + s1w + b2w
		wLw, LwL = b1w - s1c + b2w, -b1c + s1w - b2c

		for n in ['b1','s1', 'b2']:
			for s in [f'{n}str',f'{n}size',f'{n}avgp',f'{n}c',f'{n}w']:
				eval(f'{n}x').append(eval(s))

		sdf = pd.DataFrame({'key': key, 'b1': b1x, 's1': s1x, 'b2': b2x})
		sdf['avg'] = round((sdf['b1'] + sdf['b2'] + sdf['s1'])/3,ndigits=2)
		sdfavgc = (sdf['avg'][3])
		print(sdf)

	elif b2p == False and s2p == True:
		www, wwL, Lww = s1w + b1w + s2w, s1w + b1w - s2c, -s1c + b1w + s2w
		wLw, LwL = s1w - b1c + s2w, -s1c + b1w - s2c

		for n in ['b1','s1', 's2']:
			for s in [f'{n}str',f'{n}size',f'{n}avgp',f'{n}c',f'{n}w']:
				eval(f'{n}x').append(eval(s))

		sdf = pd.DataFrame({'key': key, 'b1': b1x, 's1': s1x, 's2': s2x})
		sdf['avg'] = round((sdf['b1'] + sdf['s1'] + sdf['s2'])/3,ndigits=2)
		avgcost = (sdf['avg'][3])
		print(sdf)

	elif b2p == False and s2p == False:
		ww1, wL1 = round((b1w+s1w),ndigits=2), round((b1w-s1c),ndigits=2)
		Lw1 = round((s1w-b1c),ndigits=2)
		roiww, roiwL = round(((ww1/tcost)*100),ndigits=2), round(((wL1/tcost)*100),ndigits=2)
		roiLw = round(((Lw1/tcost)*100),ndigits=2)

		for n in ['b1','s1']:
			for s in [f'{n}str',f'{n}size',f'{n}avgp',f'{n}c',f'{n}w']:
				eval(f'{n}x').append(eval(s))

		s1b1 = pd.DataFrame({'key': key, 'b1': b1x, 's1': s1x})
		#s1b1['avg'] = round((s1b1['b1'] + s1b1['s1']) /2,ndigits=2)
		#avgcost = (s1b1['avg'][3])
		print(s1b1)



def desc_decr(scnDf):
	def wrapper():
		print()
		positionDf()
		print()
		scnDf()

		print()
	return wrapper

@desc_decr



def scnDf():
	if b2p == True and s2p == False:
		www, wwL, Lww = b1w + s1w + b2w, b1w + s1w - b2c, -b1c + s1w + b2w
		wLw, LwL = b1w - s1c + b2w, -b1c + s1w - b2c

		for n in ['scn']:
			for s in [f'{n}str',f'{n}size',f'{n}avgp',f'{n}c',f'{n}w']:
				eval(f'{n}x').append(eval(s))

		sdf = pd.DataFrame({'key': key1, 'b1': b1x, 's1': s1x, 'b2': b2x})
		sdf['avg'] = round((sdf['b1'] + sdf['b2'] + sdf['s1'])/3,ndigits=2)
		sdfavgc = (sdf['avg'][3])
		#print(sdf)

	elif b2p == False and s2p == True:
		www, wwL, Lww = s1w + b1w + s2w, s1w + b1w - s2c, -s1c + b1w + s2w
		wLw, LwL = s1w - b1c + s2w, -s1c + b1w - s2c

		for n in ['b1','s1', 's2']:
			for s in [f'{n}str',f'{n}size',f'{n}avgp',f'{n}c',f'{n}w']:
				eval(f'{n}x').append(eval(s))

		sdf = pd.DataFrame({'key': key1, 'b1': b1x, 's1': s1x, 's2': s2x})
		sdf['avg'] = round((sdf['b1'] + sdf['s1'] + sdf['s2'])/3,ndigits=2)
		avgcost = (sdf['avg'][3])
		#print(sdf)

	elif b2p == False and s2p == False:
		key1 = []
		key1.append("ww")
		key1.append("wL")
		key1.append("Lw")

		qww1, qwL1 = round((b1w+s1w),ndigits=2), round((b1w-s1c),ndigits=2)
		qLw1 = round((s1w-b1c),ndigits=2)
		qroiww, qroiwL = round(((qww1/tcost)*100),ndigits=2), round(((qwL1/tcost)*100),ndigits=2)
		qroiLw = round(((qLw1/tcost)*100),ndigits=2)
		scn0, roi = [qww1, qwL1, qLw1], [qroiww, qroiwL, qroiLw]
		scsum = sum(scn0)

		sdf = pd.DataFrame({'key': key1, 'scn$': scn0, 'roi%': roi})
		#sdf['dm%'] = round(((sdf['scn$'] - scsum)/scsum)*100,ndigits=2)
	
		print(sdf)


print()
