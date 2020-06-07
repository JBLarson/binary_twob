from pandas import DataFrame
import pandas as pd
import numpy as np

#the event the two options relate to
#contract = "USD/JPY>108"
#contract = "AUD/USD"

contract = "USD/JPY"

#b1str is the buy side strike price

b1p, b1str, b1avgp, b1size = False, float(108.94), 51, 100

s1p, s1str, s1avgp, s1size = False, float(109.14), 65, 45

#additional positions

b2p, b2str, b2avgp, b2size = False, float(108.94), 51, 100

s2p, s2str, s2avgp, s2size = False, float(109.24), 65, 45

b1c, b2c = (b1avgp * b1size), (b2avgp * b2size)
b1w, s1c, s1w = 100*b1size - (b1c), abs(s1size) * (100-s1avgp), (abs(s1size)*s1avgp)
b2w, s2c, s2w = 100*b2size - (b2c), abs(s2size) * (100-s2avgp), (abs(s2size)*s2avgp)
