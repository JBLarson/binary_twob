import binput as bi

b1cost, b1win, s1cost, s1win = bi.b1cost, bi.b1win, bi.s1cost, bi.s1win
b1str, b1avgp, b1size, s1str, s1avgp, s1size = bi.b1str, bi.b1avgp, bi.b1size, bi.s1str, bi.s1avgp, bi.s1size
b2p, b2cost, b2win, s2p, s2cost, s2win = bi.b2p, bi.b2cost, bi.b2win, bi.s2p, bi.s2cost, bi.s2win
b2str, b2avgp, b2size, s2str, s2avgp, s2size = bi.b2str, bi.b2avgp, bi.b2size, bi.s2str, bi.s2avgp, bi.s2size
contract = bi.contract

#risk sum for og buy / sell side orders
tcost1, tcost2, tcost3 = b1cost + s1cost, b1cost + b2cost + s1cost, b1cost + s1cost + s2cost

#calculate avg price if there are two buy side orders
bcostsum, bcost = b1cost + b2cost, b1cost
#b2p: is bet 2 placed? variable
if b2p == True:
	bcost = bcostsum
	bavgp = (b1cost + b2cost) / (b1size + b2size)
else: bavgp = b1avgp

scostsum, scost = s1cost + s2cost, s1cost
if s2p == True: scost = scostsum
	#savgp = (s1cost + s2cost) / (s1size + s2size) #not how it works

tcost = round(scost + bcost, ndigits=2)

b1wT, b2wT = contract + ">" + str(b1str), contract + ">" + str(b2str)
b1LT, b2LT = contract + "<" + str(b1str), contract + "<" + str(b2str)
s1wT, s1LT = contract + "<" + str(s1str), contract + ">" + str(s1str)
s2wT, s2LT = contract + "<" + str(s2str), contract + ">" + str(s2str)



#two buy's one sell
if b2p == True and s2p == False:

	www, wwL, Lww = b1win + s1win + b2win, b1win + s1win - b2cost, -b1cost + s1win + b2win
	wLw, LwL = b1win - s1cost + b2win, -b1cost + s1win - b2cost


	b1H = False
	if b1str > b2str: b1H = True

	if b1H == True: #strike price of 1st buy > 2nd buy

		roiwww = round(((www/tcost2)*100),ndigits=2)
		roiLww = round(((Lww/tcost2)*100),ndigits=2)
		roiwLw = round(((wLw/tcost2)*100),ndigits=2)
		roiLwL = round(((LwL/tcost2)*100),ndigits=2)

		print("www: $", www, " | ROI: ", roiwww, "% | ", b1wT, " | ", s1wT, " | ", b2wT)
		print("Lww: $", Lww, " | ROI: ", roiLww, "% | ", b1LT, " | ", s1wT, " | ", b2wT)
		print("wLw: $", wLw, " | ROI: ", roiwLw, "% | ", b1wT, " | ", s1LT, " | ", b2wT)
		print("LwL: $", LwL, " | ROI: ", roiLwL, "% | ", b1LT, " | ", s1wT, " | ", b2LT)
		ss = www + Lww + wLw + LwL
		print("Scenario ∑: $", ss)

	elif b1H == False:

		roiwww = round(((www/tcost2)*100),ndigits=2)
		roiLww = round(((wwL/tcost2)*100),ndigits=2)
		roiwLw = round(((wLw/tcost2)*100),ndigits=2)
		roiLwL = round(((LwL/tcost2)*100),ndigits=2)

		print("www: $", www, " | ROI: ", roiwww, "% | ", b1wT, " | ", s1wT, " | ", b2wT)
		print("wwL: $", wwL, " | ROI: ", roiwwL, "% | ", b1wT, " | ", s1wT, " | ", b2LT)
		print("wLw: $", wLw, " | ROI: ", roiwLw, "% | ", b1wT, " | ", s1LT, " | ", b2wT)
		print("LwL: $", LwL, " | ROI: ", roiLwL, "% | ", b1LT, " | ", s1wT, " | ", b2LT)
		ss = www + wwL + wLw + LwL
		print("Scenario ∑: $", ss)

#two sell's one buy
if b2p == False and s2p == True:

	www, wwL, Lww = s1win + b1win + s2win, s1win + b1win - s2cost, -s1cost + b1win + s2win
	wLw, LwL = s1win - b1cost + s2win, -s1cost + b1win - s2cost


	s1H = False
	if s1str > s2str: s1H = True

	if s1H == True: #strike price of 1st buy > 2nd buy

		roiwww = round(((www/tcost3)*100),ndigits=2)
		roiwwL = round(((wwL/tcost3)*100),ndigits=2)
		roiwLw = round(((wLw/tcost3)*100),ndigits=2)
		roiLwL = round(((LwL/tcost3)*100),ndigits=2)

		print("www: $", www, " | ROI: ", roiwww, "% | ", s1wT, " | ", b1wT, " | ", s2wT)
		print("wwL: $", wwL, " | ROI: ", roiwwL, "% | ", s1wT, " | ", b1wT, " | ", s2LT)
		print("wLw: $", wLw, " | ROI: ", roiwLw, "% | ", s1wT, " | ", b1LT, " | ", s2wT)
		print("LwL: $", LwL, " | ROI: ", roiLwL, "% | ", s1LT, " | ", b1wT, " | ", s2LT)
		ss = www + wwL + wLw + LwL
		print("Scenario ∑: $", ss)
	elif s1H == False:
		roiwww = round(((www/tcost3)*100),ndigits=2)
		roiLww = round(((Lww/tcost3)*100),ndigits=2)
		roiwLw = round(((wLw/tcost3)*100),ndigits=2)
		roiLwL = round(((LwL/tcost3)*100),ndigits=2)

		print("www: $", www, " | ROI: ", roiwww, "% | ", s1wT, " | ", b1wT, " | ", s2wT)
		print("Lww: $", Lww, " | ROI: ", roiLww, "% | ", s1LT, " | ", b1wT, " | ", s2wT)
		print("wLw: $", wLw, " | ROI: ", roiwLw, "% | ", b1wT, " | ", b1LT, " | ", s2wT)
		print("LwL: $", LwL, " | ROI: ", roiLwL, "% | ", s1LT, " | ", b1wT, " | ", s2LT)

		ss = www + Lww + wLw + LwL
		print("Scenario ∑: $", ss)
#one buy one sell

if b2p == False and s2p == False:
	ww1 = round((b1win+s1win),ndigits=2)
	wL1 = round((b1win-s1cost),ndigits=2)
	Lw1 = round((s1win-b1cost),ndigits=2)

	#title variables for win and loss scenarios

	roiww = round(((ww1/tcost1)*100),ndigits=2)
	roiwL = round(((wL1/tcost1)*100),ndigits=2)
	roiLw = round(((Lw1/tcost1)*100),ndigits=2)

	print("win-win: $", str(ww1), " | ROI:", roiww, "% | ", b1wT, " | ", s1wT)
	print("win-loss: $", str(wL1), " | ROI:", roiwL, "% | ", b1wT, " | ", s1LT)
	print("loss-win: $", str(Lw1), " | ROI:", roiLw, "% | ", b1LT, " | ", s1wT)
	ss = ww1 + wL1 + Lw1
	print("Scenario ∑: $", ss)

	print()



print()