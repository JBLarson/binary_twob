import binput as bi

b1cost, b1win, s1cost, s1win = bi.b1cost, bi.b1win, bi.s1cost, bi.s1win
b1str, b1avgp, b1size, s1str, s1avgp, s1size = bi.b1str, bi.b1avgp, bi.b1size, bi.s1str, bi.s1avgp, bi.s1size
b2p, b2cost, b2win, s2p, s2cost, s2win = bi.b2p, bi.b2cost, bi.b2win, bi.s2p, bi.s2cost, bi.s2win
b2str, b2avgp, b2size, s2str, s2avgp, s2size = bi.b2str, bi.b2avgp, bi.b2size, bi.s2str, bi.s2avgp, bi.s2size
contract = bi.contract

tcost1 = b1cost + s1cost

bcostsum = b1cost + b2cost
bcost = b1cost
if b2p == True:
	bcost = bcostsum
	bavgp = (b1cost + b2cost) / (b1size + b2size)
else:
	bavgp = b1avgp

scostsum = s1cost + s2cost
scost = s1cost
if s2p == True:
	scost = scostsum
	#savgp = (s1cost + s2cost) / (s1size + s2size) #not how it works

tcost = round(scost + bcost, ndigits=2)


ww1 = round((b1win+s1win),ndigits=2)
wL1 = round((b1win-s1cost),ndigits=2)
Lw1 = round((s1win-b1cost),ndigits=2)

#title variables for win and loss scenarios
b1wT = contract + ">" + str(b1str)
b1LT = contract + "<" + str(b1str)
s1wT = contract + "<" + str(s1str)
s1LT = contract + ">" + str(s1str)


print("win-win: $", str(ww1), " | ", b1wT, " | ", s1wT)
print("win-loss: $", str(wL1), " | ", b1wT, " | ", s1LT)
print("loss-win: $", str(Lw1), " | ", b1LT, " | ", s1wT)

print()

#ROI

roiww = round(((ww1/tcost1)*100),ndigits=2)
roiwL = round(((wL1/tcost1)*100),ndigits=2)
roiLw = round(((Lw1/tcost1)*100),ndigits=2)

print("ROI win-win: ", roiww, "%")
print("ROI win-loss: ", roiwL, "%")
print("ROI loss-win: ", roiLw, "%")

print()
