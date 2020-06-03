from pandas import DataFrame
import pandas as pd


import binput2 as bi

contract, b1c, b1w, s1c, s1w = bi.contract, bi.b1c, bi.b1w, bi.s1c, bi.s1w
b1str, b1avgp, b1size, s1str, s1avgp, s1size = bi.b1str, bi.b1avgp, bi.b1size, bi.s1str, bi.s1avgp, bi.s1size
b2p, b2c, b2w, s2p, s2c, s2w = bi.b2p, bi.b2c, bi.b2w, bi.s2p, bi.s2c, bi.s2w
b2str, b2avgp, b2size, s2str, s2avgp, s2size = bi.b2str, bi.b2avgp, bi.b2size, bi.s2str, bi.s2avgp, bi.s2size

#risk sum for og buy / sell side orders
tcost, tcost1, tcost2 = b1c + s1c, b1c + b2c + s1c, b1c + s1c + s2c

#contract = ''

b1wT, b2wT = contract + ">" + str(b1str), contract + ">" + str(b2str)
b1LT, b2LT = contract + "<" + str(b1str), contract + "<" + str(b2str)
s1wT, s1LT = contract + "<" + str(s1str), contract + ">" + str(s1str)
s2wT, s2LT = contract + "<" + str(s2str), contract + ">" + str(s2str)



#two buy's one sell
if b2p == True and s2p == False:

	www, wwL, Lww = b1w + s1w + b2w, b1w + s1w - b2c, -b1c + s1w + b2w
	wLw, LwL = b1w - s1c + b2w, -b1c + s1w - b2c


	b1H = False
	if b1str > b2str: b1H = True

	if b1H == True: #strike price of 1st buy > 2nd buy
		roiwww, roiLww = round(((www/tcost2)*100),ndigits=2), round(((Lww/tcost2)*100),ndigits=2)
		roiwLw, roiLwL = round(((wLw/tcost2)*100),ndigits=2), round(((LwL/tcost2)*100),ndigits=2)

		print("www: $", round(www,ndigits=2), " | ROI: ", roiwww, "% | ", b1wT, " | ", s1wT, " | ", b2wT)
		print("Lww: $", round(Lww,ndigits=2), " | ROI: ", roiLww, "% | ", b1LT, " | ", s1wT, " | ", b2wT)
		print("wLw: $", round(wLw,ndigits=2), " | ROI: ", roiwLw, "% | ", b1wT, " | ", s1LT, " | ", b2wT)
		print("LwL: $", round(LwL,ndigits=2), " | ROI: ", roiLwL, "% | ", b1LT, " | ", s1wT, " | ", b2LT)
		ss = www + Lww + wLw + LwL
		print("Scenario ∑: $", ss)

	elif b1H == False:

		roiwww, roiwwL = round(((www/tcost2)*100),ndigits=2), round(((wwL/tcost2)*100),ndigits=2)
		roiwLw, roiLwL = round(((wLw/tcost2)*100),ndigits=2), round(((LwL/tcost2)*100),ndigits=2)

		print("www: $", round(www,ndigits=2), " | ROI: ", roiwww, "% | ", b1wT, " | ", s1wT, " | ", b2wT)
		print("wwL: $", round(wwL,ndigits=2), " | ROI: ", roiwwL, "% | ", b1wT, " | ", s1wT, " | ", b2LT)
		print("wLw: $", round(wLw,ndigits=2), " | ROI: ", roiwLw, "% | ", b1wT, " | ", s1LT, " | ", b2wT)
		print("LwL: $", round(LwL,ndigits=2), " | ROI: ", roiLwL, "% | ", b1LT, " | ", s1wT, " | ", b2LT)
		ss = www + wwL + wLw + LwL
		print("Scenario ∑: $", ss)

#two sell's one buy
if b2p == False and s2p == True:

	www, wwL, Lww = s1w + b1w + s2w, s1w + b1w - s2c, -s1c + b1w + s2w
	wLw, LwL = s1w - b1c + s2w, -s1c + b1w - s2c


	s1H = False
	if s1str > s2str: s1H = True

	if s1H == True: #strike price of 1st buy > 2nd buy

		roiwww, roiwwL = round(((www/tcost2)*100),ndigits=2), round(((wwL/tcost2)*100),ndigits=2)
		roiwLw, roiLwL = round(((wLw/tcost2)*100),ndigits=2), round(((LwL/tcost2)*100),ndigits=2)

		print("www: $", round(www,ndigits=2), " | ROI: ", roiwww, "% | ", s1wT, " | ", b1wT, " | ", s2wT)
		print("wwL: $", round(wwL,ndigits=2), " | ROI: ", roiwwL, "% | ", s1wT, " | ", b1wT, " | ", s2LT)
		print("wLw: $", round(wLw,ndigits=2), " | ROI: ", roiwLw, "% | ", s1wT, " | ", b1LT, " | ", s2wT)
		print("LwL: $", round(LwL,ndigits=2), " | ROI: ", roiLwL, "% | ", s1LT, " | ", b1wT, " | ", s2LT)
		ss = www + wwL + wLw + LwL
		print("Scenario ∑: $", ss)

	elif s1H == False:
		roiwww, roiLww = round(((www/tcost2)*100),ndigits=2), round(((Lww/tcost2)*100),ndigits=2)
		roiwLw, roiLwL = round(((wLw/tcost2)*100),ndigits=2), round(((LwL/tcost2)*100),ndigits=2)

		print("www: $", round(www,ndigits=2), " | ROI: ", roiwww, "% | ", s1wT, " | ", b1wT, " | ", s2wT)
		print("Lww: $", round(Lww,ndigits=2), " | ROI: ", roiLww, "% | ", s1LT, " | ", b1wT, " | ", s2wT)
		print("wLw: $", round(wLw,ndigits=2), " | ROI: ", roiwLw, "% | ", b1wT, " | ", b1LT, " | ", s2wT)
		print("LwL: $", round(LwL,ndigits=2), " | ROI: ", roiLwL, "% | ", s1LT, " | ", b1wT, " | ", s2LT)

		ss = www + Lww + wLw + LwL
		print("Scenario ∑: $", ss)
#one buy one sell

if b2p == False and s2p == False:
	ww1, wL1 = round((b1w+s1w),ndigits=2), round((b1w-s1c),ndigits=2)
	Lw1 = round((s1w-b1c),ndigits=2)

	roiww, roiwL = round(((ww1/tcost)*100),ndigits=2), round(((wL1/tcost)*100),ndigits=2)
	roiLw = round(((Lw1/tcost)*100),ndigits=2)

	print("win-win: $", str(wround(w1),ndigits=2), " | ROI:", roiww, "% | ", b1wT, " | ", s1wT)
	print("win-loss: $", str(wround(L1),ndigits=2), " | ROI:", roiwL, "% | ", b1wT, " | ", s1LT)
	print("loss-win: $", str(Lround(w1),ndigits=2), " | ROI:", roiLw, "% | ", b1LT, " | ", s1wT)
	ss = ww1 + wL1 + Lw1
	print("Scenario ∑: $", ss)

	print()





#two buy's one sell
if b2p == True and s2p == False:

	www, wwL, Lww = b1w + s1w + b2w, b1w + s1w - b2c, -b1c + s1w + b2w
	wLw, LwL, key = b1w - s1c + b2w, -b1c + s1w - b2c, []


	key.append("strike")
	key.append("size")
	key.append("price")
	key.append("cost")
	key.append("win")

	b1x, b2x, s1x = [], [], []

	for n in ['b1','s1', 'b2']:
		for s in [f'{n}str',f'{n}size',f'{n}avgp',f'{n}c',f'{n}w']:
			eval(f'{n}x').append(eval(s))


	b2s1 = pd.DataFrame({'key': key, 'b1': b1x, 's1': s1x, 'b2': b2x})

	b2s1['avg'] = round((b2s1['b1'] + b2s1['b2'] + b2s1['s1'])/3,ndigits=2)

	b2s1avgc = (b2s1['avg'][3])



	print()

	print(b2s1)



elif b2p == False and s2p == True:

	www, wwL, Lww = s1w + b1w + s2w, s1w + b1w - s2c, -s1c + b1w + s2w
	wLw, LwL, key = s1w - b1c + s2w, -s1c + b1w - s2c, []

	key.append("strike")
	key.append("size")
	key.append("price")
	key.append("cost")
	key.append("win")

	b1x, s2x, s1x = [], [], []

	for n in ['b1','s1', 's2']:
		for s in [f'{n}str',f'{n}size',f'{n}avgp',f'{n}c',f'{n}w']:
			eval(f'{n}x').append(eval(s))


	s2b1 = pd.DataFrame({'key': key, 'b1': b1x, 's1': s1x, 's2': s2x})

	s2b1['avg'] = round((s2b1['b1'] + s2b1['s1'] + s2b1['s2'])/3,ndigits=2)

	avgcost = (s2b1['avg'][3])



	print()

	print(s2b1)


if b2p == False and s2p == False:
	ww1, wL1 = round((b1w+s1w),ndigits=2), round((b1w-s1c),ndigits=2)
	Lw1 = round((s1w-b1c),ndigits=2)

	roiww, roiwL = round(((ww1/tcost)*100),ndigits=2), round(((wL1/tcost)*100),ndigits=2)
	roiLw = round(((Lw1/tcost)*100),ndigits=2)


	ss = ww1 + wL1 + Lw1



print()
