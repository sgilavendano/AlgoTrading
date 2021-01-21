import pandas as pd
import matplotlib as plt
import numpy as np
import statistics
import math
import quandl
quandl.ApiConfig.api_key = 'z8yaUmivVu3o-3KngVCH'


def get_macd():
  mydata = quandl.get("EIA/PET_RWTC_D", returns = "numpy")   #Crude oil
  mydata2 = quandl.get("EOD/AAPL", returns = "numpy")         #Apple
  mydata3 = quandl.get_table('ZACKS/FC', ticker='AAPL')
  x=[]
  y=[]
  sma5 =[]
  sma20 = []
  ema5 = []
  ema20 = []
  for data in mydata:
    x.append(data[0])
    y.append(data[1])
  #plt.pyplot.plot(x,y)
  x1=x[19:]
  x2=x[4:]
  for a in range(4,len(y)):
    if a>=19:
      avg20 = (y[a] + y[a-19] + y[a-18] + y[a-17] + y[a-16]+ y[a-15] + y[a-14] + y[a-13] + y[a-12] + y[a-11]+y[a-10] + y[a-9] + y[a-8] + y[a-7] + y[a-6]+ y[a-5] + y[a-4] + y[a-3] + y[a-2] + y[a-1])/20
      sma20.append(avg20)
    avg5 = (y[a] + y[a-1] + y[a-2] + y[a-3] + y[a-4])/5
    sma5.append(avg5)
  ema5.append(sma5[0])
  ema20.append(sma20[0])
  for b in range(1,len(sma20)):
    avg = ema20[b-1] * (19/21) + sma20[b] * (2/21)
    ema20.append(avg)
  for c in range(1,len(sma5)):
    avg = ema5[c-1] * (2/3) + sma5[c] * (1/3)
    ema5.append(avg)
  #plt.pyplot.plot(x1,ema20)
  #plt.pyplot.plot(x2,ema5)
  macd = ema5[15:]
  for x in range(0,len(ema20)):
    macd[x] = macd[x] - ema20[x]
  plt.pyplot.plot(x1,macd)
