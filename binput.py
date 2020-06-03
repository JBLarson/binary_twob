from pandas import DataFrame
import pandas as pd
import numpy as np

#the event the two options relate to
#contract = "USD/JPY>108"
#contract = "AUD/USD"

contract = "USD/JPY"


#b1str is the buy side strike price

b1str = float(108.58)
b1avgp = 74.15
b1size = 100

s1str = float(108.74)
s1avgp = 29.02
s1size = -238

#additional positions

b2p = False
b2str = float(108.56)
b2avgp = 67
b2size = 100

s2p = True
s2str = float(108.66)
s2avgp = 33.75
s2size = -50



b1c = b1avgp * b1size
b1w = 100*b1size - (b1c)
s1c = abs(s1size) * (100-s1avgp)
s1w = (abs(s1size)*s1avgp)

b2c = b2avgp * b2size
b2w = 100*b2size - (b2c)
s2c = abs(s2size) * (100-s2avgp)
s2w = (abs(s2size)*s2avgp)


print()
print("1: " + contract + " > " + str(b1str) + " | size: " + str(b1size) + " | risk: $" + str(b1c) + " | net: $" + str(b1w))



print("2: " + contract + " > " + str(s1str) + " | size: " + str(s1size) + " | risk: $" + str(s1c) + " | net: $" + str(s1w))

if b2p == True:
	print("3: " + contract + " > " + str(b2str) + " | size: " + str(b2size) + " | risk: $" + str(b2c) + " | net: $" + str(b2w))


if s2p == True and b2p == True:
	print("4: " + contract + " > " + str(s2str) + " | size: " + str(s2size) + " | risk: $" + str(s2c) + " | net: $" + str(s2w))
elif s2p == True and b2p == False:
	print("3: " + contract + " > " + str(s2str) + " | size: " + str(s2size) + " | risk: $" + str(s2c) + " | net: $" + str(s2w))

print()

