import pandas as pd
import matplotlib as plt
import numpy as np
import statistics
import math
import quandl
#Import your own API
quandl.ApiConfig.api_key = bahbhsbvjkwenvknd


def get_macd():
  #mydata = quandl.get("EIA/PET_RWTC_D", returns = "numpy")   #Crude oil
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
def get_bollingerbands():
  #bol_data = quandl.get("EOD/AAPL", returns= "numpy")
  upper_bollingerband=[]
  lower_bollingerband=[]
  middlebollinger=[]
  xcord=[]
  ycord=[]

  for data in bol_data:
    xcord.append(data[0])
    ycord.append(data[1])
  
  #creating a tuple from the data
  xcord=xcord[19:]
  for a in range(19,len(ycord)):
    avg = (ycord[a] + ycord[a-19] + ycord[a-18] + ycord[a-17] + ycord[a-16]+ ycord[a-15] + ycord[a-14] + ycord[a-13] + ycord[a-12] + ycord[a-11]+ycord[a-10] + ycord[a-9] + ycord[a-8] + ycord[a-7] + ycord[a-6]+ ycord[a-5] + ycord[a-4] + ycord[a-3] + ycord[a-2] + ycord[a-1])/20
    middlebollinger.append(avg)
    templist= [ycord[a], ycord[a-19], ycord[a-18], ycord[a-17], ycord[a-16], ycord[a-15], ycord[a-14], ycord[a-13], ycord[a-12], ycord[a-11],ycord[a-10], ycord[a-9], ycord[a-8], ycord[a-7], ycord[a-6], ycord[a-5], ycord[a-4], ycord[a-3],ycord[a-2], ycord[a-1]]
    std = np.std(templist)
    #these if statements are not needed, but through seeing the data, i started noticing that 10-19 is the avg std and anything over and lower is extremely different
    #if(std> 20 ):
    #  print("this is an extremely volatile time to invest in")
    #if(std<10):
    #  print("At this point, there is little volatility")
    upper_bollingerband.append( avg + (std*2))
    lower_bollingerband.append( avg - (std*2))




    #upper_bollingerband = middlebollinger + np.std(middlebollinger.std *2)
    #lower_bollingerband = middlebollinger - np.std(middlebollinger.std *2)

  plt.pyplot.plot(xcord, middlebollinger)
  plt.pyplot.plot(xcord,upper_bollingerband)
  plt.pyplot.plot(xcord,lower_bollingerband)
  



  #print(bol_data)
  #print(bolpanddata)
  
def get_rsi():
  #mydata = quandl.get("EIA/PET_RWTC_D", returns = "numpy")   #Crude oil
  eod_data=[]
  time=[]
  rsi_data=[]
  for data in mydata:
    eod_data.append(data[1])
    time.append(data[0])
  for eod in range(13,len(eod_data)):
    loss_days=0
    gain_days=0
    gain=0
    loss=0
    for x in range(eod-13,eod-1):
      if eod_data[x]<eod_data[x+1]:
        gain = gain + ((eod_data[x+1]-eod_data[x])/eod_data[x])
        gain_days+=1
      elif eod_data[x]>eod_data[x+1]:
        loss = loss + ((eod_data[x]-eod_data[x+1])/eod_data[x])
        loss_days+=1
      if gain>0:
        avg_gain= gain/gain_days
      else:
        avg_gain = 0
      if loss> 0:
        avg_loss = loss/loss_days
      else:
        avg_loss = 0
    if avg_loss != 0:
      rsi = 100 - 100 / (1 + (avg_gain/avg_loss))
    else:
      rsi = 100
    rsi_data.append(rsi)
  time=time[13:]
  plt.pyplot.plot(time,rsi_data)