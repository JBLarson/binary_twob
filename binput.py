from pandas import DataFrame
import pandas as pd
import numpy as np

#the event the two options relate to
#contract = "USD/JPY>108"
contract = "AUD/USD"

#b1str is the buy side strike price

b1str = float(.6884)
b1avgp = 81.25
b1size = 10

s1str = float(.6901)
s1avgp = 18.25
s1size = -80

#additional positions

b2p = False
b2str = float(.688)
b2avgp = 70.5
b2size = 60

s2p = False
s2str = float(0.84)
s2avgp = 36.5
s2size = -400



b1cost = b1avgp * b1size
b1win = 100*b1size - (b1cost)
s1cost = abs(s1size) * (100-s1avgp)
s1win = (abs(s1size)*s1avgp)

b2cost = b2avgp * b2size
b2win = 100*b2size - (b2cost)
s2cost = abs(s2size) * (100-s2avgp)
s2win = (abs(s2size)*s2avgp)


print()
print("1: " + contract + " > " + str(b1str) + " | size: " + str(b1size) + " | risk: $" + str(b1cost) + " | net: $" + str(b1win))



print("2: " + contract + " > " + str(s1str) + " | size: " + str(s1size) + " | risk: $" + str(s1cost) + " | net: $" + str(s1win))

if b2p == True:
	print("3: " + contract + " > " + str(b2str) + " | size: " + str(b2size) + " | risk: $" + str(b2cost) + " | net: $" + str(b2win))


if s2p == True and b2p == True:
	print("4: " + contract + " > " + str(s2str) + " | size: " + str(s2size) + " | risk: $" + str(s2cost) + " | net: $" + str(s2win))
elif s2p == True and b2p == False:
	print("3: " + contract + " > " + str(s2str) + " | size: " + str(s2size) + " | risk: $" + str(s2cost) + " | net: $" + str(s2win))

print()

